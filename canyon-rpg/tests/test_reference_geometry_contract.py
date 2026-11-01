"""Offline structural regression tests; does not claim Blender visual verification."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "blueprint"))
from validate_reference_geometry_contract import validate


class ReferenceGeometryContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = json.loads((ROOT / "blueprint/reference_geometry_contract.example.json").read_text())

    def test_valid_example_has_unverified_camera_placements(self):
        result = validate(self.example)
        self.assertEqual(result["status"], "STRUCTURE_PASS_WITH_OPEN_VISUAL_CHECKS")
        self.assertFalse(result["errors"])
        self.assertEqual(result["runtime_visual_validation"], "NOT_RUN")

    def test_duplicate_feature_id_fails(self):
        candidate = copy.deepcopy(self.example)
        candidate["features"][1]["feature_id"] = candidate["features"][0]["feature_id"]
        self.assertEqual(validate(candidate)["status"], "FAIL")

    def test_cyclic_dependencies_fail(self):
        candidate = copy.deepcopy(self.example)
        candidate["features"][0]["dependency_ids"] = ["pool_main"]
        self.assertEqual(validate(candidate)["status"], "FAIL")

    def test_invalid_screen_target_fails(self):
        candidate = copy.deepcopy(self.example)
        target = candidate["features"][0]["camera_checks"][0]
        target["expected_uv_top_left"] = [1.3, 0.4]
        target["tolerance_uv"] = 0.03
        self.assertEqual(validate(candidate)["status"], "FAIL")

    def test_approved_target_cannot_have_zero_tolerance(self):
        candidate = copy.deepcopy(self.example)
        target = candidate["features"][0]["camera_checks"][0]
        target["expected_uv_top_left"] = [0.4, 0.4]
        target["tolerance_uv"] = 0
        self.assertEqual(validate(candidate)["status"], "FAIL")

    def test_unknown_image_id_fails(self):
        candidate = copy.deepcopy(self.example)
        candidate["features"][0]["source_image_id"] = "not_real"
        self.assertEqual(validate(candidate)["status"], "FAIL")


if __name__ == "__main__":
    unittest.main()
