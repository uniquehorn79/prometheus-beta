import pytest
from src.array_processor import process_multi_array

def test_basic_processing():
    """Test basic multi-array processing"""
    input_array = [[1, 2], [3, 4, 5]]
    expected = [2, 1, 5, 4, 3]
    assert process_multi_array(input_array) == expected

def test_remove_empty_subarrays():
    """Test removal of empty sub-arrays"""
    input_array = [[1, 2], [], [3, 4]]
    expected = [2, 1, 4, 3]
    assert process_multi_array(input_array) == expected

def test_remove_duplicates():
    """Test removal of duplicates while maintaining order"""
    input_array = [[1, 1], [2, 2], [3, 3]]
    expected = [1, 2, 3]
    assert process_multi_array(input_array) == expected

def test_mixed_elements():
    """Test processing with mixed types and duplicate elements"""
    input_array = [[1, 'a'], ['b', 2], [3, 'a', 4]]
    expected = ['a', 1, 2, 'b', 4, 3]
    assert process_multi_array(input_array) == expected

def test_empty_input():
    """Test processing an empty input array"""
    input_array = []
    expected = []
    assert process_multi_array(input_array) == expected

def test_nested_empty_arrays():
    """Test processing nested empty arrays"""
    input_array = [[], [1, 2], []]
    expected = [2, 1]
    assert process_multi_array(input_array) == expected

def test_complex_nested_array():
    """Test processing a more complex nested array"""
    input_array = [[1, [2, 3]], [4, 5], [6]]
    expected = [6]  # Function doesn't handle further nested arrays
    assert process_multi_array(input_array) == expected