from abc import ABC, abstractmethod
from typing import Any

from core.agent_core import FeatureEngineeringAgent


class AgentAdapter(ABC):
    """Framework-neutral adapter boundary; no external agent SDK dependency."""

    @abstractmethod
    def invoke(self, tool: str, payload: dict[str, Any]) -> dict[str, Any]:
        raise NotImplementedError


class LocalAdapter(AgentAdapter):
    def __init__(self, agent: FeatureEngineeringAgent | None = None) -> None:
        self.agent = agent or FeatureEngineeringAgent()

    def invoke(self, tool: str, payload: dict[str, Any]) -> dict[str, Any]:
        return self.agent.run(tool, payload)


class OpenAIAdapter(LocalAdapter):
    """Portable boundary for an OpenAI SDK host; SDK integration is intentionally external."""


class CrewAIAdapter(LocalAdapter):
    """Portable boundary for a CrewAI host; CrewAI remains an optional host dependency."""


class ClaudeCodeAdapter(LocalAdapter):
    """Portable boundary for a Claude Code host; Claude tooling remains outside the core."""


class LyzrAdapter(LocalAdapter):
    """Portable boundary for a Lyzr host; Lyzr integration remains outside the core."""
