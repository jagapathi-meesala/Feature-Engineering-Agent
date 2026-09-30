from contracts.tool_contract import ToolContract, ToolMetadata, ToolError


def encode(payload):
    values = payload["values"]
    if not isinstance(values, list):
        raise ToolError("values must be a list")
    if any(not isinstance(v, (str, int, float, bool)) or v is None for v in values):
        raise ToolError("categorical values must be scalar non-null values")
    categories = sorted({str(v) for v in values})
    mapping = {category: index for index, category in enumerate(categories)}
    encoded = [mapping[str(v)] for v in values]
    return {"categories": categories, "mapping": mapping, "encoded": encoded, "encoding": "deterministic ordinal by lexical category order"}


TOOL = ToolContract(ToolMetadata("encode-categorical", "Encode categorical values using deterministic lexical category ordering.", {"type": "object", "required": ["values"]}), encode)
