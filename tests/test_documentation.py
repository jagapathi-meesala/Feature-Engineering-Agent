from pathlib import Path


def test_required_docs_exist():
    root = Path(__file__).parents[1]
    for name in ["SOUL.md", "RULES.md", "DUTIES.md", "AGENTS.md", "README.md", "EXPLAINABILITY.md"]:
        assert (root / name).is_file()


def test_skill_frontmatter():
    root = Path(__file__).parents[1]
    for skill in ["feature-engineering", "feature-validation", "feature-selection"]:
        text = (root / "skills" / skill / "SKILL.md").read_text(encoding="utf-8")
        assert text.startswith("---\n") and "name:" in text and "description:" in text
