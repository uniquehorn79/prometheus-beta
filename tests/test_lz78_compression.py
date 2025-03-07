import pytest
from src.lz78_compression import lz78_compress, lz78_decompress

def test_lz78_basic_compression():
    """Test basic compression and decompression."""
    original = "TOBEORNOTTOBEORTOBEORNOT"
    compressed = lz78_compress(original)
    decompressed = lz78_decompress(compressed)
    assert decompressed == original

def test_lz78_empty_string():
    """Test compression and decompression of an empty string."""
    original = ""
    compressed = lz78_compress(original)
    assert compressed == []
    
    decompressed = lz78_decompress(compressed)
    assert decompressed == ""

def test_lz78_single_character():
    """Test compression and decompression of a single character."""
    original = "A"
    compressed = lz78_compress(original)
    decompressed = lz78_decompress(compressed)
    assert decompressed == original

def test_lz78_repeated_pattern():
    """Test compression of a string with repeated patterns."""
    original = "ABABABABAB"
    compressed = lz78_compress(original)
    decompressed = lz78_decompress(compressed)
    assert decompressed == original

def test_lz78_complex_string():
    """Test compression of a more complex string."""
    original = "MISSISSIPPI"
    compressed = lz78_compress(original)
    decompressed = lz78_decompress(compressed)
    assert decompressed == original

def test_lz78_invalid_input_type():
    """Test handling of invalid input type for compression."""
    with pytest.raises(TypeError):
        lz78_compress(123)
    
    with pytest.raises(TypeError):
        lz78_decompress(123)

def test_lz78_compression_invalid_decompression_data():
    """Test handling of invalid compressed data."""
    with pytest.raises(ValueError):
        lz78_decompress([(0, 'A'), (2, 'B')])  # Invalid index
    
    with pytest.raises(ValueError):
        lz78_decompress([(0, 'A'), 'invalid'])  # Invalid tuple

def test_lz78_large_input():
    """Test handling of a large input string."""
    original = "A" * 1000
    compressed = lz78_compress(original)
    decompressed = lz78_decompress(compressed)
    assert decompressed == original