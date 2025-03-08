import pytest
from src.list_rotation import rotate_list

def test_basic_rotation():
    """Test basic right rotation of a list"""
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

def test_rotation_full_cycle():
    """Test rotation equal to list length returns same list"""
    assert rotate_list([1, 2, 3], 3) == [1, 2, 3]

def test_rotation_more_than_length():
    """Test rotation more than list length"""
    assert rotate_list([1, 2, 3], 4) == [3, 1, 2]

def test_empty_list():
    """Test rotation of an empty list"""
    assert rotate_list([], 5) == []

def test_zero_rotation():
    """Test rotation of 0 positions"""
    assert rotate_list([1, 2, 3], 0) == [1, 2, 3]

def test_single_element_list():
    """Test rotation of a single-element list"""
    assert rotate_list([42], 10) == [42]

def test_invalid_input_types():
    """Test invalid input types raise TypeError"""
    with pytest.raises(TypeError):
        rotate_list("not a list", 2)
    
    with pytest.raises(TypeError):
        rotate_list([1, 2, 3], "not an int")

def test_negative_rotation():
    """Test negative rotation raises ValueError"""
    with pytest.raises(ValueError):
        rotate_list([1, 2, 3], -1)