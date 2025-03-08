import pytest
from src.find_duplicates import find_duplicates

def test_find_duplicates_basic():
    """Test basic duplicate finding."""
    assert find_duplicates([1, 2, 3, 4, 2, 5, 6, 3]) == [2, 3]

def test_find_duplicates_no_duplicates():
    """Test case with no duplicates."""
    assert find_duplicates([1, 2, 3, 4, 5]) == []

def test_find_duplicates_all_duplicates():
    """Test case where all elements are duplicates."""
    assert find_duplicates([1, 1, 1, 1]) == [1]

def test_find_duplicates_empty_list():
    """Test empty list input."""
    assert find_duplicates([]) == []

def test_find_duplicates_sorted_output():
    """Ensure the output is sorted."""
    assert find_duplicates([3, 1, 2, 2, 1]) == [1, 2]

def test_find_duplicates_invalid_input_type():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_duplicates("not a list")

def test_find_duplicates_invalid_element_type():
    """Test raising TypeError for non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        find_duplicates([1, 2, "3", 4])

def test_find_duplicates_multiple_duplicates():
    """Test finding multiple duplicates of different frequencies."""
    assert find_duplicates([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == [2, 3, 4]