def find_odd_occurrence(numbers):
    """
    Find the number that appears an odd number of times in the given list using bitwise XOR.
    If multiple such numbers exist, return the smallest one.

    Args:
        numbers (list): A list of integers to search through.

    Returns:
        int: The smallest number that appears an odd number of times.
        
    Raises:
        ValueError: If the input list is empty or no number appears an odd number of times.
    """
    # Handle empty list
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    # Find all numbers with odd occurrences using bitwise XOR
    odd_occurrence_numbers = set()
    
    # Use a dictionary to track the count of each number
    count_dict = {}
    for num in numbers:
        count_dict[num] = count_dict.get(num, 0) + 1
    
    # Find numbers with odd occurrences
    for num, count in count_dict.items():
        if count % 2 != 0:
            odd_occurrence_numbers.add(num)
    
    # Handle no odd occurrence numbers
    if not odd_occurrence_numbers:
        raise ValueError("No number appears an odd number of times")
    
    # Return the smallest number with odd occurrences
    return min(odd_occurrence_numbers)