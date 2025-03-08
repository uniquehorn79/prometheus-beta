def capitalize_comma_words(input_string: str) -> str:
    """
    Capitalize words in a comma-separated string of alphabetical characters.
    
    Args:
        input_string (str): A string of words separated by commas, 
                            containing only alphabetical characters.
    
    Returns:
        str: A new string with each word capitalized.
    
    Raises:
        ValueError: If the input string contains non-alphabetical characters.
    
    Example:
        >>> capitalize_comma_words("hello,world,python")
        'Hello,World,Python'
    """
    # Validate input contains only alphabetical characters and commas
    if not all(char.isalpha() or char == ',' for char in input_string):
        raise ValueError("Input must contain only alphabetical characters and commas")
    
    # Split the string, capitalize each word, then rejoin
    return ','.join(word.capitalize() for word in input_string.split(','))