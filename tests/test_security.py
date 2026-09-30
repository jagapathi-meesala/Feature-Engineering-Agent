from core.agent_core import FeatureEngineeringAgent


def test_missing_required_field_does_not_execute():
    result = FeatureEngineeringAgent().run("analyze-numeric", {})
    assert result["ok"] is False


def test_invalid_type_is_rejected():
    result = FeatureEngineeringAgent().run("select-features", {"features": "x", "scores": {}, "k": 1})
    assert result["ok"] is False


def test_no_secret_defaults_in_config():
    text = open("config/settings.py", encoding="utf-8").read()
    assert "API_KEY" not in text and "SECRET" not in text
