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
    
    # Compute multiplication 
    result = {}
    # Track which rows appear in matrix2
    matrix2_row_keys = set(matrix2.keys())
    
    # Iterate through rows of matrix1
    for row_idx, row_dict in matrix1.items():
        row_result = {}
        
        # For each non-zero column in this row of matrix1
        for col_1, val_1 in row_dict.items():
            # Check if this column is a row in matrix2
            if col_1 in matrix2_row_keys:
                # Multiply with each column of that row in matrix2
                for col_2, val_2 in matrix2[col_1].items():
                    prod = val_1 * val_2
                    row_result[col_2] = row_result.get(col_2, 0) + prod
        
        # Keep only non-zero results
        row_result = {k: v for k, v in row_result.items() if v != 0}
        
        # Add non-empty rows to result
        if row_result:
            result[row_idx] = row_result
    
    return result