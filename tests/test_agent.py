from core.agent_core import FeatureEngineeringAgent


def test_agent_discovers_tools():
    agent = FeatureEngineeringAgent()
    assert set(agent.registry.tools) == {"analyze-numeric", "encode-categorical", "select-features", "validate-dataset"}


def test_agent_executes_tool():
    result = FeatureEngineeringAgent().run("analyze-numeric", {"values": [1, 2, 3]})
    assert result["ok"] is True
    assert result["result"]["mean"] == 2


def test_unknown_tool_is_structured_error():
    result = FeatureEngineeringAgent().run("missing", {})
    assert result["ok"] is False
