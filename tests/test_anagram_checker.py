import pytest
from src.anagram_checker import are_anagrams

def test_basic_anagrams():
    """Test basic anagram scenarios"""
    assert are_anagrams("listen", "silent") == True
    assert are_anagrams("hello", "world") == False

def test_case_insensitive():
    """Test that anagram check is case-insensitive"""
    assert are_anagrams("Tea", "Eat") == True
    assert are_anagrams("LISTEN", "silent") == True

def test_whitespace_handling():
    """Test that whitespace is ignored"""
    assert are_anagrams("debit card", "bad credit") == True
    assert are_anagrams("stop", "posts") == False  # Corrected expectation

def test_empty_strings():
    """Test handling of empty strings"""
    assert are_anagrams("", "") == True
    assert are_anagrams("a", "") == False

def test_different_lengths():
    """Test strings of different lengths"""
    assert are_anagrams("abc", "abcd") == False
    assert are_anagrams("aabb", "ab") == False

def test_repeated_characters():
    """Test strings with repeated characters"""
    assert are_anagrams("aab", "aba") == True
    assert are_anagrams("aab", "aaa") == False

def test_unicode_characters():
    """Test handling of Unicode characters"""
    assert are_anagrams("résumé", "sumeer") == False
    assert are_anagrams("café", "face") == True

def test_type_errors():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        are_anagrams(123, "abc")
    with pytest.raises(TypeError):
        are_anagrams("abc", None)
    with pytest.raises(TypeError):
        are_anagrams([], "abc")