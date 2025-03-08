class Queue:
    """
    A simple Queue implementation using a list.
    
    Provides basic queue operations: enqueue, dequeue, and peek.
    """
    def __init__(self):
        """Initialize an empty queue."""
        self._items = []
    
    def enqueue(self, item):
        """
        Add an item to the end of the queue.
        
        Args:
            item: The item to be added to the queue.
        """
        self._items.append(item)
    
    def dequeue(self):
        """
        Remove and return the first item from the queue.
        
        Returns:
            The first item in the queue.
        
        Raises:
            IndexError: If the queue is empty.
        """
        if not self._items:
            raise IndexError("Cannot dequeue from an empty queue")
        return self._items.pop(0)
    
    def peek(self):
        """
        Return the first item in the queue without removing it.
        
        Returns:
            The first item in the queue.
        
        Raises:
            IndexError: If the queue is empty.
        """
        if not self._items:
            raise IndexError("Cannot peek an empty queue")
        return self._items[0]
    
    def is_empty(self):
        """
        Check if the queue is empty.
        
        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self._items) == 0
    
    def size(self):
        """
        Get the number of items in the queue.
        
        Returns:
            int: Number of items in the queue.
        """
        return len(self._items)

def is_word_valid(word, rules):
    """
    Determine if a word is valid based on a set of rules.
    
    Args:
        word (str): The word to validate.
        rules (list): A list of validation rules to apply.
    
    Returns:
        bool: True if the word is valid, False otherwise.
    
    Rules can include:
    - 'min_length': Minimum length of the word
    - 'max_length': Maximum length of the word
    - 'contains_digit': Word must contain at least one digit
    - 'contains_uppercase': Word must contain at least one uppercase letter
    - 'contains_special_char': Word must contain at least one special character
    - 'starts_with': Word must start with a specific character
    - 'ends_with': Word must end with a specific character
    """
    if not isinstance(word, str):
        return False
    
    # Create a queue to process the rules
    rule_queue = Queue()
    for rule in rules:
        rule_queue.enqueue(rule)
    
    # Process each rule
    while not rule_queue.is_empty():
        rule = rule_queue.dequeue()
        
        # Minimum length rule
        if isinstance(rule, dict) and 'min_length' in rule:
            if len(word) < rule['min_length']:
                return False
        
        # Maximum length rule
        if isinstance(rule, dict) and 'max_length' in rule:
            if len(word) > rule['max_length']:
                return False
        
        # Contains digit rule
        if rule == 'contains_digit':
            if not any(char.isdigit() for char in word):
                return False
        
        # Contains uppercase rule
        if rule == 'contains_uppercase':
            if not any(char.isupper() for char in word):
                return False
        
        # Contains special character rule
        if rule == 'contains_special_char':
            special_chars = '!@#$%^&*()_+-=[]{}|;:,.<>?'
            if not any(char in special_chars for char in word):
                return False
        
        # Starts with rule
        if isinstance(rule, dict) and 'starts_with' in rule:
            if not word.startswith(rule['starts_with']):
                return False
        
        # Ends with rule
        if isinstance(rule, dict) and 'ends_with' in rule:
            if not word.endswith(rule['ends_with']):
                return False
    
    return True