import pytest
from src.validate_ip_address import validate_single_digit_ip_address

def test_valid_ip_addresses():
    """Test valid single-digit IP addresses."""
    valid_ips = [
        "1.2.3.4",
        "0.0.0.0",
        "9.9.9.9"
    ]
    
    for ip in valid_ips:
        assert validate_single_digit_ip_address(ip) == True, f"{ip} should be valid"

def test_invalid_ip_addresses():
    """Test various invalid IP address formats."""
    invalid_ips = [
        # Wrong number of segments
        "1.2.3",  # Too few
        "1.2.3.4.5",  # Too many
        
        # Non-digit segments
        "a.2.3.4",  # Non-numeric
        "1.2.3.b",  # Non-numeric
        "1.2.3.4.",  # Extra dot
        ".1.2.3.4",  # Leading dot
        
        # Multi-digit segments
        "12.3.4.5",  # Two-digit segment
        
        # Type and edge cases
        "",  # Empty string
        None,  # None value
        "   ",  # Whitespace
        "1.2.3.4 ",  # Extra spaces
        " 1.2.3.4"  # Leading space
    ]
    
    for ip in invalid_ips:
        assert validate_single_digit_ip_address(ip) == False, f"{ip} should be invalid"

def test_edge_cases():
    """Test additional edge cases."""
    # Test digits at segment boundaries
    assert validate_single_digit_ip_address("0.0.0.0") == True
    assert validate_single_digit_ip_address("9.9.9.9") == True
    
    # Ensure non-numeric inputs are rejected
    assert validate_single_digit_ip_address("a.2.3.4") == False
    assert validate_single_digit_ip_address("1.a.3.4") == False
    assert validate_single_digit_ip_address("1.2.a.4") == False
    assert validate_single_digit_ip_address("1.2.3.a") == False