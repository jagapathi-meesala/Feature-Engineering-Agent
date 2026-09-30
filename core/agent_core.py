from dataclasses import dataclass
from importlib import import_module
from pathlib import Path
from typing import Any

from contracts.tool_contract import ToolContract, ToolError


@dataclass
class ToolRegistry:
    tools: dict[str, ToolContract]

    def __init__(self) -> None:
        self.tools = {}

    def register(self, tool: ToolContract) -> None:
        if tool.metadata.name in self.tools:
            raise ToolError(f"Tool already registered: {tool.metadata.name}")
        self.tools[tool.metadata.name] = tool

    def discover(self, tools_dir: Path) -> list[str]:
        discovered = []
        for path in sorted(tools_dir.glob("*.py")):
            if path.name == "__init__.py":
                continue
            module = import_module(f"tools.{path.stem}")
            contract = getattr(module, "TOOL", None)
            if not isinstance(contract, ToolContract):
                raise ToolError(f"Tool module lacks TOOL contract: {path.name}")
            self.register(contract)
            discovered.append(contract.metadata.name)
        return discovered

    def execute(self, name: str, payload: dict[str, Any]) -> dict[str, Any]:
        tool = self.tools.get(name)
        if tool is None:
            return {"ok": False, "error": {"type": "unknown_tool", "message": name}}
        try:
            return {"ok": True, "tool": name, "result": tool.execute(payload)}
        except ToolError as exc:
            return {"ok": False, "tool": name, "error": {"type": "validation_or_execution", "message": str(exc)}}


class FeatureEngineeringAgent:
    def __init__(self, tools_dir: str | Path | None = None) -> None:
        self.registry = ToolRegistry()
        root = Path(tools_dir) if tools_dir else Path(__file__).resolve().parents[1] / "tools"
        self.registry.discover(root)

    def run(self, tool_name: str, payload: dict[str, Any]) -> dict[str, Any]:
        return self.registry.execute(tool_name, payload)
