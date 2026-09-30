from contracts.tool_contract import ToolContract, ToolMetadata, ToolError


def validate(payload):
    rows = payload["rows"]
    if not isinstance(rows, list) or not rows:
        raise ToolError("rows must be a non-empty list of objects")
    if not all(isinstance(r, dict) for r in rows):
        raise ToolError("every row must be an object")
    columns = payload.get("columns") or sorted({k for r in rows for k in r})
    if not columns or any(not isinstance(c, str) or not c for c in columns):
        raise ToolError("columns must contain non-empty strings")
    missing = {c: sum(c not in r or r[c] is None for r in rows) for c in columns}
    types = {}
    for c in columns:
        values = [r[c] for r in rows if c in r and r[c] is not None]
        types[c] = sorted({type(v).__name__ for v in values})
    return {"row_count": len(rows), "columns": columns, "missing_values": missing, "observed_types": types}


TOOL = ToolContract(ToolMetadata("validate-dataset", "Validate tabular rows for shape, missingness, and observed types.", {"type": "object", "required": ["rows"]}), validate)
