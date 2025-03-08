import pytest
from src.sparse_matrix_multiply import sparse_matrix_multiply

def test_basic_multiplication():
    # Basic multiplication of 2x2 sparse matrices
    matrix1 = {
        0: {0: 1, 1: 2},
        1: {0: 3, 1: 4}
    }
    matrix2 = {
        0: {0: 5, 1: 6},
        1: {0: 7, 1: 8}
    }
    
    expected = {
        0: {0: 19, 1: 22},
        1: {0: 43, 1: 50}
    }
    
    assert sparse_matrix_multiply(matrix1, matrix2) == expected

def test_sparse_matrix_multiplication():
    # Sparse matrix with some zero rows/columns
    matrix1 = {
        0: {1: 3},
        2: {0: 2, 1: 4}
    }
    matrix2 = {
        1: {0: 5, 2: 7},
        2: {1: 6}
    }
    
    expected = {
        0: {2: 21},
        2: {0: 10, 1: 24}
    }
    
    assert sparse_matrix_multiply(matrix1, matrix2) == expected

def test_empty_matrices():
    # Test multiplication with empty matrices
    assert sparse_matrix_multiply({}, {}) == {}
    assert sparse_matrix_multiply({0: {}}, {0: {}}) == {}

def test_invalid_input():
    # Test invalid input types
    with pytest.raises(ValueError):
        sparse_matrix_multiply([], [])
    with pytest.raises(ValueError):
        sparse_matrix_multiply(None, None)

def test_non_overlapping_matrices():
    # Matrices with no common indices should result in empty matrix
    matrix1 = {0: {2: 3}}
    matrix2 = {1: {0: 5}}
    
    assert sparse_matrix_multiply(matrix1, matrix2) == {}

def test_large_sparse_matrix():
    # Test with a larger sparse matrix
    matrix1 = {
        0: {1: 1, 3: 2},
        1: {2: 3},
        3: {0: 4, 2: 5}
    }
    matrix2 = {
        1: {0: 1, 3: 2},
        2: {1: 3},
        3: {2: 4}
    }
    
    expected = {
        0: {0: 1, 3: 4},
        1: {1: 9},
        3: {0: 4, 1: 6, 2: 20}
    }
    
    assert sparse_matrix_multiply(matrix1, matrix2) == expected