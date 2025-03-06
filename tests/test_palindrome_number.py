import pytest
from src.palindrome_number import is_palindrome

def test_positive_palindrome():
    """Test palindrome numbers."""
    assert is_palindrome(121) == True
    assert is_palindrome(11) == True
    assert is_palindrome(12321) == True
    assert is_palindrome(0) == True
    assert is_palindrome(1) == True

def test_non_palindrome():
    """Test non-palindrome numbers."""
    assert is_palindrome(10) == False
    assert is_palindrome(123) == False
    assert is_palindrome(1234) == False

def test_negative_numbers():
    """Test negative numbers (should return False)."""
    assert is_palindrome(-121) == False
    assert is_palindrome(-11) == False

def test_invalid_input():
    """Test invalid input types."""
    with pytest.raises(TypeError):
        is_palindrome("121")
    with pytest.raises(TypeError):
        is_palindrome(12.34)
    with pytest.raises(TypeError):
        is_palindrome(None)