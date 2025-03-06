def is_palindrome(number):
    """
    Check if a given number is a palindrome.
    
    A palindrome number reads the same backward as forward.
    
    Args:
        number (int): The number to check for palindrome property.
    
    Returns:
        bool: True if the number is a palindrome, False otherwise.
    
    Raises:
        TypeError: If the input is not an integer.
    
    Examples:
        >>> is_palindrome(121)
        True
        >>> is_palindrome(-121)
        False
        >>> is_palindrome(10)
        False
    """
    # Check input type
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    # Negative numbers are not palindromes
    if number < 0:
        return False
    
    # Convert number to string for easy comparison
    str_num = str(number)
    
    # Check if the number reads the same backward and forward
    return str_num == str_num[::-1]