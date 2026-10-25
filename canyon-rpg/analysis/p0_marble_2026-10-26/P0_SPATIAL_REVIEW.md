# Marble 1.1 世界模型：P0 空間審核（2026-10-26）

## 判定

**P0-A 已有經使用者核對的 25 組像素／GLB 點與可重現的原圖相機候選。P0-B 正式 Godot 藍圖仍為 `BLOCKED`。** 目前成果是幾何量測與候選拓樸，不是可遊走關卡。沒有重新生成 Marble 世界，也沒有使用舊 P0 藍圖或 Hunyuan 物件。

輸入為原始 2752×1536 參考圖、現有 Marble 1.1 GLB/SPZ、`paired_landmarks.json`。原始標註檔 SHA-256 `692736c4b36510974865c2ceaba2bbd2fe9168ea1cb1565cc7cb2e68c6b26224`，留在 `annotations/paired_landmarks_raw.json`，未修改任何座標。使用者在對話中確認「全部核對過」，因此另建 `annotations/paired_landmarks_user_reviewed.json` 記錄 25 筆完整配對的人工核對來源；`exit_lower_left` 和 `right_red_tree` 沒有 3D 點，仍為未配對。此確認只涵蓋標註點，不代表曲面語義、相機、尺度或通行已核准。

## 視覺對照

- [原圖地標與 collider 俯視對照](visual_evidence_reference_vs_collider.png)：右圖只顯示 GLB 面中心與候選水流／導航線，不是經驗證的俯視地圖。GLB 顏色供辨識，不足以自動分類地面。
- [原圖相機重投影](registration/camera_reprojection_review.jpg)：25 點，RANSAC 23 點納入，中位誤差 19.3 px，90 分位 35.6 px；相機水平 FOV 候選 76°，無鏡頭畸變假設。`stream_lower` 66.8 px、`stair_left_upper` 61.4 px 是最大離群點。來源相機只用於核對模型與圖片，不是 Godot 的 45° 正交遊戲相機。
- [水流相對高度剖面](visual_evidence_water_profile.png)：高度定義為 `-raw Y`，單位仍是模型單位。
- [路線內部曲面取樣](visual_evidence_route_surface_survey.png)：每段直線連接線採 21 個 XZ 位置，尋找接近兩端插值高度且朝上的 GLB 面。黑色接近插值高度，亮色差距較大；這不是可遊走測試。

## 座標與高度

GLB 的原始 **−Y 為相對向上**：6/6 已量測的候選水流線段沿下游降低；21,641 個 GLB 面法線的 −Y 分量 >0.75，+Y 對照為 2,326。顯示器共用的 X 軸 180° 旋轉將 raw −Y 映至畫面 +Y。此證據可支持相對朝向，不能決定公尺比例。建議把橋中央原始座標 `(0.134183, 0.876082, 1.706814)` 當本地原點；尺度確定後，候選 Godot 轉換為 `s × (x−x0, −(y−y0), −(z−z0))`。SPZ 和 GLB 必須使用同一轉換。

| 水段端點 | 起點高於終點（raw unit） | 判讀 |
|---|---:|---|
| 遠瀑布 → 中瀑布 | 0.201 | 端點符合下落 |
| 中瀑布 → 上游河道 | 0.302 | 端點符合下落 |
| 上游河道 → 主瀑布 | 0.204 | 端點符合下落；上游點落在偏綠 GLB 面 |
| 主瀑布 → 主水潭 | 0.122 | 端點符合下落 |
| 主水潭 → 橋下水道 | 0.016 | 端點符合下落，但差值很小 |
| 橋下水道 → 下游 | 0.032 | 端點符合下落；下游點落在偏綠 GLB 面 |
| 下游 → 左下出口 | 未量測 | 出口沒有 3D 點 |

橋左右端點水平間距為 **0.216502 raw unit**。`metric_design_hypothesis.json` 示範若設計者指定橋跨度 3.0 m，則 `s=13.8567 m/raw unit`；這是**未核准的玩法設計假設**，不是從 Marble 或照片量出的真實公尺。`reports/topology_3m_bridge_hypothesis.json` 只供距離比較，不可用於正式高度圖或物理門檻。

## 幾何與拓樸審核

來源相機投出的 27 條射線全與 GLB 相交；這只證明有幾何命中。每個已配對點的射線第一命中與人工點有偏移（詳見 `registered_spatial_measurements.json`），且不能從命中推知水面或地面。GLB 面法線／顏色初篩需複查的 5 點：`upper_run`、`stream_lower`（水點落在偏綠面），`left_bank_upper`（路點落在斜面），`stair_left_upper`、`stair_far_right`（階梯點落在陡面）。這些是警示，不是自動重分類。

導航提案的 12 段都有 3D 端點，其中 `stair_far_right → right_upper` 端點高差約對應 23.1°；其他坡角見 `registered_spatial_measurements.json`。尚未對每段中間曲面做語義分割、角色尺寸碰撞、階高、橋面寬度或連續通路測試。進一步做 21 點／段的投影三角面取樣：橋及鄰近下層路線與端點插值高度接近；`stair_left_upper → left_upper` 只有 16/21 點在 0.08 raw unit 內，`stair_far_right → right_upper` 為 14/21 且 t=0.6 沒有候選面；`right_lower → stair_far_right` 以更嚴的 0.02 raw unit 門檻只有 11/21。這些斷層可能來自樓梯曲線、遮擋或幾何缺口，不能據此單獨判死，但主路與右支線都不能標為連續可走。逐點資料見 `route_surface_survey.json`。周圍背景殼體、樹冠、岩壁、水面與地面仍需分離，不能把全部 GLB 面直接烘成遊戲高度圖。候選 16-bit 圖和有效性遮罩留在 `blueprint/candidates/`，只用作診斷。

## 驗證結果與限制

- 工作包資料稽核成功：GLB 76,454 頂點／146,266 面；4 個 SPZ LOD 點數為 98,304／150,000／500,000／1,920,000；輸入 hash 檢查通過。
- 工作包 16/16 單元與故障注入測試通過；`node --check` 檢視器腳本語法通過。直接執行該 `.mjs` 缺 `three` 套件，因此不是瀏覽器互動驗收。使用者已在目前標註工具完成實際標註，這份報告只根據其匯出資料。
- 原工作包 `validate_p0.py` 對**新**的 25 筆 3D 草案得 35 PASS／1 FAIL，失敗項 `no_fabricated_3d` 硬編碼草案必須全為空，並把「沒有已核對配對」寫死在階段文字；不能拿這個失敗當成座標造假證據，也不能拿其階段文字當成當前狀態。新建 `post_annotation_validation.json`：11 PASS／0 FAIL，僅驗證標註、配準、端點量測與不虛報正式成果。
- 更新軸向與水流證據後，原工作包正式升級 Gate 仍為 **BLOCKED：10 個條件未滿**，詳見 `reports/promotion_gate.json`。主要剩餘：公尺比例、相機候選人工視覺核准、地表與背景／樹／水／橋／階梯／懸崖分割、連續主路物理驗證。`ready_for_p0b` 保持 false。
- `register_camera.py` 對完整匯出檔中 `mesh_xyz_raw:null` 的兩筆直接做 `len(None)`，所以給該腳本的 `annotations/paired_landmarks_registration.json` 明確排除了這兩筆；沒有改原始標註。

**下一道實際 Gate**：先在 SPZ/GLB 同步檢視器中複核兩個高殘差點，設定設計尺度（例如確認橋跨度），對中心場景建立面級語義遮罩，再沿每條路線以選定角色尺寸檢查連續碰撞及階高。只有這些通過後才建立正式 `scene_blueprint.json`、公尺高度圖及 Godot 導航；目前均未輸出。
