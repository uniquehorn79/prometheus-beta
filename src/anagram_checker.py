def is_anagram(str1: str, str2: str) -> bool:
    """
    Determine if two strings are anagrams.
    
    An anagram is a word or phrase formed by rearranging the letters of another, 
    using all the original letters exactly once.
    
    Args:
        str1 (str): The first string to compare
        str2 (str): The second string to compare
    
    Returns:
        bool: True if the strings are anagrams, False otherwise
    
    Examples:
        >>> is_anagram("listen", "silent")
        True
        >>> is_anagram("hello", "world")
        False
    
    Raises:
        TypeError: If either input is not a string
    """
    # Check input types
    if not (isinstance(str1, str) and isinstance(str2, str)):
        raise TypeError("Inputs must be strings")
    
    # Remove whitespace and convert to lowercase for case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Quick length check
    if len(str1) != len(str2):
        return False
    
    # Use character frequency counting
    char_count = {}
    
    # Count characters in first string
    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Subtract characters from second string
    for char in str2:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False
    
    return True