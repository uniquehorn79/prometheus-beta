import pytest
from src.timestamp_converter import convert_timestamp_to_readable_date

def test_convert_timestamp_standard_cases():
    # Test a few well-known timestamps
    assert convert_timestamp_to_readable_date(0) == 'January 01, 1970 at 12:00:00 AM UTC'
    assert convert_timestamp_to_readable_date(1609459200) == 'January 01, 2021 at 12:00:00 AM UTC'

def test_convert_timestamp_float_input():
    # Test float timestamp
    assert convert_timestamp_to_readable_date(1609459200.5) == 'January 01, 2021 at 12:00:00 AM UTC'

def test_convert_timestamp_invalid_inputs():
    # Test invalid input types
    with pytest.raises(ValueError, match="Invalid timestamp"):
        convert_timestamp_to_readable_date("not a number")
    
    with pytest.raises(ValueError, match="Invalid timestamp"):
        convert_timestamp_to_readable_date(None)

def test_convert_timestamp_extreme_values():
    # Test extremely large timestamp
    with pytest.raises(OverflowError):
        convert_timestamp_to_readable_date(2**64)  # Way beyond valid range
    
    # Test extremely small timestamp
    with pytest.raises(OverflowError):
        convert_timestamp_to_readable_date(-2**64)  # Way beyond valid range

def test_convert_timestamp_different_formats():
    # Test different numeric formats
    assert convert_timestamp_to_readable_date(1234567890) == 'February 13, 2009 at 11:31:30 PM UTC'
    assert convert_timestamp_to_readable_date(float(1234567890)) == 'February 13, 2009 at 11:31:30 PM UTC'