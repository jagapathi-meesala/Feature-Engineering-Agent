# Feature Engineering Agent

A framework-independent OpenGAP 0.1.0 agent for structural dataset validation, deterministic feature transformation, and score-based feature selection.

## Architecture
The core consists of a framework-neutral tool contract, dynamic registry, domain tools, skills, and adapter boundaries. Runtime configuration is supplied through environment variables; the core does not require an LLM SDK.

## Installation
```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

## Configuration
Copy `.env.example` to `.env` and provide `ENVIRONMENT`, `LOG_LEVEL`, `MAX_ROWS`, and `MAX_COLUMNS` through the environment. No credentials are required by the current implementation.

## Tools
- `validate-dataset`: checks row structure, missingness, and observed types.
- `analyze-numeric`: computes deterministic descriptive statistics.
- `encode-categorical`: encodes categories by lexical order.
- `select-features`: ranks supplied feature scores and returns top-k features.

## Skills
`feature-validation`, `feature-engineering`, and `feature-selection` document the capabilities used by the tools.

## Usage
```python
from core.agent_core import FeatureEngineeringAgent
agent = FeatureEngineeringAgent()
print(agent.run("encode-categorical", {"values": ["b", "a", "b"]}))
```

## Testing
Run `pytest -q` and `python verification/readiness_audit.py`.

## Portability
The core exposes adapter boundaries for OpenAI SDK, CrewAI, Claude Code, and Lyzr hosts. These are framework-independent interfaces; the repository does not claim external SDK integration has been tested.

## Limitations
This agent does not perform model-specific feature importance, automated target-leakage detection, imputation, causal analysis, or external data retrieval.
