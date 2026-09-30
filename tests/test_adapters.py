from adapters.registry import get_adapter


def test_adapter_names():
    for name in ["openai", "crewai", "claude-code", "lyzr"]:
        adapter = get_adapter(name)()
        assert adapter.invoke("analyze-numeric", {"values": [2, 4]})["ok"]
