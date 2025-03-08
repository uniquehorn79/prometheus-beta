import pytest
from src.longest_unique_substring import longest_unique_substring

def test_longest_unique_substring():
    # Test basic cases
    assert longest_unique_substring("abcabcbb") == 3  # "abc" is the longest
    assert longest_unique_substring("bbbbb") == 1     # "b" is the longest
    assert longest_unique_substring("pwwkew") == 3    # "wke" is the longest
    
    # Edge cases
    assert longest_unique_substring("") == 0          # Empty string
    assert longest_unique_substring(" ") == 1         # Single space
    assert longest_unique_substring("a") == 1         # Single character
    
    # More complex cases
    assert longest_unique_substring("dvdf") == 3      # Handles non-linear repeats
    assert longest_unique_substring("tmmzuxt") == 5   # Handles complex substring
    
    # Cases with special characters and mixed types
    assert longest_unique_substring("!@#$%^&*()") == 10  # All unique special chars
    assert longest_unique_substring("aA1!bB2@") == 8     # Mixed case and types
    
    # Repeated characters at different positions
    assert longest_unique_substring("abba") == 2
    assert longest_unique_substring("aab") == 2