import math
from contracts.tool_contract import ToolContract, ToolMetadata, ToolError


def analyze(payload):
    values = payload["values"]
    if not isinstance(values, list) or not values:
        raise ToolError("values must be a non-empty list")
    if any(isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) for v in values):
        raise ToolError("values must contain only finite numbers")
    ordered = sorted(values)
    n = len(values)
    mean = sum(values) / n
    variance = sum((x - mean) ** 2 for x in values) / n
    q1 = ordered[(n - 1) // 4]
    median = ordered[(n - 1) // 2]
    q3 = ordered[(3 * (n - 1)) // 4]
    return {"count": n, "mean": mean, "std": math.sqrt(variance), "min": ordered[0], "q1": q1, "median": median, "q3": q3, "max": ordered[-1]}


TOOL = ToolContract(ToolMetadata("analyze-numeric", "Compute deterministic descriptive statistics for a numeric feature.", {"type": "object", "required": ["values"]}), analyze)
