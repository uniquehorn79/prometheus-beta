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
    # Use Unicode-aware digit check to support various numeral systems
    import unicodedata
    
    # Validate input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Extract all digits from the string, converting each to an integer
    # Use unicodedata to catch digits from various scripts
    digits = [int(char) for char in input_string if unicodedata.category(char) in ['Nd', 'Digit']]
    
    # Return the sum of the digits
    return sum(digits)