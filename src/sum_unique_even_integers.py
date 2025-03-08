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
    
    # Filter out repeated even numbers
    even_numbers = [num for num in numbers if num % 2 == 0]
    
    # Sum unique even numbers
    unique_even_sum = sum(num for num in even_numbers 
                           if even_numbers.count(num) == 1)
    
    return unique_even_sum