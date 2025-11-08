import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("  abc", "  Paper"),
    ("  hello world", "  Hello world"),
    (  "123"), (  "04 ноября 2025"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("World","W"),
    ("book","K"),
])
def test_contains_positive(input_str,expected):
    assert string_utils.contains(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("Book", "B"),
    ("House", "U"),
    ("homework","work"),
])
def test_delete_symbol_positive(input_str, expected):
    assert string_utils.delete_symbol(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", " "),
    ("none", " !@#$^"),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("Lake", "S"),
    ("12", "M"),
    ("!","12"),
])
def test_contains_negative(input_str, expected):
    assert string_utils.contains(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("Book", "12"),
    ("Horse", " !@#$^"),
    ("Huge","M"),
])
def test_delete_symbol_negative(input_str, expected):
    assert string_utils.delete_symbol(input_str) == expected