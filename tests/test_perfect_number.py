import pytest
from src.perfect_number import is_perfect_number

def test_known_perfect_numbers():
    """Test known perfect numbers."""
    perfect_numbers = [6, 28, 496, 8128]
    for num in perfect_numbers:
        assert is_perfect_number(num), f"{num} should be a perfect number"

def test_non_perfect_numbers():
    """Test numbers that are not perfect numbers."""
    non_perfect_numbers = [7, 12, 18, 30, 100]
    for num in non_perfect_numbers:
        assert not is_perfect_number(num), f"{num} should not be a perfect number"

def test_edge_cases():
    """Test edge cases and boundary conditions."""
    # Zero and negative numbers are not perfect
    assert not is_perfect_number(0)
    assert not is_perfect_number(-6)
    assert not is_perfect_number(-28)

def test_invalid_input():
    """Test that invalid inputs raise appropriate exceptions."""
    with pytest.raises(ValueError):
        is_perfect_number(3.14)
    
    with pytest.raises(ValueError):
        is_perfect_number("not a number")
    
    with pytest.raises(ValueError):
        is_perfect_number(None)