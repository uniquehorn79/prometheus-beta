import pytest
from src.prime_factorization import prime_factorization

def test_prime_factorization_basic():
    """Test basic prime factorization scenarios."""
    assert prime_factorization(12) == (2, 2, 3)
    assert prime_factorization(15) == (3, 5)
    assert prime_factorization(100) == (2, 2, 5, 5)

def test_prime_factorization_prime_numbers():
    """Test prime numbers return themselves."""
    assert prime_factorization(2) == (2,)
    assert prime_factorization(7) == (7,)
    assert prime_factorization(11) == (11,)
    assert prime_factorization(13) == (13,)

def test_prime_factorization_large_numbers():
    """Test larger numbers for correct factorization."""
    assert prime_factorization(84) == (2, 2, 3, 7)
    assert prime_factorization(1260) == (2, 2, 3, 3, 5, 7)

def test_prime_factorization_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be greater than or equal to 2"):
        prime_factorization(1)
    
    with pytest.raises(ValueError, match="Input must be greater than or equal to 2"):
        prime_factorization(0)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        prime_factorization(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        prime_factorization("12")

def test_prime_factorization_edge_cases():
    """Test edge cases."""
    assert prime_factorization(2) == (2,)
    assert prime_factorization(3) == (3,)
    assert prime_factorization(4) == (2, 2)
    assert prime_factorization(2 * 3 * 5 * 7 * 11 * 13) == (2, 3, 5, 7, 11, 13)