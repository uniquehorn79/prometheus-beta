import pytest
from src.odd_occurrence_finder import find_odd_occurrence

def test_basic_odd_occurrence():
    """Test basic scenario with one number appearing odd times"""
    assert find_odd_occurrence([1, 1, 2, 2, 3]) == 3

def test_multiple_odd_occurrences():
    """Test scenario with multiple numbers appearing odd times"""
    assert find_odd_occurrence([1, 1, 2, 2, 3, 3, 3, 4, 4]) == 3

def test_single_number():
    """Test with a single number"""
    assert find_odd_occurrence([5]) == 5

def test_repeated_number():
    """Test with a number repeated odd times"""
    assert find_odd_occurrence([5, 5, 5]) == 5

def test_large_numbers():
    """Test with larger numbers"""
    assert find_odd_occurrence([1000, 1000, 2000, 2000, 3000]) == 3000

def test_negative_numbers():
    """Test with negative numbers"""
    assert find_odd_occurrence([-1, -1, 2, 2, -3]) == -3

def test_empty_list_raises_error():
    """Test that empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_odd_occurrence([])

def test_no_odd_occurrence_raises_error():
    """Test that a list with no odd occurrence numbers raises a ValueError"""
    with pytest.raises(ValueError, match="No number appears an odd number of times"):
        find_odd_occurrence([1, 1, 2, 2, 3, 3])