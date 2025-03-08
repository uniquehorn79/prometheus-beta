import pytest
from src.vowel_consonant_counter import count_vowels_consonants

def test_basic_counting():
    """Test basic vowel and consonant counting"""
    result = count_vowels_consonants("hello world")
    assert result == {'vowels': 3, 'consonants': 7}

def test_mixed_case():
    """Test that the function works with mixed case"""
    result = count_vowels_consonants("HeLLo WoRLD")
    assert result == {'vowels': 3, 'consonants': 7}

def test_empty_string():
    """Test an empty string returns zero counts"""
    result = count_vowels_consonants("")
    assert result == {'vowels': 0, 'consonants': 0}

def test_only_vowels():
    """Test a string with only vowels"""
    result = count_vowels_consonants("aeiou")
    assert result == {'vowels': 5, 'consonants': 0}

def test_only_consonants():
    """Test a string with only consonants"""
    result = count_vowels_consonants("bcdfg")
    assert result == {'vowels': 0, 'consonants': 5}

def test_special_characters():
    """Test that special characters are ignored"""
    result = count_vowels_consonants("hello, world! 123")
    assert result == {'vowels': 3, 'consonants': 7}

def test_invalid_input():
    """Test that non-string input raises TypeError"""
    with pytest.raises(TypeError):
        count_vowels_consonants(123)
    with pytest.raises(TypeError):
        count_vowels_consonants(None)