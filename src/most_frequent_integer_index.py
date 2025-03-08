from typing import List, Optional

def find_most_frequent_integer_index(nums: List[int]) -> Optional[int]:
    """
    Find the index of the integer with the highest frequency in the list.
    
    In case of a tie, returns the index of the last occurrence of the 
    first-occurring most frequent integer.
    
    Args:
        nums (List[int]): A list of integers to analyze
    
    Returns:
        Optional[int]: Index of the most frequent integer, or None if the list is empty
    
    Examples:
        >>> find_most_frequent_integer_index([1, 2, 3, 3, 1, 1])
        4
        >>> find_most_frequent_integer_index([1, 1, 2, 2, 3])
        0
        >>> find_most_frequent_integer_index([])
        None
    """
    # Handle empty list case
    if not nums:
        return None
    
    # Count frequencies and track last occurrence indices
    frequency = {}
    last_occurrence = {}
    
    for idx, num in enumerate(nums):
        # Update frequency count
        frequency[num] = frequency.get(num, 0) + 1
        
        # Update last occurrence index
        last_occurrence[num] = idx
    
    # Find the maximum frequency
    max_freq = max(frequency.values())
    
    # Find the index of the first occurrence of the most frequent integer
    most_frequent_nums = [num for num, freq in frequency.items() if freq == max_freq]
    
    # Return the last index of first-occurring most frequent number
    return min(last_occurrence[num] for num in most_frequent_nums)