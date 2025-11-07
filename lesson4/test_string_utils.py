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
    (" Paper", "Paper"),
    (" Hello world", " Hello world"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("world","w"),("true"),
    ("book","b"),("true"),
])
def test_contains_positive(input_str,expected):
    assert string_utils.contains(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("Book"), ("ook"),
    ("House"), ("hose"),
    ("homework"),("home"),
])
def test_delete_symbol_positive(input_str, expected):
    assert string_utils.delete_symbol(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc"), ("123Abc"),
    (""), ("Abc"),
    ("   "), ("Lake"),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    (" ", ""), ("false"), ("false"),
    (" none", "!@#$^"), ("false"),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("Lake"), ("S"),
    ("12"), ("M"),
    ("!"),("12"),
])
def test_contains_negative(input_str, expected):
    assert string_utils.contains(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("Book"), ("12"),
    ("Horse"), (" !@#$^"),
    ("Huge"),("M"),
])
def test_delete_symbol_negative(input_str, expected):
    assert string_utils.delete_symbol(input_str) == expected