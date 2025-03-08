def find_duplicates(numbers):
    """
    Find and return a list of duplicate integers in the input list.

    Args:
        numbers (list): A list of integers to search for duplicates.

    Returns:
        list: A list of integers that appear more than once in the input list.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Validate input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")

    # Validate all elements are integers
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements must be integers")

    # Use a dictionary to track number frequencies
    freq_dict = {}
    duplicates = []

    # Count frequencies
    for num in numbers:
        freq_dict[num] = freq_dict.get(num, 0) + 1

    # Collect numbers that appear more than once
    duplicates = [num for num, count in freq_dict.items() if count > 1]

    return sorted(duplicates)