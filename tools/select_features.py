from contracts.tool_contract import ToolContract, ToolMetadata, ToolError


def select(payload):
    features = payload["features"]
    scores = payload["scores"]
    k = payload["k"]
    if not isinstance(features, list) or not all(isinstance(x, str) and x for x in features):
        raise ToolError("features must be a list of non-empty strings")
    if not isinstance(scores, dict) or set(scores) != set(features):
        raise ToolError("scores must contain exactly one numeric score for each feature")
    if not isinstance(k, int) or isinstance(k, bool) or k < 1 or k > len(features):
        raise ToolError("k must be between 1 and the number of features")
    if any(isinstance(v, bool) or not isinstance(v, (int, float)) for v in scores.values()):
        raise ToolError("scores must be numeric")
    ranked = sorted(features, key=lambda f: (-scores[f], f))
    return {"selected": ranked[:k], "ranking": [{"feature": f, "score": scores[f]} for f in ranked], "k": k}


TOOL = ToolContract(ToolMetadata("select-features", "Select top-k features using deterministic score ordering with lexical tie-breaking.", {"type": "object", "required": ["features", "scores", "k"]}), select)
