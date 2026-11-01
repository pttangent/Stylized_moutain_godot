"""Prevent scene-specific historical requirements from leaking into canonical prompts.

Run: python -m unittest discover -s tests -p 'test_prompt_neutrality.py' -v
This is a text-level regression test, not a guarantee of general reasoning quality.
"""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROMPTS = ROOT / "prompts"
EXPECTED = {
    "00.md", "P0.md", "P0-A.md", "P0-B.md",
    "P0-A_world-model-optional.md", "P0-B_world-model-optional.md",
    "P1.md", "P1-concept.md", "P1-playable.md",
    "P2.md", "P2-A.md", "P2-B.md",
    "P3.md", "P3-A.md", "P3-B.md",
    "P4.md", "P4-A.md", "P4-B.md",
    "P5.md", "P5-A.md", "P5-B.md",
}
FORBIDDEN = [
    r"CAM_HERO_45", r"canyon-waterfall", r"blueprint/heightmap_16bit",
    r"main_fall", r"assets/worlds/", r"\bTripo\b", r"\bMarble\b",
    r"(?i:\b(?:waterfall|canyon|forest|river)\b)",
    r"(?:瀑布|草地|峽谷|森林|城市|室內|室外|野外)",
]


class PromptNeutralityTests(unittest.TestCase):
    def test_both_languages_expose_complete_canonical_phases(self):
        for language in ("en", "zh"):
            files = {p.name for p in (PROMPTS / language).glob("*.md")}
            self.assertEqual(EXPECTED, files, (language, EXPECTED ^ files))

    def test_core_prompts_do_not_hardcode_previous_scene(self):
        for language in ("en", "zh"):
            for path in (PROMPTS / language).glob("*.md"):
                text = path.read_text(encoding="utf-8")
                for pattern in FORBIDDEN:
                    self.assertIsNone(
                        re.search(pattern, text),
                        f"{path.relative_to(ROOT)} leaked pattern {pattern}",
                    )

    def test_fixed_45_engineering_camera_cannot_be_dropped(self):
        for language in ("en", "zh"):
            for name in ("00.md", "P0.md", "P0-A.md", "P0-B.md",
                         "P1.md", "P1-concept.md", "P2-B.md", "P3-B.md",
                         "P4-B.md", "P5-A.md", "P5-B.md"):
                content = (PROMPTS / language / name).read_text(encoding="utf-8")
                self.assertIn("CAM_QA_45", content, (language, name))
        doc = (ROOT / "docs/QA_CAMERA_45_STANDARD.md").read_text(encoding="utf-8")
        self.assertIn("45°", doc)
        self.assertIn("presentation camera", doc.lower())
        self.assertIn("lock", doc.lower())

    def test_qa_helper_parses_without_blender(self):
        import ast
        source = (ROOT / "blender/scripts/ensure_qa_45_camera.py").read_text(encoding="utf-8")
        ast.parse(source)
        self.assertIn('CAMERA_NAME = "CAM_QA_45"', source)
        self.assertIn('math.radians(45.0)', source)
        self.assertIn('cam["qa_locked"] = True', source)
        self.assertIn("--force-reframe", source)

    def test_reference_examples_are_separate_and_opt_in(self):
        text = (ROOT / "docs/SCENE_TYPE_EXAMPLES.md").read_text(encoding="utf-8").lower()
        for word in ("interior", "exterior", "city", "wilderness"):
            self.assertIn(word, text)
        self.assertIn("not defaults", text)

    def test_generic_contract_example_is_v2_without_scene_data(self):
        import json
        data = json.loads((ROOT / "blueprint/reference_geometry_contract.example.json").read_text())
        self.assertEqual(data["schema_version"], 2)
        self.assertEqual(data["revision"], "TEMPLATE_UNAPPROVED")
        self.assertIsNone(data["reference_sources"][0]["path"])
        self.assertIsNone(data["features"][0]["source_pixel_xy"])


if __name__ == "__main__":
    unittest.main()
