---
name: feature-selection
description: Select a deterministic top-k subset from supplied feature scores.
---
# Feature Selection
## Purpose
Choose a reproducible subset of candidate features from externally supplied scores.
## Inputs
Feature names, numeric scores, and a requested k.
## Processing
Sort by descending score and break ties lexically by feature name.
## Outputs
Selected features and the complete ranking with scores.
## Limitations
The skill does not calculate predictive importance or guarantee model performance; scores must come from a valid upstream method.
## Expected behavior
Reject mismatched feature/score sets and invalid k values.
