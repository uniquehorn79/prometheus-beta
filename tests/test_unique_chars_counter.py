import pytest
from src.unique_chars_counter import count_unique_characters

def test_count_unique_characters():
    # Test various scenarios
    assert count_unique_characters("hello") == 4  # h, e, l, o
    assert count_unique_characters("Hello") == 4  # H, e, l, o
    assert count_unique_characters("") == 0  # Empty string
    assert count_unique_characters("   ") == 1  # Whitespace
    assert count_unique_characters("aAaA") == 2  # Case-sensitive
    
def test_none_input():
    # Test None input
    assert count_unique_characters(None) == 0

def test_special_characters():
    # Test special characters and mixed inputs
    assert count_unique_characters("!@#$%^") == 6
    assert count_unique_characters("a1B2c3") == 6
    
def test_unicode_characters():
    # Test unicode characters
    assert count_unique_characters("こんにちは") == 5  # 5 unique Japanese characters
    assert count_unique_characters("áéíóú") == 5  # 5 unique accented characters