---
name: feature-validation
description: Inspect tabular feature data for structural quality issues.
---
# Feature Validation
## Purpose
Validate tabular rows before feature engineering.
## Inputs
Rows represented as dictionaries and optional column names.
## Processing
Check row structure, column presence, missing values, and observed Python scalar types.
## Outputs
A structured validation summary with row counts, columns, missingness, and observed types.
## Limitations
Validation is structural; it does not establish statistical correctness, causal validity, or absence of target leakage.
## Expected behavior
Fail clearly on malformed rows and never fabricate missing data.
