import pytest
from src.anagram_checker import is_anagram

def test_basic_anagrams():
    """Test basic anagram scenarios"""
    assert is_anagram("listen", "silent") == True
    assert is_anagram("rail safety", "fairy tales") == True
    assert is_anagram("hello", "world") == False

def test_case_insensitive():
    """Test that anagram check is case-insensitive"""
    assert is_anagram("Tea", "Eat") == True
    assert is_anagram("Race", "Care") == True

def test_whitespace_handling():
    """Test that whitespace is ignored"""
    assert is_anagram("debit card", "bad credit") == True
    assert is_anagram("eleven plus two", "twelve plus one") == True

def test_empty_strings():
    """Test empty string scenarios"""
    assert is_anagram("", "") == True
    assert is_anagram("a", "") == False

def test_different_lengths():
    """Test strings of different lengths"""
    assert is_anagram("abc", "abcd") == False
    assert is_anagram("abc", "ab") == False

def test_repeated_characters():
    """Test strings with repeated characters"""
    assert is_anagram("aab", "aba") == True
    assert is_anagram("aab", "abc") == False

def test_type_errors():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        is_anagram(123, "abc")
    with pytest.raises(TypeError):
        is_anagram("abc", [1, 2, 3])
    with pytest.raises(TypeError):
        is_anagram(None, "test")

def test_unicode_characters():
    """Test anagram check with unicode characters"""
    assert is_anagram("café", "facé") == True
    assert is_anagram("résumé", "suméré") == True