def map_word_positions(text: str) -> dict:
    """
    Maps unique words in a given text to their positions.

    Args:
        text (str): Input text to analyze

    Returns:
        dict: A dictionary where keys are unique words and values are 
              lists of their positions in the text (0-indexed)

    Raises:
        TypeError: If input is not a string
    """
    # Validate input
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Normalize the text (convert to lowercase and split)
    words = text.lower().split()
    
    # Create a dictionary to store word positions
    word_positions = {}
    
    # Iterate through words and track their positions
    for position, word in enumerate(words):
        # If word not in dictionary, create a new list
        if word not in word_positions:
            word_positions[word] = []
        
        # Append current position to the word's position list
        word_positions[word].append(position)
    
    return word_positions