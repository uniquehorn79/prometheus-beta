import pytest
from src.word_validator import Queue, is_word_valid

def test_queue_basic_operations():
    """Test basic Queue operations."""
    q = Queue()
    assert q.is_empty() == True
    
    q.enqueue(1)
    assert q.size() == 1
    assert q.peek() == 1
    
    item = q.dequeue()
    assert item == 1
    assert q.is_empty() == True

def test_queue_error_handling():
    """Test error handling in Queue operations."""
    q = Queue()
    
    with pytest.raises(IndexError):
        q.dequeue()
    
    with pytest.raises(IndexError):
        q.peek()

def test_word_valid_min_length():
    """Test word validation with minimum length rule."""
    assert is_word_valid("hello", [{'min_length': 3}]) == True
    assert is_word_valid("hi", [{'min_length': 3}]) == False

def test_word_valid_max_length():
    """Test word validation with maximum length rule."""
    assert is_word_valid("hello", [{'max_length': 5}]) == True
    assert is_word_valid("helloworld", [{'max_length': 5}]) == False

def test_word_valid_contains_digit():
    """Test word validation with contains digit rule."""
    assert is_word_valid("abc123", ['contains_digit']) == True
    assert is_word_valid("abcdef", ['contains_digit']) == False

def test_word_valid_contains_uppercase():
    """Test word validation with contains uppercase rule."""
    assert is_word_valid("AbcDef", ['contains_uppercase']) == True
    assert is_word_valid("abcdef", ['contains_uppercase']) == False

def test_word_valid_contains_special_char():
    """Test word validation with contains special character rule."""
    assert is_word_valid("hello!", ['contains_special_char']) == True
    assert is_word_valid("hello", ['contains_special_char']) == False

def test_word_valid_starts_with():
    """Test word validation with starts with rule."""
    assert is_word_valid("hello", [{'starts_with': 'h'}]) == True
    assert is_word_valid("world", [{'starts_with': 'h'}]) == False

def test_word_valid_ends_with():
    """Test word validation with ends with rule."""
    assert is_word_valid("hello", [{'ends_with': 'o'}]) == True
    assert is_word_valid("world", [{'ends_with': 'o'}]) == False

def test_word_valid_multiple_rules():
    """Test word validation with multiple rules."""
    rules = [
        {'min_length': 5},
        {'max_length': 10},
        'contains_digit',
        'contains_uppercase',
        {'starts_with': 'a'}
    ]
    assert is_word_valid("abc123XYZ", rules) == True
    assert is_word_valid("abc", rules) == False

def test_word_valid_invalid_input():
    """Test word validation with invalid input."""
    assert is_word_valid(123, []) == False
    assert is_word_valid(None, []) == False
    assert is_word_valid("", []) == True  # Empty string is valid if no rules