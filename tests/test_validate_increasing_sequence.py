import pytest
from src.validate_increasing_sequence import is_valid_increasing_sequence

def test_valid_increasing_sequence():
    """Test valid strictly increasing sequences"""
    assert is_valid_increasing_sequence([1, 2, 3, 4, 5]) == True
    assert is_valid_increasing_sequence([10, 20, 30, 40]) == True
    assert is_valid_increasing_sequence([-5, -3, 0, 2, 4]) == True

def test_invalid_increasing_sequence():
    """Test invalid sequences"""
    assert is_valid_increasing_sequence([1, 1, 2, 3]) == False  # Duplicate elements
    assert is_valid_increasing_sequence([5, 4, 3, 2, 1]) == False  # Decreasing sequence
    assert is_valid_increasing_sequence([1, 3, 2, 4]) == False  # Not strictly increasing

def test_edge_cases():
    """Test edge cases"""
    assert is_valid_increasing_sequence([]) == True  # Empty list
    assert is_valid_increasing_sequence([42]) == True  # Single element list

def test_invalid_input_types():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        is_valid_increasing_sequence("not a list")
    with pytest.raises(TypeError):
        is_valid_increasing_sequence(123)
    with pytest.raises(TypeError):
        is_valid_increasing_sequence(None)

def test_mixed_types():
    """Test sequences with non-integer elements"""
    assert is_valid_increasing_sequence([1, 2, 3, 'a']) == False
    assert is_valid_increasing_sequence([1, 2.5, 3]) == False