---
name: feature-engineering
description: Apply deterministic, validated feature transformations.
---
# Feature Engineering
## Purpose
Transform numeric and categorical feature values into structured representations suitable for downstream modeling.
## Inputs
Validated JSON-like feature values and transformation parameters.
## Processing
Use the registered deterministic tools and preserve explicit input validation before transformation.
## Outputs
Structured results containing transformed values, mappings, or statistics.
## Limitations
The skill does not infer domain meaning, perform model-specific leakage analysis, or replace human review of transformations.
## Expected behavior
Reject malformed inputs and return reproducible outputs for identical inputs.
