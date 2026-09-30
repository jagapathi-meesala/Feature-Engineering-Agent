# Explainability

## Inputs and Data Sources
Input data consists of structured rows, numeric value arrays, categorical value arrays, and feature-score mappings supplied directly by the caller. Data sources are caller-provided inputs; the agent does not silently fetch external datasets, and each tool declares the fields it consumes.

### Input Requirements
The validation tool expects a non-empty list of row objects. Transformation tools require the specific arrays or mappings documented by their contracts, and malformed or missing required fields are rejected.

### Failure Handling
Invalid types, missing required fields, non-finite numeric values, mismatched feature scores, and invalid selection sizes produce structured errors. The agent does not silently coerce ambiguous data or invent replacements.

## Decision and Reasoning
The decision process is deterministic for the implemented transformations: numeric analysis computes descriptive statistics, categorical encoding orders distinct category strings lexically, and feature selection sorts supplied scores descending with lexical tie-breaking. The agent therefore decides from explicit input values and documented rules rather than hidden model judgments or external framework behavior.

### Rules Applied
For feature selection, a feature with a higher supplied score ranks before a lower-scored feature; equal scores are resolved by feature name. For categorical encoding, sorted distinct category strings receive consecutive integer identifiers starting at zero.

### Expected Outputs
Every successful tool returns a structured dictionary describing the computed result. Every failed execution returns an explicit error object through the agent core instead of reporting success.

### Worked Example
Given categories `['b', 'a', 'b']`, the encoding tool produces the lexical mapping `{'a': 0, 'b': 1}` and encoded values `[1, 0, 1]`. Given feature scores `{'age': 0.7, 'income': 0.7, 'city': 0.4}` with `k=2`, the deterministic ranking selects `age` and `income` because the equal scores are resolved lexically.

## Limits and Constraints
The agent cannot determine whether a feature is causally meaningful, whether a transformation improves a particular model, or whether a dataset contains target leakage without additional domain and experimental evidence. It also does not provide production claims about external frameworks because those integrations are adapter boundaries rather than tested dependencies in the core.

### Constraints
The implementation is intentionally dependency-light and operates on in-memory JSON-like structures. It does not automatically read arbitrary files, connect to databases, call remote APIs, or store secrets.

### Known Issues
The numeric quartile calculation uses deterministic positional selection rather than an interpolated statistical percentile method. Structural validation also reports observed types but does not prove semantic correctness or statistical quality.

### Unsupported Behavior
Automatic imputation, automated target-leakage detection, model-specific feature importance calculation, and uncontrolled external data retrieval are outside the current tool contracts.
