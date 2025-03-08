import pytest
from src.palindrome_checker import is_palindrome

def test_classic_palindromes():
    """Test classic palindrome strings."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True

def test_palindrome_with_spaces_and_punctuation():
    """Test palindromes with spaces and punctuation."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_case_insensitive():
    """Test case-insensitive palindrome checking."""
    assert is_palindrome("Able was I ere I saw Elba") == True

def test_empty_and_single_char_strings():
    """Test empty and single character strings."""
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True

def test_non_palindromes():
    """Test non-palindrome strings."""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_special_characters():
    """Test strings with various special characters."""
    assert is_palindrome("12321") == True
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("A1b2c3b1a") == False

def test_whitespace_only():
    """Test strings with only whitespace."""
    assert is_palindrome("   ") == True

def test_mixed_alphanumeric():
    """Test mixed alphanumeric palindromes."""
    assert is_palindrome("A1b1a") == True
    assert is_palindrome("a1b2b1a") == True
    assert is_palindrome("a1b2c3b1a") == False