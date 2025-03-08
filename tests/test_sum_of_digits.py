import pytest
from src.sum_of_digits import sum_of_digits

def test_sum_of_digits_basic():
    """Test basic functionality of sum_of_digits"""
    assert sum_of_digits('1234567890') == 45
    assert sum_of_digits('abc123') == 6

def test_sum_of_digits_edge_cases():
    """Test various edge cases"""
    # Empty string
    assert sum_of_digits('') == 0
    
    # String with no digits
    assert sum_of_digits('abcdef') == 0
    
    # String with leading zeros
    assert sum_of_digits('00123') == 6
    
    # Mixed string with multiple zeros
    assert sum_of_digits('a0b0c123') == 6

def test_sum_of_digits_special_cases():
    """Test special input scenarios"""
    # String with special characters
    assert sum_of_digits('!@#$123%^&*') == 6
    
    # String with decimal digits
    assert sum_of_digits('1.2.3') == 6

def test_sum_of_digits_type_error():
    """Test that the function handles type errors correctly"""
    with pytest.raises(TypeError):
        sum_of_digits(None)
    with pytest.raises(TypeError):
        sum_of_digits(123)  # Non-string input