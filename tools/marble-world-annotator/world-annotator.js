import * as THREE from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";
import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";
import { SparkRenderer, SplatMesh } from "@sparkjsdev/spark";

const DEFAULT_ROOT = "../../canyon-rpg/assets/worlds/canyon-waterfall/";
const DEFAULT_IMAGE = `${DEFAULT_ROOT}canyon-waterfall-reference.jpeg`;
const DEFAULT_GLB = `${DEFAULT_ROOT}canyon-waterfall-collider.glb`;
const DEFAULT_SPZ = `${DEFAULT_ROOT}canyon-waterfall-100k.spz`;

const ui = {
  imageInput: document.querySelector("#imageInput"),
  splatPreset: document.querySelector("#splatPreset"),
  spzInput: document.querySelector("#spzInput"),
  glbInput: document.querySelector("#glbInput"),
  jsonInput: document.querySelector("#jsonInput"),
  imagePane: document.querySelector("#imagePane"),
  imageStage: document.querySelector("#imageStage"),
  imageDropHint: document.querySelector("#imageDropHint"),
  modelPane: document.querySelector("#modelPane"),
  modelDropHint: document.querySelector("#modelDropHint"),
  imageName: document.querySelector("#imageName"),
  modelName: document.querySelector("#modelName"),
  canvas: document.querySelector("#referenceCanvas"),
  viewport: document.querySelector("#viewport"),
  picker: document.querySelector("#landmarkPicker"),
  selected: document.querySelector("#selected"),
  status: document.querySelector("#status"),
  summary: document.querySelector("#summary"),
  note: document.querySelector("#anchorNote"),
  annotator: document.querySelector("#annotator"),
  reviewed: document.querySelector("#humanReviewed"),
};
const imageContext = ui.canvas.getContext("2d");
const landmarks = [];
const seedPixels = new Map();
const records = new Map();
const markers = new Map();
let image = null;
let glbRoot = null;
let splatRoot = null;
let showSplat = true;
let flipY = true;
let colliderOriginalMaterials = new WeakMap();
let colliderUseNormalMaterial = false;
let currentImageName = "canyon-waterfall-reference.jpeg";
let currentGlbName = "canyon-waterfall-collider.glb";
let currentSpzName = "canyon-waterfall-100k.spz";

const scene = new THREE.Scene();
scene.background = new THREE.Color("#172123");
scene.add(new THREE.HemisphereLight("#ffffff", "#48645d", 2.3));
const keyLight = new THREE.DirectionalLight("#ffffff", 2.2);
keyLight.position.set(5, 12, 10);
scene.add(keyLight);
const worldGroup = new THREE.Group();
worldGroup.add(new THREE.AxesHelper(5));
const grid = new THREE.GridHelper(24, 12, 0x46766b, 0x35504e);
grid.material.transparent = true;
grid.material.opacity = 0.28;
worldGroup.add(grid);
const colliderNormalMaterial = new THREE.MeshNormalMaterial({ side: THREE.DoubleSide, flatShading: true });

const camera = new THREE.PerspectiveCamera(55, 1, 0.01, 1000);
const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false });
renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
renderer.outputColorSpace = THREE.SRGBColorSpace;
ui.viewport.prepend(renderer.domElement);
// Match the Spark configuration used by the supplied Marble viewer.
// These legacy SPZ files use Spark's regular SplatMesh loading path.
const spark = new SparkRenderer({ renderer, enableLod: true });
scene.add(spark);
// Match Image-Blaster's scene hierarchy: the SPZ and collider share one group
// under SparkRenderer so both receive the same world transform.
spark.add(worldGroup);
const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.dampingFactor = 0.08;
controls.target.set(0, 0, 0);
const raycaster = new THREE.Raycaster();
const modelBox = new THREE.Box3();
let dragStart = null;
let imageShiftDragging = false;
let suppressImageClick = false;
const markerWorldPosition = new THREE.Vector3();
const cameraWorldPosition = new THREE.Vector3();

function setStatus(message, warning = false) {
  ui.status.textContent = message;
  ui.status.classList.toggle("warning", warning);
}

function currentLandmark() {
  return landmarks.find((item) => item.id === ui.picker.value) || null;
}

function currentRecord() {
  const landmark = currentLandmark();
  if (!landmark) return null;
  if (!records.has(landmark.id)) {
    records.set(landmark.id, {
      id: landmark.id,
      kind: landmark.kind || "landmark",
      pixel_xy: landmark.pixel_xy ? [...landmark.pixel_xy] : null,
      mesh_xyz_raw: null,
      source_status: landmark.source_status || "not_reviewed",
      pixel_status: landmark.pixel_xy ? "ESTIMATED_SEED_NEEDS_REVIEW" : "UNSET",
      pick_approval_status: "NO_3D_PICK",
      human_approved: false,
      annotator: "agent_proposal",
      note: landmark.note || "",
    });
  }
  return records.get(landmark.id);
}

function paintImage() {
  if (!image) return;
  ui.canvas.width = image.naturalWidth;
  ui.canvas.height = image.naturalHeight;
  imageContext.clearRect(0, 0, ui.canvas.width, ui.canvas.height);
  imageContext.drawImage(image, 0, 0);

  for (const landmark of landmarks) {
    const record = records.get(landmark.id);
    const point = record?.pixel_xy || landmark.pixel_xy;
    if (!point) continue;
    const active = landmark.id === ui.picker.value;
    const paired = Boolean(record?.mesh_xyz_raw);
    imageContext.beginPath();
    imageContext.lineWidth = active ? 5 : 3;
    imageContext.strokeStyle = active ? "#ffd166" : paired ? "#56e39f" : "#ef8a72";
    imageContext.fillStyle = "#111a19cc";
    imageContext.arc(point[0], point[1], active ? 17 : 11, 0, Math.PI * 2);
    imageContext.fill();
    imageContext.stroke();
    if (active) {
      imageContext.font = "bold 26px system-ui";
      imageContext.lineWidth = 5;
      imageContext.strokeStyle = "#111718";
      imageContext.strokeText(landmark.id, point[0] + 21, point[1] - 12);
      imageContext.fillStyle = "#ffffff";
      imageContext.fillText(landmark.id, point[0] + 21, point[1] - 12);
    }
  }
}

function imagePointFromEvent(event) {
  const bounds = ui.canvas.getBoundingClientRect();
  const x = Math.round((event.clientX - bounds.left) * image.naturalWidth / bounds.width);
  const y = Math.round((event.clientY - bounds.top) * image.naturalHeight / bounds.height);
  return [Math.max(0, Math.min(image.naturalWidth - 1, x)), Math.max(0, Math.min(image.naturalHeight - 1, y))];
}

function landmarkAtImageEvent(event) {
  const bounds = ui.canvas.getBoundingClientRect();
  const [x, y] = imagePointFromEvent(event);
  let nearest = null;
  let nearestDistance = Infinity;
  for (const landmark of landmarks) {
    const point = records.get(landmark.id)?.pixel_xy || landmark.pixel_xy;
    if (!point) continue;
    const dx = (x - point[0]) * bounds.width / image.naturalWidth;
    const dy = (y - point[1]) * bounds.height / image.naturalHeight;
    const distance = Math.hypot(dx, dy);
    if (distance < nearestDistance) {
      nearestDistance = distance;
      nearest = landmark;
    }
  }
  return nearestDistance <= 14 ? nearest : null;
}

function moveSelectedImageLandmark(event) {
  const record = currentRecord();
  if (!record || !image) return;
  record.pixel_xy = imagePointFromEvent(event);
  record.pixel_status = "OPERATOR_PICKED_NEEDS_CROSS_MODAL_REVIEW";
  record.human_approved = false;
  paintImage();
  updateReviewState();
}

function renderPicker() {
  const previous = ui.picker.value;
  ui.picker.replaceChildren();
  for (const landmark of landmarks) {
    const option = document.createElement("option");
    option.value = landmark.id;
    option.textContent = `${landmark.id} — ${landmark.kind || "landmark"}`;
    ui.picker.append(option);
  }
  if (landmarks.some((item) => item.id === previous)) ui.picker.value = previous;
  paintImage();
  updateReviewState();
}

function updateMarker(id) {
  const old = markers.get(id);
  if (old) {
    worldGroup.remove(old);
    old.geometry.dispose();
    old.material.dispose();
    markers.delete(id);
  }
  const record = records.get(id);
  if (!record?.mesh_xyz_raw) return;
  const selected = id === ui.picker.value;
  const marker = new THREE.Mesh(
    new THREE.SphereGeometry(1, 12, 10),
    new THREE.MeshBasicMaterial({ color: selected ? "#ffd166" : record.human_approved ? "#56e39f" : "#f78c73" }),
  );
  marker.position.fromArray(record.mesh_xyz_raw);
  // Keep the marker legible without letting nearby picks cover the scene.
  marker.userData.radius_pixels = selected ? 6 : 4;
  marker.userData.landmarkId = id;
  worldGroup.add(marker);
  markers.set(id, marker);
}

function updateMarkerScreenSizes() {
  const pixelHeight = renderer.domElement.clientHeight;
  if (pixelHeight <= 0 || markers.size === 0) return;
  camera.getWorldPosition(cameraWorldPosition);
  const worldUnitsPerPixelAtUnitDepth = 2 * Math.tan(THREE.MathUtils.degToRad(camera.getEffectiveFOV()) / 2) / pixelHeight;
  for (const marker of markers.values()) {
    marker.getWorldPosition(markerWorldPosition);
    const distance = cameraWorldPosition.distanceTo(markerWorldPosition);
    const radius = marker.userData.radius_pixels * distance * worldUnitsPerPixelAtUnitDepth;
    marker.scale.setScalar(radius);
  }
}

function updateReviewState() {
  const record = currentRecord();
  if (!record) {
    ui.selected.textContent = "尚無地標。新增地標，或匯入標註 JSON。";
    return;
  }
  const pixelText = record.pixel_xy ? record.pixel_xy.join(", ") : "未點選";
  const xyzText = record.mesh_xyz_raw ? record.mesh_xyz_raw.map((n) => Number(n).toFixed(3)).join(", ") : "未選擇";
  const depthText = Number.isFinite(record.camera_optical_depth_raw_units)
    ? `　視線深度 ${record.camera_optical_depth_raw_units.toFixed(3)} raw units`
    : "";
  ui.selected.textContent = `${record.id}　像素 (${pixelText})　raw XYZ (${xyzText})${depthText}　${record.human_approved ? "人工核對" : "待審"}`;
  ui.note.value = record.note || "";
  ui.annotator.value = record.annotator || "agent_proposal";
  ui.reviewed.checked = Boolean(record.human_approved);
  ui.summary.innerHTML = `<b>${Array.from(records.values()).filter((row) => row.mesh_xyz_raw).length}</b> 個 raw GLB 點候選；<b>${Array.from(records.values()).filter((row) => row.human_approved).length}</b> 個已人工核對。座標未校準為公尺。`;
  for (const id of Array.from(markers.keys())) updateMarker(id);
}

function loadImage(source, name = "local image") {
  const url = source instanceof File ? URL.createObjectURL(source) : source;
  const next = new Image();
  next.onload = () => {
    image = next;
    currentImageName = name;
    ui.imageName.textContent = `${name} · ${image.naturalWidth} × ${image.naturalHeight}`;
    paintImage();
    setStatus(`圖片載入完成：${image.naturalWidth} × ${image.naturalHeight}`);
    if (source instanceof File) URL.revokeObjectURL(url);
  };
  next.onerror = () => {
    if (source instanceof File) URL.revokeObjectURL(url);
    setStatus(`圖片載入失敗：${name}`, true);
  };
  next.src = url;
}

function lookFrom(axis) {
  worldGroup.updateMatrixWorld(true);
  const direction = axis === "TOP" ? new THREE.Vector3(0, -1, 0) : {
    X: new THREE.Vector3(1, 0, 0),
    Y: new THREE.Vector3(0, 1, 0),
    Z: new THREE.Vector3(0, 0, 1),
  }[axis];
  const up = (axis === "Z" ? new THREE.Vector3(0, 1, 0) : new THREE.Vector3(0, 0, 1))
    .transformDirection(worldGroup.matrixWorld);
  direction.transformDirection(worldGroup.matrixWorld);
  if (glbRoot && !modelBox.isEmpty()) {
    const worldBox = modelBox.clone().applyMatrix4(worldGroup.matrixWorld);
    const center = worldBox.getCenter(new THREE.Vector3());
    const size = Math.max(worldBox.getSize(new THREE.Vector3()).length(), 0.1);
    camera.position.copy(center).addScaledVector(direction, size * 0.78);
    controls.target.copy(center);
    camera.near = Math.max(size / 10000, 0.001);
    camera.far = size * 20;
  } else {
    camera.position.copy(direction).multiplyScalar(25);
    controls.target.set(0, 0, 0);
  }
  camera.up.copy(up);
  controls.update();
  camera.updateProjectionMatrix();
}

function lookHome() {
  // The handoff pose is expressed in raw GLB coordinates. Transform its point
  // and target through the shared SPZ/GLB parent before positioning the camera;
  // otherwise the camera and flipped world occupy opposite hemispheres.
  worldGroup.updateMatrixWorld(true);
  controls.target.copy(worldGroup.localToWorld(new THREE.Vector3(-0.4, 5.7, 1.1)));
  camera.position.copy(worldGroup.localToWorld(new THREE.Vector3(2.5, 19.4, 20.5)));
  camera.fov = 55;
  camera.up.set(0, 1, 0);
  controls.update();
  camera.near = 0.025;
  camera.far = 800;
  camera.updateProjectionMatrix();
}

function lookWorldLabsStart() {
  // The provided World Labs Splat Explorer starts at the world origin, looking
  // down -Z with a 70-degree vertical FOV. Its default OpenCV-space SPZ is
  // rotated by pi around X; worldGroup applies the same flip to GLB and SPZ.
  camera.position.set(0, 0, 0);
  controls.target.set(0, 0, -1);
  camera.up.set(0, 1, 0);
  camera.fov = 70;
  camera.near = 0.01;
  camera.far = 1000;
  controls.update();
  camera.updateProjectionMatrix();
}

function captureCameraRawPose() {
  worldGroup.updateMatrixWorld(true);
  const inverse = worldGroup.matrixWorld.clone().invert();
  const position = camera.getWorldPosition(new THREE.Vector3());
  const forward = camera.getWorldDirection(new THREE.Vector3());
  position.applyMatrix4(inverse);
  forward.transformDirection(inverse);
  return {
    position_raw_xyz: position.toArray().map((value) => Number(value.toFixed(6))),
    forward_raw_xyz: forward.toArray().map((value) => Number(value.toFixed(6))),
    vertical_fov_degrees: camera.fov,
    aspect_ratio: camera.aspect,
    viewport_px: [renderer.domElement.width, renderer.domElement.height],
  };
}

function applyWorldTransform() {
  worldGroup.rotation.set(flipY ? Math.PI : 0, 0, 0);
  worldGroup.updateMatrixWorld(true);
}

function loadGlb(source, name = "local collider.glb") {
  const url = source instanceof File ? URL.createObjectURL(source) : source;
  const loader = new GLTFLoader();
  loader.load(url, (gltf) => {
    if (glbRoot) worldGroup.remove(glbRoot);
    glbRoot = gltf.scene;
    glbRoot.updateMatrixWorld(true);
    modelBox.setFromObject(glbRoot);
    colliderOriginalMaterials = new WeakMap();
    glbRoot.traverse((object) => {
      if (!object.isMesh) return;
      colliderOriginalMaterials.set(object, object.material);
      object.material = colliderUseNormalMaterial ? colliderNormalMaterial : object.material;
    });
    worldGroup.add(glbRoot);
    applyWorldTransform();
    currentGlbName = name;
    ui.modelName.textContent = `${currentSpzName} + ${name}`;
    lookWorldLabsStart();
    setStatus(`Collider 載入完成；${name}；原始單位未校準`);
    if (source instanceof File) URL.revokeObjectURL(url);
    for (const id of markers.keys()) updateMarker(id);
  }, undefined, (error) => {
    if (source instanceof File) URL.revokeObjectURL(url);
    setStatus(`GLB 載入失敗：${error.message || name}`, true);
  });
}

async function loadSpz(source, name = "local splat.spz") {
  const url = source instanceof File ? URL.createObjectURL(source) : source;
  setStatus(`正在解碼 Gaussian Splat：${name}…`);
  try {
    const next = new SplatMesh({ url });
    // Attach before the async decode completes, matching Spark's streaming
    // examples so its renderer can register the mesh during initialization.
    worldGroup.add(next);
    await next.initialized;
    if (splatRoot) {
      worldGroup.remove(splatRoot);
      splatRoot.dispose?.();
    }
    splatRoot = next;
    splatRoot.visible = showSplat;
    applyWorldTransform();
    currentSpzName = name;
    ui.modelName.textContent = `${name} + ${currentGlbName}`;
    setStatus(`SPZ 載入完成：${name}；採 raw 座標顯示，外圍 splat 不作為地圖邊界`);
  } catch (error) {
    setStatus(`SPZ 載入失敗：${error.message || name}`, true);
  } finally {
    if (source instanceof File) URL.revokeObjectURL(url);
  }
}

function loadPresetSplat(quality) {
  const suffix = quality === "full-res" ? "full-res" : quality;
  const fileName = quality.startsWith("core-") ? `canyon-waterfall-${quality}.spz` : `canyon-waterfall-${suffix}.spz`;
  currentSpzName = fileName;
  const url = new URL(quality.startsWith("core-") ? `./diagnostics/${fileName}` : `${DEFAULT_ROOT}${fileName}`, document.baseURI).href;
  void loadSpz(url, fileName);
}

function resize() {
  const width = Math.max(1, ui.viewport.clientWidth);
  const height = Math.max(1, ui.viewport.clientHeight);
  renderer.setSize(width, height, false);
  camera.aspect = width / height;
  camera.updateProjectionMatrix();
}
new ResizeObserver(resize).observe(ui.viewport);
resize();

function addLandmark(landmark, isSeed = false) {
  if (!landmark?.id || landmarks.some((item) => item.id === landmark.id)) return false;
  landmarks.push(landmark);
  seedPixels.set(landmark.id, isSeed && landmark.pixel_xy ? [...landmark.pixel_xy] : null);
  records.set(landmark.id, {
    id: landmark.id,
    kind: landmark.kind || "landmark",
    pixel_xy: landmark.pixel_xy ? [...landmark.pixel_xy] : null,
    mesh_xyz_raw: landmark.mesh_xyz_raw ? [...landmark.mesh_xyz_raw] : null,
    source_status: landmark.source_status || "not_reviewed",
    pixel_status: landmark.pixel_xy ? "ESTIMATED_SEED_NEEDS_REVIEW" : "UNSET",
    pick_approval_status: landmark.mesh_xyz_raw ? "RAW_RAY_HIT_NEEDS_REVIEW" : "NO_3D_PICK",
    human_approved: Boolean(landmark.human_approved),
    annotator: landmark.annotator || "agent_proposal",
    note: landmark.note || "",
    ...(landmark.face_index === undefined ? {} : { face_index: landmark.face_index }),
  });
  return true;
}

function importAnnotations(data) {
  const entries = data.pairs || data.landmarks || [];
  let count = 0;
  for (const entry of entries) {
    if (!entry.id) continue;
    const known = landmarks.find((item) => item.id === entry.id);
    const merged = { ...(known || {}), ...entry, kind: entry.kind || known?.kind || "landmark" };
    if (known) {
      const record = { ...(records.get(entry.id) || {}), ...merged };
      for (const key of ["pixel_xy", "mesh_xyz_raw"]) record[key] = entry[key] ?? record[key] ?? known[key] ?? null;
      for (const key of ["camera_optical_depth_raw_units", "camera_ray_depth_raw_units", "camera_raw_pose"]) {
        if (entry[key] !== undefined) record[key] = entry[key];
      }
      record.human_approved = Boolean(entry.human_approved);
      record.pick_approval_status = entry.pick_approval_status || (record.mesh_xyz_raw ? "RAW_RAY_HIT_NEEDS_REVIEW" : "NO_3D_PICK");
      record.annotator = entry.annotator || "agent_proposal";
      record.note = entry.note || known.note || "";
      records.set(entry.id, record);
      if (entry.pixel_xy) known.pixel_xy = [...entry.pixel_xy];
    } else if (addLandmark(merged)) {
      count += 1;
    }
    updateMarker(entry.id);
  }
  renderPicker();
  setStatus(`匯入完成；處理 ${entries.length} 筆，新增 ${count} 個地標`);
}

async function importJsonFile(file) {
  try {
    importAnnotations(JSON.parse(await file.text()));
  } catch (error) {
    setStatus(`標註 JSON 載入失敗：${error.message}`, true);
  }
}

function fileKind(file) {
  const name = file.name.toLowerCase();
  if (file.type.startsWith("image/") || /\.(png|jpe?g|webp|gif|avif)$/.test(name)) return "image";
  if (name.endsWith(".glb")) return "glb";
  if (name.endsWith(".spz")) return "spz";
  if (name.endsWith(".json")) return "json";
  return "unknown";
}

function handleDrop(event, zone) {
  event.preventDefault();
  zone.classList.remove("drop-active");
  const files = Array.from(event.dataTransfer?.files || []);
  if (!files.length) return;
  for (const file of files) {
    const kind = fileKind(file);
    if (kind === "image" && zone === ui.imagePane) loadImage(file, file.name);
    else if (kind === "spz" && zone === ui.modelPane) void loadSpz(file, file.name);
    else if (kind === "glb" && zone === ui.modelPane) loadGlb(file, file.name);
    else if (kind === "json" && zone === ui.modelPane) void importJsonFile(file);
    else setStatus(`此窗格不接受 ${file.name}；放到另一個窗格，或使用上方載入按鈕`, true);
  }
}

for (const [zone, hint] of [[ui.imagePane, ui.imageDropHint], [ui.modelPane, ui.modelDropHint]]) {
  zone.addEventListener("dragenter", (event) => {
    event.preventDefault();
    zone.classList.add("drop-active");
    hint.hidden = false;
  });
  zone.addEventListener("dragover", (event) => event.preventDefault());
  zone.addEventListener("dragleave", (event) => {
    if (!zone.contains(event.relatedTarget)) {
      zone.classList.remove("drop-active");
      hint.hidden = true;
    }
  });
  zone.addEventListener("drop", (event) => {
    hint.hidden = true;
    handleDrop(event, zone);
  });
}

document.querySelectorAll("[data-open]").forEach((button) => {
  button.addEventListener("click", () => document.getElementById(button.dataset.open).click());
});
ui.imageInput.addEventListener("change", (event) => {
  const file = event.target.files?.[0];
  if (file) loadImage(file, file.name);
  event.target.value = "";
});
ui.spzInput.addEventListener("change", (event) => {
  const file = event.target.files?.[0];
  if (file) void loadSpz(file, file.name);
  event.target.value = "";
});
ui.splatPreset.addEventListener("change", () => loadPresetSplat(ui.splatPreset.value));
ui.glbInput.addEventListener("change", (event) => {
  const file = event.target.files?.[0];
  if (file) loadGlb(file, file.name);
  event.target.value = "";
});
document.querySelector("#importJson").addEventListener("click", () => ui.jsonInput.click());
ui.jsonInput.addEventListener("change", (event) => {
  const file = event.target.files?.[0];
  if (file) void importJsonFile(file);
  event.target.value = "";
});

ui.canvas.addEventListener("pointerdown", (event) => {
  if (!event.shiftKey || !image) return;
  imageShiftDragging = true;
  suppressImageClick = true;
  ui.canvas.setPointerCapture(event.pointerId);
  moveSelectedImageLandmark(event);
});
ui.canvas.addEventListener("pointermove", (event) => {
  if (imageShiftDragging && event.shiftKey && (event.buttons & 1)) moveSelectedImageLandmark(event);
});
ui.canvas.addEventListener("pointerup", (event) => {
  if (!imageShiftDragging) return;
  if (event.shiftKey) moveSelectedImageLandmark(event);
  imageShiftDragging = false;
  const record = currentRecord();
  if (record) setStatus(`已移動 ${record.id} 的原圖標註點；配對仍待核對`);
});
ui.canvas.addEventListener("pointercancel", () => {
  imageShiftDragging = false;
  suppressImageClick = false;
});
ui.canvas.addEventListener("click", (event) => {
  if (!image || suppressImageClick) {
    suppressImageClick = false;
    return;
  }
  if (event.shiftKey) {
    moveSelectedImageLandmark(event);
    const record = currentRecord();
    if (record) setStatus(`已移動 ${record.id} 的原圖標註點；配對仍待核對`);
    return;
  }
  const landmark = landmarkAtImageEvent(event);
  if (landmark) {
    ui.picker.value = landmark.id;
    paintImage();
    updateReviewState();
    setStatus(`已選取 ${landmark.id}；按住 Shift 點擊或拖曳可移動`);
  } else {
    setStatus("點擊既有標註點可選取；按住 Shift 後點擊或拖曳可移動目前選中的點");
  }
});

renderer.domElement.addEventListener("pointerdown", (event) => { dragStart = [event.clientX, event.clientY]; });
renderer.domElement.addEventListener("pointerup", (event) => {
  if (!glbRoot || !dragStart || Math.hypot(event.clientX - dragStart[0], event.clientY - dragStart[1]) > 4) return;
  const bounds = renderer.domElement.getBoundingClientRect();
  const ndc = new THREE.Vector2(2 * (event.clientX - bounds.left) / bounds.width - 1, 1 - 2 * (event.clientY - bounds.top) / bounds.height);
  raycaster.setFromCamera(ndc, camera);
  worldGroup.updateMatrixWorld(true);
  const hits = raycaster.intersectObject(glbRoot, true);
  if (!hits.length) {
    setStatus("射線沒有擊中 collider；旋轉場景或選另一個位置", true);
    return;
  }
  const record = currentRecord();
  if (!record) return;
  const hit = hits[0];
  record.mesh_xyz_raw = worldGroup.worldToLocal(hit.point.clone()).toArray().map((value) => Number(value.toFixed(6)));
  const cameraSpaceHit = camera.worldToLocal(hit.point.clone());
  record.camera_ray_depth_raw_units = Number(hit.distance.toFixed(6));
  record.camera_optical_depth_raw_units = Number((-cameraSpaceHit.z).toFixed(6));
  record.camera_raw_pose = captureCameraRawPose();
  record.face_index = hit.faceIndex;
  record.mesh_name = hit.object.name || "";
  record.mesh_uuid = hit.object.uuid;
  record.pick_approval_status = "RAW_RAY_HIT_NEEDS_CROSS_MODAL_REVIEW";
  record.human_approved = false;
  record.annotator = ui.annotator.value;
  updateMarker(record.id);
  updateReviewState();
  setStatus(`已記錄 ${record.id}：raw XYZ、視線深度 ${record.camera_optical_depth_raw_units.toFixed(3)}；表面語義仍待審`);
});

ui.picker.addEventListener("change", () => {
  paintImage();
  updateReviewState();
});
document.querySelector("#viewX").addEventListener("click", () => lookFrom("X"));
document.querySelector("#viewY").addEventListener("click", () => lookFrom("Y"));
document.querySelector("#viewZ").addEventListener("click", () => lookFrom("Z"));
document.querySelector("#viewTop").addEventListener("click", () => lookFrom("TOP"));
document.querySelector("#viewHome").addEventListener("click", lookHome);
document.querySelector("#viewWorldLabsStart").addEventListener("click", lookWorldLabsStart);
document.querySelector("#flipY").addEventListener("click", (event) => {
  flipY = !flipY;
  applyWorldTransform();
  event.currentTarget.textContent = `flipY: ${flipY ? "ON" : "OFF"}`;
  lookFrom("TOP");
  setStatus(`SPZ 與 collider 共用 flip_y=${flipY}；比例仍是未校準 raw units`);
});
document.querySelector("#toggleSplat").addEventListener("click", (event) => {
  if (!splatRoot) return setStatus("尚未載入 SPZ", true);
  showSplat = !showSplat;
  splatRoot.visible = showSplat;
  event.currentTarget.textContent = showSplat ? "隱藏 SPZ" : "顯示 SPZ";
});
document.querySelector("#toggleCollider").addEventListener("click", (event) => {
  if (!glbRoot) return setStatus("尚未載入 GLB", true);
  glbRoot.visible = !glbRoot.visible;
  event.currentTarget.textContent = glbRoot.visible ? "隱藏 GLB" : "顯示 GLB";
});
document.querySelector("#toggleMaterial").addEventListener("click", (event) => {
  if (!glbRoot) return setStatus("尚未載入 GLB", true);
  colliderUseNormalMaterial = !colliderUseNormalMaterial;
  glbRoot.traverse((object) => {
    if (object.isMesh) object.material = colliderUseNormalMaterial ? colliderNormalMaterial : colliderOriginalMaterials.get(object);
  });
  event.currentTarget.textContent = colliderUseNormalMaterial ? "Collider 法線色" : "Collider 原始材質";
});
document.querySelector("#addLandmark").addEventListener("click", () => {
  const id = document.querySelector("#newLandmarkId").value.trim().toLowerCase().replace(/[^a-z0-9_-]+/g, "-").replace(/^-|-$/g, "");
  const kind = document.querySelector("#newLandmarkKind").value.trim() || "landmark";
  if (!id) return setStatus("請先輸入地標 ID", true);
  if (!addLandmark({ id, kind, source_status: "not_reviewed", note: "" })) return setStatus(`地標 ID 已存在：${id}`, true);
  renderPicker();
  ui.picker.value = id;
  document.querySelector("#newLandmarkId").value = "";
  document.querySelector("#newLandmarkKind").value = "";
  updateReviewState();
  setStatus(`新增地標 ${id}；依序點選原圖像素和 GLB 表面`);
});
document.querySelector("#clearAnchor").addEventListener("click", () => {
  const record = currentRecord();
  if (!record) return;
  record.mesh_xyz_raw = null;
  record.face_index = null;
  record.camera_ray_depth_raw_units = null;
  record.camera_optical_depth_raw_units = null;
  record.camera_raw_pose = null;
  record.pick_approval_status = "NO_3D_PICK";
  record.human_approved = false;
  updateMarker(record.id);
  paintImage();
  updateReviewState();
  setStatus(`已清除 ${record.id} 的 raw 3D 點`);
});
document.querySelector("#clearAllAnnotations").addEventListener("click", () => {
  if (!window.confirm("清除全部手動像素點、3D 點、備註與核對狀態？會保留地標 ID／類型，並恢復原始像素種子。")) return;
  for (const landmark of landmarks) {
    const seedPixel = seedPixels.get(landmark.id) || null;
    landmark.pixel_xy = seedPixel ? [...seedPixel] : null;
    records.set(landmark.id, {
      id: landmark.id,
      kind: landmark.kind || "landmark",
      pixel_xy: seedPixel ? [...seedPixel] : null,
      mesh_xyz_raw: null,
      source_status: landmark.source_status || "not_reviewed",
      pixel_status: seedPixel ? "ESTIMATED_SEED_NEEDS_REVIEW" : "UNSET",
      pick_approval_status: "NO_3D_PICK",
      human_approved: false,
      annotator: "agent_proposal",
      note: "",
    });
  }
  for (const [id, marker] of markers) {
    worldGroup.remove(marker);
    marker.geometry.dispose();
    marker.material.dispose();
    markers.delete(id);
  }
  if (landmarks.length) ui.picker.value = landmarks[0].id;
  paintImage();
  updateReviewState();
  setStatus(`已清空全部標註；保留 ${landmarks.length} 個地標及原始像素種子`);
});
ui.note.addEventListener("input", () => { const record = currentRecord(); if (record) record.note = ui.note.value; });
ui.annotator.addEventListener("change", () => { const record = currentRecord(); if (record) record.annotator = ui.annotator.value; });
ui.reviewed.addEventListener("change", () => {
  const record = currentRecord();
  if (!record) return;
  record.human_approved = ui.reviewed.checked && Boolean(record.pixel_xy && record.mesh_xyz_raw);
  if (ui.reviewed.checked && !record.human_approved) setStatus("需先有 2D 像素與 3D 點，才能標記人工核對", true);
  updateMarker(record.id);
  updateReviewState();
});

function exportData() {
  const displayMatrix = new THREE.Matrix4().makeRotationX(flipY ? Math.PI : 0);
  return {
    schema_version: 1,
    status: "CANDIDATE_NEEDS_OPERATOR_REVIEW",
    source_image: currentImageName,
    collider: currentGlbName,
    gaussian_splat: currentSpzName,
    coordinate_system: "RAW_GLTF_XYZ_UNSCALED",
    renderer_transform: {
      flip_y: flipY,
      shared_for: ["gaussian_splat", "collider"],
      raw_to_display_matrix_4x4_column_major: displayMatrix.toArray(),
      scale: 1,
      ground_plane_offset_raw: 0,
      note: "Image-Blaster display default only; does not establish physical up-axis or metric scale.",
    },
    world_id: "44c246a5-3f15-4cb3-b835-830b04857da8",
    scale_m_per_raw_unit: null,
    up_axis: null,
    annotation_note: "Raw collider ray hits are not semantic labels. Pixel seeds are approximate until reviewed. Export does not approve camera, axes, scale, terrain, or topology.",
    pairs: landmarks.map((landmark) => {
      const record = records.get(landmark.id) || {};
      return {
        id: landmark.id,
        kind: record.kind || landmark.kind || "landmark",
        pixel_xy: record.pixel_xy || null,
        mesh_xyz_raw: record.mesh_xyz_raw || null,
        camera_ray_depth_raw_units: record.camera_ray_depth_raw_units ?? null,
        camera_optical_depth_raw_units: record.camera_optical_depth_raw_units ?? null,
        camera_raw_pose: record.camera_raw_pose || null,
        face_index: record.face_index ?? null,
        mesh_name: record.mesh_name || null,
        mesh_uuid: record.mesh_uuid || null,
        source_status: record.source_status || landmark.source_status || "not_reviewed",
        pixel_status: record.pixel_status || (record.pixel_xy ? "NEEDS_REVIEW" : "UNSET"),
        pick_approval_status: record.pick_approval_status || "NO_3D_PICK",
        human_approved: Boolean(record.human_approved),
        annotator: record.annotator || "agent_proposal",
        note: record.note || "",
      };
    }),
  };
}

document.querySelector("#exportJson").addEventListener("click", async () => {
  const contents = JSON.stringify(exportData(), null, 2);
  try {
    if (window.showSaveFilePicker) {
      const handle = await window.showSaveFilePicker({
        suggestedName: "paired_landmarks.json",
        types: [{ description: "JSON", accept: { "application/json": [".json"] } }],
      });
      const writable = await handle.createWritable();
      await writable.write(contents);
      await writable.close();
    } else {
      const url = URL.createObjectURL(new Blob([contents], { type: "application/json" }));
      const link = document.createElement("a");
      link.href = url;
      link.download = "paired_landmarks.json";
      link.click();
      setTimeout(() => URL.revokeObjectURL(url), 1000);
    }
    setStatus("paired_landmarks.json 已匯出；未人工核對的項目仍標為候選");
  } catch (error) {
    if (error.name !== "AbortError") setStatus(`匯出失敗：${error.message}`, true);
  }
});

document.querySelector("#copyReview").addEventListener("click", async () => {
  const data = exportData();
  const selected = data.pairs.find((pair) => pair.id === ui.picker.value);
  const prompt = [
    "請審閱這個 Marble 1.1 世界的候選 2D↔3D 地標配對。",
    "原圖與 raw GLB 座標只作證據；不要猜測 metric scale、up-axis 或表面語義。",
    "若模型表面不是明確對應，保留未核對狀態並寫明不一致。",
    JSON.stringify(selected, null, 2),
  ].join("\n\n");
  try {
    await navigator.clipboard.writeText(prompt);
    setStatus("目前地標審閱摘要已複製；可貼回 Codex 對話請 agent 檢查");
  } catch {
    setStatus("剪貼簿無法使用；請直接匯出 JSON", true);
  }
});

async function init() {
  try {
    const response = await fetch("./landmarks.json");
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const seed = await response.json();
    for (const landmark of seed.landmarks || []) addLandmark(landmark, true);
    renderPicker();
    setStatus(`載入 ${landmarks.length} 個圖片地標種子；位置為近似值，尚無已核准 3D 對應`);
  } catch (error) {
    setStatus(`地標種子載入失敗：${error.message}；仍可手動新增`, true);
  }
  loadImage(new URL(DEFAULT_IMAGE, document.baseURI).href, "canyon-waterfall-reference.jpeg");
  loadGlb(new URL(DEFAULT_GLB, document.baseURI).href, "canyon-waterfall-collider.glb");
  ui.splatPreset.value = "100k";
  void loadSpz(new URL(DEFAULT_SPZ, document.baseURI).href, "canyon-waterfall-100k.spz");
}

function animate() {
  requestAnimationFrame(animate);
  controls.update();
  updateMarkerScreenSizes();
  renderer.render(scene, camera);
}
animate();
void init();
