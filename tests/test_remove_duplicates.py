import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test removing duplicates from a simple list."""
    input_list = [1, 2, 3, 2, 4, 1, 5]
    expected = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_empty_list():
    """Test removing duplicates from an empty list."""
    assert remove_duplicates([]) == []

def test_remove_duplicates_no_duplicates():
    """Test a list with no duplicates."""
    input_list = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_list) == input_list

def test_remove_duplicates_all_duplicates():
    """Test a list with all duplicate values."""
    input_list = [1, 1, 1, 1]
    assert remove_duplicates(input_list) == [1]

def test_remove_duplicates_mixed_types():
    """Test removing duplicates with mixed types."""
    input_list = [1, 'a', 2, 'a', 3, 1]
    expected = [1, 'a', 2, 3]
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_preserves_order():
    """Test that the function preserves the order of first occurrence."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = [3, 1, 4, 5, 9, 2, 6]
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_invalid_input():
    """Test that the function raises a TypeError for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates("not a list")
    
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates(123)
    
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates(None)