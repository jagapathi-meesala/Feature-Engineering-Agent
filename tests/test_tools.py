from tools.analyze_numeric import analyze
from tools.encode_categorical import encode
from tools.select_features import select
from tools.validate_dataset import validate
from contracts.tool_contract import ToolError


def test_numeric_analysis():
    assert analyze({"values": [1, 2, 3, 4]})["mean"] == 2.5


def test_categorical_encoding_is_deterministic():
    assert encode({"values": ["b", "a", "b"]})["encoded"] == [1, 0, 1]


def test_feature_selection_tie_break():
    assert select({"features": ["z", "a"], "scores": {"z": 1, "a": 1}, "k": 1})["selected"] == ["a"]


def test_dataset_validation():
    result = validate({"rows": [{"x": 1}, {"x": None}]})
    assert result["row_count"] == 2 and result["missing_values"]["x"] == 1


def test_invalid_numeric_input():
    try:
        analyze({"values": [1, float("nan")]})
    except ToolError:
        pass
    else:
        raise AssertionError("NaN must be rejected")
