import pytest
from src.most_frequent_integer_index import find_most_frequent_integer_index

def test_basic_functionality():
    """Test basic scenarios of finding most frequent integer index."""
    assert find_most_frequent_integer_index([1, 2, 3, 3, 1, 1]) == 4
    assert find_most_frequent_integer_index([1, 1, 2, 2, 3]) == 0
    assert find_most_frequent_integer_index([5, 5, 4, 4, 3, 3]) == 0

def test_empty_list():
    """Test handling of an empty list."""
    assert find_most_frequent_integer_index([]) is None

def test_single_element():
    """Test list with a single element."""
    assert find_most_frequent_integer_index([42]) == 0

def test_all_unique():
    """Test list where all elements are unique."""
    assert find_most_frequent_integer_index([1, 2, 3, 4, 5]) == 0

def test_complex_frequency():
    """Test more complex frequency scenarios."""
    # Multiple numbers with same frequency, should return first occurrence
    assert find_most_frequent_integer_index([1, 2, 1, 2, 3]) == 0
    assert find_most_frequent_integer_index([3, 1, 2, 1, 2, 3]) == 0

def test_negative_numbers():
    """Test handling of negative numbers."""
    assert find_most_frequent_integer_index([-1, -1, 2, 2, 3]) == 0
    assert find_most_frequent_integer_index([1, -1, -1, 2, 2]) == 1

def test_large_input():
    """Test with a larger input to ensure performance."""
    large_list = [1] * 1000 + [2] * 500 + [3] * 250
    assert find_most_frequent_integer_index(large_list) == 0