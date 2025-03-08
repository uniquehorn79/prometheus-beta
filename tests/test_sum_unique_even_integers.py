import pytest
from src.sum_unique_even_integers import sum_unique_even_integers

def test_basic_unique_even_sum():
    """Test basic functionality with unique even numbers"""
    assert sum_unique_even_integers([2, 4, 6, 8]) == 0
    
def test_mix_of_even_numbers():
    """Test mix of repeated and unique even numbers"""
    assert sum_unique_even_integers([2, 2, 4, 6, 8, 10, 10]) == 6
    
def test_empty_list():
    """Test with an empty list"""
    assert sum_unique_even_integers([]) == 0
    
def test_no_even_numbers():
    """Test list with only odd numbers"""
    assert sum_unique_even_integers([1, 3, 5, 7]) == 0
    
def test_negative_even_numbers():
    """Test with negative even numbers"""
    assert sum_unique_even_integers([-2, -4, -2, 6, -6]) == -6
    
def test_input_type_error():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        sum_unique_even_integers("not a list")
    
def test_non_integer_elements():
    """Test that TypeError is raised for non-integer elements"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_unique_even_integers([1, 2, "3", 4])
    
def test_mixed_unique_and_repeated_numbers():
    """Test a more complex scenario with mixed number types"""
    assert sum_unique_even_integers([2, 2, 4, 4, 6, 8, 10, 10, 12]) == 8