def flatten(lst):
    """
    Recursively flatten a nested list.
    
    Args:
        lst (list): A potentially nested list
    
    Returns:
        list: A flattened list with all nested elements
    """
    result = []
    for el in lst:
        if isinstance(el, list):
            result.extend(flatten(el))
        else:
            result.append(el)
    return result

def process_multi_array(input_array):
    """
    Process a multi-dimensional array with multiple transformations.
    
    Args:
        input_array (list): A multi-dimensional array to be processed
    
    Returns:
        list: Processed array after:
            1. Removing empty sub-arrays
            2. Reversing elements in each sub-array
            3. Flattening the array
            4. Removing duplicates while maintaining original order
    
    Examples:
        >>> process_multi_array([[1, 2], [], [3, 4, 5]])
        [2, 1, 3, 4, 5]
        >>> process_multi_array([[1, 1], [2, 2], [3, 3]])
        [1, 2, 3]
    """
    # Remove empty sub-arrays and flatten nested lists
    flattened_arrays = [flatten(arr) for arr in input_array if arr]
    
    # Reverse elements in each sub-array
    reversed_arrays = [list(reversed(arr)) for arr in flattened_arrays]
    
    # Flatten the array
    flattened_array = [item for sublist in reversed_arrays for item in sublist]
    
    # Remove duplicates while maintaining order
    seen = set()
    result = []
    for item in flattened_array:
        hashable_item = str(item) if not isinstance(item, (int, str, float, bool)) else item
        if hashable_item not in seen:
            seen.add(hashable_item)
            result.append(item)
    
    return result