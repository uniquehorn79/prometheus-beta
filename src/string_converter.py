def convert_to_upper_case_with_spaces(input_string: str) -> str:
    """
    Convert a string to uppercase, preserving existing spaces and adding spaces between words.

    Args:
        input_string (str): The input string to be converted.

    Returns:
        str: A string converted to uppercase with spaces added between words.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If the input is empty, return an empty string
    if not input_string:
        return ""
    
    # Replace multiple spaces with a single space and strip leading/trailing spaces
    cleaned_string = ' '.join(input_string.split())
    
    # Convert to uppercase
    return cleaned_string.upper()