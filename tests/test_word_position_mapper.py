import pytest
from src.word_position_mapper import map_word_positions

def test_basic_word_position_mapping():
    """Test basic word position mapping"""
    text = "the cat sat on the mat"
    result = map_word_positions(text)
    
    # Check expected output
    assert result == {
        'the': [0, 4],
        'cat': [1],
        'sat': [2],
        'on': [3],
        'mat': [5]
    }

def test_empty_string():
    """Test mapping with an empty string"""
    assert map_word_positions("") == {}

def test_single_word():
    """Test mapping with a single word"""
    result = map_word_positions("hello")
    assert result == {'hello': [0]}

def test_repeated_words():
    """Test mapping with multiple repeated words"""
    text = "apple banana apple cherry banana apple"
    result = map_word_positions(text)
    
    assert result == {
        'apple': [0, 2, 5],
        'banana': [1, 4],
        'cherry': [3]
    }

def test_case_insensitivity():
    """Verify that word mapping is case-insensitive"""
    text = "Hello hello HELLO"
    result = map_word_positions(text)
    
    assert result == {'hello': [0, 1, 2]}

def test_invalid_input_type():
    """Test that TypeError is raised for non-string inputs"""
    with pytest.raises(TypeError, match="Input must be a string"):
        map_word_positions(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        map_word_positions(None)

def test_whitespace_handling():
    """Test handling of extra whitespace"""
    text = "  hello   world  hello  "
    result = map_word_positions(text)
    
    assert result == {
        'hello': [0, 2],
        'world': [1]
    }