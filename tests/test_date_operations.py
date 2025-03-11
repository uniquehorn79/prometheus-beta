import pytest
from datetime import datetime, timedelta
from src.date_operations import add_days_to_date

def test_add_days_to_date_string():
    """Test adding days to a date provided as a string."""
    result = add_days_to_date('2023-01-01', 5)
    assert result == datetime(2023, 1, 6)

def test_add_days_to_date_datetime():
    """Test adding days to a datetime object."""
    input_date = datetime(2023, 1, 1)
    result = add_days_to_date(input_date, 5)
    assert result == datetime(2023, 1, 6)

def test_add_negative_days():
    """Test subtracting days from a date."""
    result = add_days_to_date('2023-01-10', -5)
    assert result == datetime(2023, 1, 5)

def test_zero_days():
    """Test adding zero days."""
    result = add_days_to_date('2023-01-01', 0)
    assert result == datetime(2023, 1, 1)

def test_large_number_of_days():
    """Test adding a large number of days."""
    result = add_days_to_date('2023-01-01', 365)
    assert result == datetime(2024, 1, 1)

def test_invalid_date_format():
    """Test raising error for invalid date format."""
    with pytest.raises(ValueError, match="Invalid date format"):
        add_days_to_date('01-01-2023', 5)

def test_invalid_days_type():
    """Test raising error for non-integer days."""
    with pytest.raises(TypeError, match="Number of days must be an integer"):
        add_days_to_date('2023-01-01', '5')

def test_invalid_date_type():
    """Test raising error for invalid date type."""
    with pytest.raises(TypeError, match="Date must be a string"):
        add_days_to_date(12345, 5)

def test_leap_year():
    """Test adding days across a leap year boundary."""
    result = add_days_to_date('2024-02-28', 1)
    assert result == datetime(2024, 2, 29)

def test_leap_year_to_non_leap_year():
    """Test adding days from a leap year to a non-leap year."""
    result = add_days_to_date('2024-02-29', 365)
    assert result == datetime(2025, 2, 28)