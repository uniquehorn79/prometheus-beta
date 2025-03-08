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
    
    # Find unique even numbers
    unique_evens = []
    
    # Iterate and check for each even number
    for num in numbers:
        if num % 2 == 0:
            # Check if this is the first or last occurrence of the number 
            if numbers.count(num) == 1:
                unique_evens.append(num)
    
    # Return the sum of unique even numbers
    return sum(unique_evens)