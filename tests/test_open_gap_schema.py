from pathlib import Path
import yaml


def test_manifest_minimum_schema():
    root = Path(__file__).parents[1]
    data = yaml.safe_load((root / "agent.yaml").read_text(encoding="utf-8"))
    assert data["spec_version"] == "0.1.0"
    assert data["name"] == "feature-engineering-agent"
    assert data["version"] == "1.0.0"
    assert isinstance(data["skills"], list) and all(isinstance(x, str) for x in data["skills"])
    assert isinstance(data["tools"], list) and all(isinstance(x, str) for x in data["tools"])
    assert all((root / "skills" / s / "SKILL.md").is_file() for s in data["skills"])
    assert all((root / t).is_file() for t in data["tools"])
