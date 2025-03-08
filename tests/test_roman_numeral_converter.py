import pytest
from src.roman_numeral_converter import convert_to_roman

def test_convert_to_roman_zero():
    """Test conversion of zero"""
    assert convert_to_roman(0) == ""

def test_convert_to_roman_single_digit():
    """Test conversion of single-digit numbers"""
    assert convert_to_roman(1) == "I"
    assert convert_to_roman(4) == "IV"
    assert convert_to_roman(5) == "V"
    assert convert_to_roman(9) == "IX"

def test_convert_to_roman_multiple_digits():
    """Test conversion of multi-digit numbers"""
    assert convert_to_roman(10) == "X"
    assert convert_to_roman(14) == "XIV"
    assert convert_to_roman(40) == "XL"
    assert convert_to_roman(50) == "L"
    assert convert_to_roman(90) == "XC"
    assert convert_to_roman(100) == "C"
    assert convert_to_roman(400) == "CD"
    assert convert_to_roman(500) == "D"
    assert convert_to_roman(900) == "CM"
    assert convert_to_roman(1000) == "M"

def test_convert_to_roman_complex_numbers():
    """Test conversion of complex numbers"""
    assert convert_to_roman(3999) == "MMMCMXCIX"
    assert convert_to_roman(2023) == "MMXXIII"
    assert convert_to_roman(1984) == "MCMLXXXIV"

def test_convert_to_roman_invalid_inputs():
    """Test handling of invalid inputs"""
    with pytest.raises(TypeError):
        convert_to_roman("1")
    
    with pytest.raises(ValueError):
        convert_to_roman(-1)
    
    with pytest.raises(ValueError):
        convert_to_roman(4000)