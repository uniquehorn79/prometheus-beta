from typing import List, Tuple, Union

def lz78_compress(input_string: str) -> List[Tuple[int, str]]:
    """
    Implement LZ78 compression algorithm.
    
    Args:
        input_string (str): The input string to be compressed.
    
    Returns:
        List[Tuple[int, str]]: Compressed representation of the input string.
                                Each tuple is (dictionary_index, character).
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If input is an empty string.
    """
    # Input validation
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not input_string:
        raise ValueError("Input string cannot be empty")
    
    # Initialize compression dictionary and output
    dictionary = {0: ''}  # 0 represents empty string
    output = []
    current_dict_index = 1
    
    # Current sequence being matched
    current_sequence = ''
    
    # Compress the input string
    for char in input_string:
        # Try to extend current sequence
        test_sequence = current_sequence + char
        
        # Check if sequence is in dictionary
        found = False
        for index, sequence in dictionary.items():
            if sequence == test_sequence:
                current_sequence = test_sequence
                found = True
                break
        
        # If sequence not found, add to dictionary and output
        if not found:
            # Find the index of the longest matching prefix
            prefix_index = 0
            for index, sequence in dictionary.items():
                if sequence == current_sequence:
                    prefix_index = index
                    break
            
            # Add compressed tuple and update dictionary
            output.append((prefix_index, char))
            dictionary[current_dict_index] = test_sequence
            current_dict_index += 1
            
            # Reset current sequence
            current_sequence = ''
    
    # Handle any remaining sequence
    if current_sequence:
        for index, sequence in dictionary.items():
            if sequence == current_sequence:
                output.append((index, ''))
                break
    
    return output

def lz78_decompress(compressed: List[Tuple[int, str]]) -> str:
    """
    Decompress LZ78 compressed data.
    
    Args:
        compressed (List[Tuple[int, str]]): Compressed representation.
    
    Returns:
        str: Decompressed original string.
    
    Raises:
        TypeError: If input is not a list of tuples.
        ValueError: If compressed data is invalid.
    """
    # Input validation
    if not isinstance(compressed, list):
        raise TypeError("Input must be a list of tuples")
    
    if not compressed:
        return ''
    
    # Validate input tuples
    for item in compressed:
        if not (isinstance(item, tuple) and len(item) == 2 and 
                isinstance(item[0], int) and isinstance(item[1], str)):
            raise ValueError("Invalid compressed data format")
    
    # Initialize dictionary
    dictionary = {0: ''}
    current_dict_index = 1
    
    # Decompression process
    output = []
    for index, char in compressed:
        # Retrieve sequence from dictionary
        if index not in dictionary:
            raise ValueError(f"Invalid dictionary index: {index}")
        
        # Construct current sequence
        current_sequence = dictionary[index] + char
        output.append(current_sequence)
        
        # Add to dictionary
        dictionary[current_dict_index] = current_sequence
        current_dict_index += 1
    
    # Return full decompressed string
    return ''.join(output)