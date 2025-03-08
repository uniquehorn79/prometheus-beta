def sparse_matrix_multiply(matrix1, matrix2):
    """
    Perform sparse matrix multiplication using dictionary representation.
    
    Args:
        matrix1 (dict): First sparse matrix represented as {row_index: {col_index: value}}
        matrix2 (dict): Second sparse matrix represented as {row_index: {col_index: value}}
    
    Returns:
        dict: Resulting sparse matrix after multiplication
    
    Raises:
        ValueError: If matrices cannot be multiplied (incompatible dimensions)
    """
    # Validate input matrices are dictionaries
    if not isinstance(matrix1, dict) or not isinstance(matrix2, dict):
        raise ValueError("Inputs must be dictionaries representing sparse matrices")
    
    # Check if multiplication is possible
    if not matrix1 or not matrix2:
        return {}
    
    # Perform multiplication
    result = {}
    for row_idx, row_dict in matrix1.items():
        row_result = {}
        
        # Go through each non-zero element in the row
        for mid_idx, val1 in row_dict.items():
            # Check if this index exists in matrix2
            if mid_idx in matrix2:
                # Go through columns in the corresponding row of matrix2
                for col_idx, val2 in matrix2[mid_idx].items():
                    # Compute precise product
                    prod = val1 * val2
                    
                    # Accumulate results with precise indexing
                    if col_idx not in row_result:
                        row_result[col_idx] = prod
                    else:
                        row_result[col_idx] += prod
        
        # Prune zero results
        row_result = {k: v for k, v in row_result.items() if v != 0}
        
        # Add non-empty rows to result
        if row_result:
            result[row_idx] = row_result
    
    return result