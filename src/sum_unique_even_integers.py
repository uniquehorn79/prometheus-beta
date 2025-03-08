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
    
    # Find unique even numbers using complex logic
    unique_evens = []
    repeated_evens = set()
    
    for num in numbers:
        if num % 2 == 0:
            # If number is already in repeated, skip
            if num in repeated_evens:
                continue
            
            # If number is already in unique_evens, it becomes a repeated number
            if num in unique_evens:
                unique_evens.remove(num)
                repeated_evens.add(num)
            else:
                # Add to unique_evens if not repeated before
                unique_evens.append(num)
    
    return sum(unique_evens)