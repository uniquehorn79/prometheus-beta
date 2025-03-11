from datetime import datetime, timedelta

def add_days_to_date(date, days_to_add):
    """
    Add a specified number of days to a given date.

    Args:
        date (str or datetime): The input date to modify. 
            Accepts date strings in 'YYYY-MM-DD' format or datetime objects.
        days_to_add (int): Number of days to add to the date. 
            Can be positive or negative.

    Returns:
        datetime: A new date after adding the specified number of days.

    Raises:
        ValueError: If the input date is invalid or days_to_add is not an integer.
        TypeError: If input types are incorrect.
    """
    # Validate input types
    if not isinstance(days_to_add, int):
        raise TypeError("Number of days must be an integer")
    
    # Convert input to datetime if it's a string
    if isinstance(date, str):
        try:
            date = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Use 'YYYY-MM-DD'")
    
    # Validate input is a datetime object
    if not isinstance(date, datetime):
        raise TypeError("Date must be a string in 'YYYY-MM-DD' format or a datetime object")
    
    # Add days and return new date
    return date + timedelta(days=days_to_add)