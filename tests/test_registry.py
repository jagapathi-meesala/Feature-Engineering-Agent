from core.agent_core import ToolRegistry
from pathlib import Path


def test_registry_discovery():
    registry = ToolRegistry()
    names = registry.discover(Path(__file__).parents[1] / "tools")
    assert len(names) == 4
