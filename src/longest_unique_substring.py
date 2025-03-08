def longest_unique_substring(s: str) -> int:
    """
    Find the length of the longest substring with no repeated characters.
    
    Args:
        s (str): Input string to analyze
    
    Returns:
        int: Length of the longest substring with unique characters
    
    Time Complexity: O(n), where n is the length of the input string
    Space Complexity: O(min(m, n)), where m is the size of the character set
    
    Examples:
        >>> longest_unique_substring("abcabcbb")
        3
        >>> longest_unique_substring("bbbbb")
        1
        >>> longest_unique_substring("pwwkew")
        3
        >>> longest_unique_substring("")
        0
    """
    # Handle empty string case
    if not s:
        return 0
    
    # Use sliding window technique
    char_index = {}  # Store the most recent index of each character
    max_length = 0
    start = 0
    
    for end, char in enumerate(s):
        # If character is already seen and its last position is after or at the start of current window
        if char in char_index and char_index[char] >= start:
            # Move the start of the window to the next position after the last occurrence
            start = char_index[char] + 1
        
        # Update the most recent index of the current character
        char_index[char] = end
        
        # Update max length if current window is longer
        max_length = max(max_length, end - start + 1)
    
    return max_length