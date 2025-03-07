import pytest
from src.string_converter import convert_to_upper_case_with_spaces

def test_convert_to_upper_case_with_spaces():
    # Test basic conversion
    assert convert_to_upper_case_with_spaces("hello world") == "HELLO WORLD"
    
    # Test with mixed case
    assert convert_to_upper_case_with_spaces("Hello World") == "HELLO WORLD"
    
    # Test with multiple spaces
    assert convert_to_upper_case_with_spaces("hello   world") == "HELLO WORLD"
    
    # Test with leading and trailing spaces
    assert convert_to_upper_case_with_spaces("  hello world  ") == "HELLO WORLD"
    
    # Test empty string
    assert convert_to_upper_case_with_spaces("") == ""
    
    # Test string with only spaces
    assert convert_to_upper_case_with_spaces("   ") == ""

def test_convert_to_upper_case_with_spaces_error_handling():
    # Test non-string input raises TypeError
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_upper_case_with_spaces(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_upper_case_with_spaces(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_upper_case_with_spaces(["hello"])

def test_convert_to_upper_case_with_spaces_edge_cases():
    # Test string with special characters
    assert convert_to_upper_case_with_spaces("hello, world!") == "HELLO, WORLD!"
    
    # Test string with numbers
    assert convert_to_upper_case_with_spaces("hello 123 world") == "HELLO 123 WORLD"