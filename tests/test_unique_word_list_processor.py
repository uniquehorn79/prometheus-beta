import os
import pytest
from src.unique_word_list_processor import process_word_list

def test_process_word_list_basic(tmp_path):
    # Create a temporary file with sample words
    test_file = tmp_path / "test_words.txt"
    test_file.write_text("apple banana apple cherry banana")
    
    result = process_word_list(str(test_file))
    assert result == ['apple', 'banana', 'cherry']

def test_process_word_list_empty_file(tmp_path):
    # Create an empty file
    test_file = tmp_path / "empty_file.txt"
    test_file.write_text("")
    
    result = process_word_list(str(test_file))
    assert result == []

def test_process_word_list_whitespace_variations(tmp_path):
    # Test various whitespace scenarios
    test_file = tmp_path / "whitespace_test.txt"
    test_file.write_text("  hello   world  hello\nworld  python  ")
    
    result = process_word_list(str(test_file))
    assert result == ['hello', 'python', 'world']

def test_process_word_list_case_sensitive(tmp_path):
    # Ensure case is preserved
    test_file = tmp_path / "case_test.txt"
    test_file.write_text("Apple apple APPLE Banana banana")
    
    result = process_word_list(str(test_file))
    assert result == ['Apple', 'APPLE', 'Banana', 'apple', 'banana']

def test_process_word_list_file_not_found():
    # Test handling of non-existent file
    with pytest.raises(FileNotFoundError):
        process_word_list("non_existent_file.txt")

def test_process_word_list_large_input(tmp_path):
    # Test with a larger input to ensure performance and sorting
    test_file = tmp_path / "large_input.txt"
    test_file.write_text("zebra ant elephant dog cat ant dog giraffe elephant")
    
    result = process_word_list(str(test_file))
    assert result == ['ant', 'cat', 'dog', 'elephant', 'giraffe', 'zebra']