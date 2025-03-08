def reverse_words(input_string: str) -> str:
    """
    Reverse the order of words in a given string.

    This function splits the input string into words, ignoring multiple spaces
    and non-alphabetic characters, and then reverses the order of words.

    Args:
        input_string (str): The input string to be processed.

    Returns:
        str: A string with words reversed, preserving original spacing and non-alphabetic characters.

    Examples:
        >>> reverse_words("Hello World")
        'World Hello'
        >>> reverse_words("  Hello   World  ")
        '  World   Hello  '
        >>> reverse_words("Hello123 World456")
        'World456 Hello123'
    """
    # If input is empty or None, return as is
    if not input_string:
        return input_string

    # Split the string preserving whitespace
    parts = []
    current_word = []
    current_whitespace = []

    for char in input_string:
        if char.isspace():
            # If we were building a word, store it
            if current_word:
                parts.append(''.join(current_word))
                current_word = []
            current_whitespace.append(char)
        else:
            # If we had accumulated whitespace, store it
            if current_whitespace:
                parts.append(''.join(current_whitespace))
                current_whitespace = []
            current_word.append(char)

    # Handle any remaining word or whitespace
    if current_word:
        parts.append(''.join(current_word))
    if current_whitespace:
        parts.append(''.join(current_whitespace))

    # Reverse the parts, keeping words and whitespace
    return ''.join(parts[::-1])