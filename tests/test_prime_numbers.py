import pytest
from src.prime_numbers import find_primes_up_to_100

def test_find_primes_up_to_100():
    """
    Test the find_primes_up_to_100 function for correctness.
    """
    # Expected list of prime numbers up to 100
    expected_primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
        31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 
        73, 79, 83, 89, 97
    ]
    
    # Get the actual primes
    actual_primes = find_primes_up_to_100()
    
    # Check that the lists are exactly the same
    assert actual_primes == expected_primes, "The list of primes does not match the expected primes"

def test_prime_list_properties():
    """
    Additional tests to verify properties of the prime number list.
    """
    primes = find_primes_up_to_100()
    
    # Check list is sorted
    assert primes == sorted(primes), "Primes should be in ascending order"
    
    # Check all numbers are within the range
    assert all(2 <= p <= 100 for p in primes), "All primes should be between 2 and 100"
    
    # Verify no duplicates
    assert len(primes) == len(set(primes)), "Primes list should not contain duplicates"

def test_edge_cases():
    """
    Test edge cases for the prime number function.
    """
    primes = find_primes_up_to_100()
    
    # Check first and last primes
    assert primes[0] == 2, "First prime should be 2"
    assert primes[-1] == 97, "Last prime should be 97"
    
    # Verify correct number of primes
    assert len(primes) == 25, "There should be exactly 25 primes between 1 and 100"