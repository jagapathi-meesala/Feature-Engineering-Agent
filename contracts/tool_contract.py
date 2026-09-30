from dataclasses import dataclass
from typing import Any, Callable


@dataclass(frozen=True)
class ToolMetadata:
    name: str
    description: str
    input_schema: dict[str, Any]


class ToolError(ValueError):
    """Expected, user-correctable tool failure."""


@dataclass
class ToolContract:
    metadata: ToolMetadata
    executor: Callable[[dict[str, Any]], dict[str, Any]]

    def validate(self, payload: dict[str, Any]) -> None:
        if not isinstance(payload, dict):
            raise ToolError("Input must be a JSON object.")
        required = self.metadata.input_schema.get("required", [])
        for key in required:
            if key not in payload:
                raise ToolError(f"Missing required field: {key}")

    def execute(self, payload: dict[str, Any]) -> dict[str, Any]:
        self.validate(payload)
        try:
            result = self.executor(payload)
        except ToolError:
            raise
        except (TypeError, ValueError) as exc:
            raise ToolError(str(exc)) from exc
        if not isinstance(result, dict):
            raise ToolError("Tool execution must return a structured object.")
        return result
