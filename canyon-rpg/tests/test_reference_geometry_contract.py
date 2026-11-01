"""Scene-agnostic contract regression tests. Structural validation does not imply art approval."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "blueprint"))
from validate_reference_geometry_contract import validate


class ContractV2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.template = json.loads((ROOT / "blueprint/reference_geometry_contract.example.json").read_text())

    def result(self, mutate):
        candidate = copy.deepcopy(self.template)
        mutate(candidate)
        return validate(candidate)

    def test_valid_text_only_template_has_open_visual_check(self):
        result = validate(self.template)
        self.assertEqual(result["schema_version"], 2)
        self.assertEqual(result["status"], "STRUCTURE_PASS_WITH_OPEN_VISUAL_CHECKS")
        self.assertFalse(result["errors"])
        self.assertEqual(result["runtime_visual_validation"], "NOT_RUN")

    def test_no_views_allowed_during_p0(self):
        result = validate(self.template)
        self.assertFalse(result["errors"])
        self.assertEqual(result["camera_count"], 0)

    def with_view(self, data, **fields):
        data["review_views"].append({
            "view_id": "VIEW_TEST", "camera_object": None,
            "purpose": "TEST_ONLY", "approval": "UNAPPROVED"})
        check = {
            "view_id": "VIEW_TEST", "expected_uv_top_left": None,
            "tolerance_uv": None, "check_occlusion": False
        }
        check.update(fields)
        data["features"][0]["view_checks"].append(check)

    def test_duplicate_feature_id_fails(self):
        def mutate(d):
            d["features"][1]["feature_id"] = d["features"][0]["feature_id"]
        self.assertEqual(self.result(mutate)["status"], "FAIL")

    def test_dependency_cycle_fails(self):
        self.assertEqual(self.result(
            lambda d: d["features"][0]["dependency_ids"].append("feature_secondary")
        )["status"], "FAIL")

    def test_missing_reference_fails(self):
        self.assertEqual(self.result(
            lambda d: d["features"][0].update(source_refs=["absent_reference"])
        )["status"], "FAIL")

    def test_missing_view_fails(self):
        def mutate(data):
            data["features"][0]["view_checks"].append({
                "view_id": "NOT_A_VIEW", "expected_uv_top_left": None,
                "tolerance_uv": None})
        self.assertEqual(self.result(mutate)["status"], "FAIL")

    def test_invalid_screen_position_fails(self):
        def mutate(data):
            self.with_view(data, expected_uv_top_left=[1.3, 0.5], tolerance_uv=0.03)
        self.assertEqual(self.result(mutate)["status"], "FAIL")

    def test_unknown_target_must_not_have_tolerance(self):
        def mutate(data):
            self.with_view(data, expected_uv_top_left=None, tolerance_uv=0.02)
        self.assertEqual(self.result(mutate)["status"], "FAIL")

    def test_approved_target_validates_structure_only(self):
        def mutate(data):
            self.with_view(data, expected_uv_top_left=[0.4, 0.5], tolerance_uv=0.02)
        result = self.result(mutate)
        self.assertFalse(result["errors"])
        self.assertEqual(result["runtime_visual_validation"], "NOT_RUN")

    def test_invalid_stage_fails(self):
        self.assertEqual(self.result(
            lambda d: d["features"][0].update(stage="ENVIRONMENT_FORCED")
        )["status"], "FAIL")

    def test_v1_legacy_contract_still_supported(self):
        v1 = {
            "schema_version": 1, "scene_id": "legacy_case", "revision": "historic",
            "source_images": [{"image_id": "source_01"}],
            "cameras": [{"shot_id": "view_a", "camera_object": "camera_a"}],
            "features": [{
                "feature_id": "legacy_feature", "asset_id": "asset_a",
                "anchor_art_id": "anchor_a", "layer": "L1_MACRO",
                "evidence": "DESIGNED", "source_image_id": "source_01",
                "source_pixel_xy": None,
                "reference_shape": {
                    "must_preserve": ["stable shape"],
                    "may_redesign": ["unknown backside"],
                    "do_not_copy": ["unverified depth"]},
                "dependency_ids": [],
                "camera_checks": [{
                    "shot_id": "view_a", "expected_uv_top_left": None,
                    "tolerance_uv": None, "check_occlusion": False}]
            }]
        }
        result = validate(v1)
        self.assertFalse(result["errors"])
        self.assertEqual(result["runtime_visual_validation"], "NOT_RUN")


if __name__ == "__main__":
    unittest.main()
