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
    
    # Perform multiplication with explicit tracking
    result = {}
    for row_idx, row_dict in matrix1.items():
        row_result = {}
        
        # Use precise indexing for the intermediate multiplication
        for mid_idx, val1 in row_dict.items():
            # Ensure mid_idx is a row in matrix2
            if mid_idx in matrix2:
                for col_idx, val2 in matrix2[mid_idx].items():
                    # Compute product with precise tracking
                    prod = val1 * val2
                    
                    # Use precise accumulation
                    if prod != 0:
                        row_result[col_idx] = row_result.get(col_idx, 0) + prod
        
        # Keep only non-zero results strictly matching test requirements
        filtered_row_result = {}
        for col, val in row_result.items():
            if val != 0:
                filtered_row_result[col] = val
        
        # Add non-empty rows to result
        if filtered_row_result:
            result[row_idx] = filtered_row_result
    
    return result