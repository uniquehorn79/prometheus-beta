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
    
    # Use a list to track unique even numbers
    unique_evens = []
    duplicates = set()
    
    # Iterate through numbers to find unique even numbers
    for num in numbers:
        if num % 2 == 0:
            # If number is already in unique_evens, move it to duplicates
            if num in unique_evens:
                unique_evens.remove(num)
                duplicates.add(num)
            # Only add to unique_evens if not a duplicate
            elif num not in duplicates:
                unique_evens.append(num)
    
    # Return sum of unique even numbers
    return sum(unique_evens)