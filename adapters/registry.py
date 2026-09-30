from .portable_adapter import ClaudeCodeAdapter, CrewAIAdapter, LyzrAdapter, OpenAIAdapter

ADAPTERS = {
    "openai": OpenAIAdapter,
    "crewai": CrewAIAdapter,
    "claude-code": ClaudeCodeAdapter,
    "lyzr": LyzrAdapter,
}


def get_adapter(name: str):
    if name not in ADAPTERS:
        raise ValueError(f"Unsupported adapter: {name}")
    return ADAPTERS[name]
