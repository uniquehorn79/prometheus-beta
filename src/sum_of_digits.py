def sum_of_digits(input_string: str) -> int:
    """
    Calculate the sum of all digits in the given input string.

    Args:
        input_string (str): The input string to extract digits from.

    Returns:
        int: The sum of all digits in the string, ignoring leading zeros.

    Examples:
        >>> sum_of_digits('1234567890')
        45
        >>> sum_of_digits('abc123')
        6
        >>> sum_of_digits('no digits')
        0
    """
    # Extract all digits from the string, converting each to an integer
    # Use strip to handle any leading zeros
    digits = [int(char) for char in input_string if char.isdigit()]
    
    # Return the sum of the digits
    return sum(digits)