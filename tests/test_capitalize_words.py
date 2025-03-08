import pytest
from src.capitalize_words import capitalize_comma_words

def test_basic_capitalization():
    """Test basic capitalization of words"""
    assert capitalize_comma_words("hello,world,python") == "Hello,World,Python"

def test_already_capitalized():
    """Test string with already capitalized words"""
    assert capitalize_comma_words("Hello,World,Python") == "Hello,World,Python"

def test_mixed_case():
    """Test string with mixed case words"""
    assert capitalize_comma_words("hElLo,wOrLd,pYtHoN") == "Hello,World,Python"

def test_single_word():
    """Test capitalization of a single word"""
    assert capitalize_comma_words("hello") == "Hello"

def test_empty_string():
    """Test empty string input"""
    assert capitalize_comma_words("") == ""

def test_invalid_input_with_whitespace():
    """Test input with whitespace"""
    with pytest.raises(ValueError):
        capitalize_comma_words("hello, world")

def test_invalid_input_with_numbers():
    """Test input with numbers"""
    with pytest.raises(ValueError):
        capitalize_comma_words("hello,world123")

def test_invalid_input_with_special_chars():
    """Test input with special characters"""
    with pytest.raises(ValueError):
        capitalize_comma_words("hello,world!")