import pytest
from src.array_shuffler import shuffle_array
import random

def test_shuffle_array_basic():
    """Test basic shuffling functionality."""
    original = [1, 2, 3, 4, 5]
    shuffled = shuffle_array(original)
    
    # Verify shuffled array has same elements
    assert sorted(shuffled) == sorted(original)
    
    # Verify shuffled array is not exactly the same as original
    # (though this could technically happen by chance)
    assert shuffled != original

def test_shuffle_array_empty():
    """Test shuffling an empty list."""
    empty_list = []
    shuffled = shuffle_array(empty_list)
    assert shuffled == []

def test_shuffle_array_single_element():
    """Test shuffling a list with a single element."""
    single_elem = [42]
    shuffled = shuffle_array(single_elem)
    assert shuffled == [42]

def test_shuffle_array_large_list():
    """Test shuffling a larger list."""
    large_list = list(range(100))
    shuffled = shuffle_array(large_list)
    
    # Verify shuffled array has same elements
    assert sorted(shuffled) == sorted(large_list)
    
    # Verify shuffled array is not exactly the same as original
    assert shuffled != large_list

def test_shuffle_array_different_types():
    """Test shuffling a list with different types of elements."""
    mixed_list = [1, 'a', True, 3.14, None]
    shuffled = shuffle_array(mixed_list)
    
    # Verify shuffled array has same elements
    assert sorted(shuffled, key=str) == sorted(mixed_list, key=str)
    
    # Verify shuffled array is not exactly the same as original
    assert shuffled != mixed_list

def test_shuffle_array_invalid_input():
    """Test that invalid inputs raise a TypeError."""
    with pytest.raises(TypeError):
        shuffle_array("not a list")
    
    with pytest.raises(TypeError):
        shuffle_array(123)
    
    with pytest.raises(TypeError):
        shuffle_array(None)

def test_shuffle_array_randomness():
    """Test that multiple shuffles produce different results."""
    original = list(range(10))
    
    # Set a seed for reproducibility of the randomness test
    random.seed(42)
    
    # Perform multiple shuffles
    shuffles = [shuffle_array(original) for _ in range(10)]
    
    # Verify that not all shuffles are the same
    # This checks that the shuffling is somewhat random
    assert len(set(tuple(s) for s in shuffles)) > 1