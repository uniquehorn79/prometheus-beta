from datetime import datetime, timezone

def convert_timestamp_to_readable_date(timestamp):
    """
    Convert a timestamp to a human-readable date string.

    Args:
        timestamp (int or float): Unix timestamp (seconds since epoch)

    Returns:
        str: Formatted date string in the format 'Month Day, Year at HH:MM:SS AM/PM'

    Raises:
        ValueError: If the timestamp is not a valid number
        OverflowError: If the timestamp is out of valid range
    """
    try:
        # Convert timestamp to float to handle both integer and float inputs
        timestamp_float = float(timestamp)
        
        # Convert to datetime object in UTC
        dt = datetime.fromtimestamp(timestamp_float, tz=timezone.utc)
        
        # Format the date in a human-readable way
        return dt.strftime('%B %d, %Y at %I:%M:%S %p %Z')
    
    except (TypeError, ValueError) as e:
        raise ValueError(f"Invalid timestamp: {timestamp}. Must be a numeric value.") from e
    except OverflowError:
        raise OverflowError(f"Timestamp {timestamp} is out of valid range.")