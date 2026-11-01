"""Reusable Blender helper for scoped, idempotent P1 geometry replacement.

Import from a Blender generator; it does not modify any scene on import.
No global object purge, no camera edits, no update of linked library assets.
"""


def find_by_art_id(scene, art_id):
    hits = [obj for obj in scene.objects if obj.get("art_id") == art_id]
    if len(hits) > 1:
        raise ValueError("Duplicate art_id in scene: " + art_id)
    return hits[0] if hits else None


def ensure_collection(scene, name):
    import bpy
    found = bpy.data.collections.get(name)
    if found is None:
        found = bpy.data.collections.new(name)
    if name not in scene.collection.children.keys():
        scene.collection.children.link(found)
    return found


def replace_mesh(scene, *, art_id, mesh, owner, revision, collection_name,
                 object_name=None, expected_previous_revision=None):
    """Swap only the owned mesh datablock; keep object transform/parent/links.

    The old mesh is retained as a recoverable datablock (fake user) unless it is
    brand new. Caller owns the created mesh and must log the revision/evidence.
    """
    import bpy
    if not all(isinstance(v, str) and v for v in (art_id, owner, revision, collection_name)):
        raise ValueError("art_id, owner, revision and collection_name are required")
    if not isinstance(mesh, bpy.types.Mesh):
        raise TypeError("mesh must be bpy.types.Mesh")
    obj = find_by_art_id(scene, art_id)
    if obj is None:
        obj = bpy.data.objects.new(object_name or art_id, mesh)
        ensure_collection(scene, collection_name).objects.link(obj)
        obj["art_id"] = art_id
        obj["art_owner"] = owner
        obj["art_revision"] = revision
        return obj, "CREATED"
    if obj.type != "MESH" or obj.library is not None or obj.data.library is not None:
        raise ValueError("Refusing to replace nonlocal/nonmesh asset: " + art_id)
    if obj.get("art_owner") != owner:
        raise ValueError("Object owned by another generator: " + art_id)
    current = obj.get("art_revision")
    if expected_previous_revision is not None and current != expected_previous_revision:
        raise ValueError("Revision mismatch for " + art_id)
    if obj.data == mesh:
        obj["art_revision"] = revision
        return obj, "UNCHANGED"
    old_mesh = obj.data
    old_mesh.use_fake_user = True
    obj.data = mesh
    obj["art_revision"] = revision
    return obj, "REPLACED"
