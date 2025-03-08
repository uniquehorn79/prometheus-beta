def sum_unique_even_integers(numbers):
    """
    Calculate the sum of unique even integers in the given array.
    
    Args:
        numbers (list): A list of integers to process
    
    Returns:
        int: Sum of even integers that appear only once in the input list
    
    Raises:
        TypeError: If the input is not a list or contains non-integer elements
    """
    # Validate input type
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers")
    
    # Validate all elements are integers
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements must be integers")
    
    # Collect unique and non-unique even numbers
    unique_evens = []
    non_unique_evens = []
    
    # Count occurrences of even numbers
    for num in numbers:
        if num % 2 == 0:
            # If the number is already in non_unique_evens, skip
            if num in non_unique_evens:
                continue
            # If the number appears more than once, remove from unique and add to non-unique
            if num in unique_evens:
                unique_evens.remove(num)
                non_unique_evens.append(num)
            else:
                unique_evens.append(num)
    
    # Return sum of unique even numbers
    return sum(unique_evens)