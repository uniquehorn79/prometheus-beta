def count_unique_characters(input_string: str) -> int:
    """
    Count the number of unique characters in a given string.
    
    This function is case-sensitive, meaning 'a' and 'A' are considered 
    different characters.
    
    Args:
        input_string (str): The input string to analyze
    
    Returns:
        int: Number of unique characters in the string
    
    Examples:
        >>> count_unique_characters("hello")
        4
        >>> count_unique_characters("Hello")
        5
        >>> count_unique_characters("")
        0
        >>> count_unique_characters("   ")
        1
    """
    # Handle None or non-string input
    if input_string is None:
        return 0
    
    # Use a set to count unique characters
    # This preserves the case-sensitivity requirement
    return len(set(list(input_string)))