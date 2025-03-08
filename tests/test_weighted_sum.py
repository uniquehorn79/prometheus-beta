import pytest
from src.weighted_sum import compute_weighted_sum

def test_compute_weighted_sum_basic():
    """Test basic weighted sum computation with integers."""
    numbers = [1, 2, 3]
    weights = [1, 2, 3]
    assert compute_weighted_sum(numbers, weights) == 14

def test_compute_weighted_sum_floats():
    """Test weighted sum computation with floating point numbers."""
    numbers = [1.5, 2.5, 3.5]
    weights = [1.0, 2.0, 3.0]
    assert compute_weighted_sum(numbers, weights) == 17.0

def test_compute_weighted_sum_unequal_lengths():
    """Test that an error is raised when input lists have different lengths."""
    numbers = [1, 2, 3]
    weights = [1, 2]
    with pytest.raises(ValueError, match="Numbers and weights lists must have equal length"):
        compute_weighted_sum(numbers, weights)

def test_compute_weighted_sum_empty_lists():
    """Test that an error is raised when input lists are empty."""
    numbers = []
    weights = []
    with pytest.raises(ValueError, match="Input lists cannot be empty"):
        compute_weighted_sum(numbers, weights)

def test_compute_weighted_sum_invalid_types():
    """Test that an error is raised when non-numeric types are provided."""
    numbers = [1, 2, 'three']
    weights = [1, 2, 3]
    with pytest.raises(TypeError, match="All elements in numbers and weights must be numeric"):
        compute_weighted_sum(numbers, weights)

def test_compute_weighted_sum_mixed_numeric_types():
    """Test weighted sum computation with mixed numeric types."""
    numbers = [1, 2.5, 3]
    weights = [1.0, 2, 3.5]
    assert compute_weighted_sum(numbers, weights) == 16.5