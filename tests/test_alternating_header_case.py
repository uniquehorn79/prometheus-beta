import pytest
from src.alternating_header_case import to_alternating_header_case

def test_basic_conversion():
    """Test basic string conversion to alternating header case"""
    assert to_alternating_header_case("hello world") == "HeLlO WoRlD"
    assert to_alternating_header_case("python is awesome") == "PyThOn Is AwEsOmE"

def test_single_word():
    """Test conversion of a single word"""
    assert to_alternating_header_case("hello") == "HeLlO"

def test_empty_string():
    """Test conversion of an empty string"""
    assert to_alternating_header_case("") == ""

def test_mixed_case_input():
    """Test input with mixed case"""
    assert to_alternating_header_case("HELLO world") == "HeLlO WoRlD"

def test_multiple_spaces():
    """Test input with multiple spaces"""
    assert to_alternating_header_case("  hello   world  ") == "HeLlO WoRlD"

def test_invalid_input():
    """Test raising TypeError for non-string input"""
    with pytest.raises(TypeError, match="Input must be a string"):
        to_alternating_header_case(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        to_alternating_header_case(None)

def test_special_characters():
    """Test conversion with special characters"""
    assert to_alternating_header_case("hello! world.") == "HeLlO! WoRlD."

def test_numbers_in_string():
    """Test conversion with numbers in the string"""
    assert to_alternating_header_case("hello 123 world") == "HeLlO 123 WoRlD"