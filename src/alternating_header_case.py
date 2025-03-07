def to_alternating_header_case(text: str) -> str:
    """
    Convert a string to alternating header case.
    
    In alternating header case, words alternate between starting with 
    an uppercase and lowercase letter.
    
    Args:
        text (str): The input string to convert
    
    Returns:
        str: The string converted to alternating header case
    
    Raises:
        TypeError: If input is not a string
    
    Examples:
        >>> to_alternating_header_case("hello world")
        'HeLlO WoRlD'
        >>> to_alternating_header_case("python is awesome")
        'PyThOn Is AwEsOmE'
    """
    # Check input type
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string
    if not text:
        return ""
    
    # Split the string into words
    words = text.split()
    
    # Convert each word to alternating case
    alternating_words = []
    for word in words:
        converted_word = ''.join(
            char.upper() if idx % 2 == 0 else char.lower() 
            for idx, char in enumerate(word)
        )
        alternating_words.append(converted_word)
    
    # Join the words back together
    return ' '.join(alternating_words)