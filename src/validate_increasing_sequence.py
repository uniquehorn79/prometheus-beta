def is_valid_increasing_sequence(arr):
    """
    Check if the given array is a valid sequence with distinct integers in strictly increasing order.
    
    Args:
        arr (list): Input list of integers to validate
    
    Returns:
        bool: True if the array is a valid strictly increasing sequence of distinct integers, False otherwise
    
    Raises:
        TypeError: If input is not a list
    
    Examples:
        >>> is_valid_increasing_sequence([1, 2, 3, 4, 5])
        True
        >>> is_valid_increasing_sequence([1, 1, 2, 3])
        False
        >>> is_valid_increasing_sequence([5, 4, 3, 2, 1])
        False
        >>> is_valid_increasing_sequence([])
        True
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Empty list is considered a valid sequence
    if len(arr) <= 1:
        return True
    
    # Check for distinct integers in strictly increasing order
    for i in range(1, len(arr)):
        # Ensure each element is an integer
        if not isinstance(arr[i], int):
            return False
        
        # Check for strict increase and distinctness
        if arr[i] <= arr[i-1]:
            return False
    
    return True