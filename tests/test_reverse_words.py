import pytest
from src.reverse_words import reverse_words

def test_basic_reverse():
    """Test basic word reversal."""
    assert reverse_words("Hello World") == "World Hello"

def test_multiple_spaces():
    """Test reversal with multiple spaces between words."""
    assert reverse_words("  Hello   World  ") == "  World   Hello  "

def test_with_numbers():
    """Test word reversal with numbers in words."""
    assert reverse_words("Hello123 World456") == "World456 Hello123"

def test_single_word():
    """Test reversal with a single word."""
    assert reverse_words("Hello") == "Hello"

def test_empty_string():
    """Test reversal with an empty string."""
    assert reverse_words("") == ""

def test_whitespace_only():
    """Test reversal with only whitespace."""
    assert reverse_words("   ") == "   "

def test_mixed_characters():
    """Test reversal with mixed alphabetic and non-alphabetic characters."""
    assert reverse_words("Hello! World.") == "World. Hello!"

def test_none_input():
    """Test handling of None input."""
    assert reverse_words(None) is None