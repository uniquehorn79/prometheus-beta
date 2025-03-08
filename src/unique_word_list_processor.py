def process_word_list(input_file_path):
    """
    Read a text file containing words, remove duplicates, and return a sorted list of unique words.

    Args:
        input_file_path (str): Path to the input text file containing words.

    Returns:
        list: A sorted list of unique words from the input file, preserving first occurrence.

    Raises:
        FileNotFoundError: If the input file does not exist.
        IOError: If there is an error reading the file.
    """
    try:
        # Read file and split into words
        with open(input_file_path, 'r') as file:
            # Split by whitespace, remove leading/trailing whitespace from each word
            words = [word.strip() for word in file.read().split()]

        # Remove duplicates while preserving first occurrence order
        seen = set()
        unique_words = []
        for word in words:
            if word.lower() not in seen:
                seen.add(word.lower())
                unique_words.append(word)

        # Sort the unique words case-insensitively
        return sorted(unique_words, key=str.lower)

    except FileNotFoundError:
        raise FileNotFoundError(f"Input file not found: {input_file_path}")
    except IOError as e:
        raise IOError(f"Error reading file {input_file_path}: {e}")