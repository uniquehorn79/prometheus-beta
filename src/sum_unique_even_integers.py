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
    
    # Find unique even numbers in the input order
    unique_evens = []
    seen = set()
    duplicates = set()
    
    for num in numbers:
        if num % 2 == 0:
            # If number is already a duplicate, skip it
            if num in duplicates:
                continue
            
            # If it's already seen, remove from unique and add to duplicates
            if num in seen:
                unique_evens.remove(num)
                duplicates.add(num)
            else:
                # If it's new, add to seen and unique_evens
                seen.add(num)
                unique_evens.append(num)
    
    # Return sum of unique even numbers
    return sum(unique_evens)