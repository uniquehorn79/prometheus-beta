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
    
    # Create a full list of even numbers 
    even_numbers = [num for num in numbers if num % 2 == 0]
    
    # Find unique and repeated even numbers
    unique_evens = []
    repeated_evens = set()
    
    for num in even_numbers:
        if num in unique_evens:
            unique_evens.remove(num)
            repeated_evens.add(num)
        elif num not in repeated_evens:
            unique_evens.append(num)
    
    # Sum unique even numbers
    return sum(unique_evens)