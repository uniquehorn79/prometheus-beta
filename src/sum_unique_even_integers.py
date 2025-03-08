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
    
    # Create a list of even numbers
    even_numbers = [num for num in numbers if num % 2 == 0]
    
    # Find which even numbers appear only once
    unique_evens = []
    for num in even_numbers:
        # If the first index differs from the last index,
        # the number appears more than once 
        if even_numbers.index(num) == even_numbers.rindex(num):
            unique_evens.append(num)
    
    # Return sum of unique even numbers
    return sum(unique_evens)