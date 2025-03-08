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
    
    # Precompute common keys to enable efficient dot product calculation
    matrix2_cols = {}
    for row_idx, row_dict in matrix2.items():
        for col_idx, val in row_dict.items():
            if col_idx not in matrix2_cols:
                matrix2_cols[col_idx] = {}
            matrix2_cols[col_idx][row_idx] = val
    
    # Perform multiplication
    result = {}
    # Iterate through each row of matrix1
    for row_idx, row_dict in matrix1.items():
        # Initialize result row
        result_row = {}
        
        # Iterate through columns of matrix2
        for col_idx in matrix2_cols:
            # Perform dot product
            dot_product = sum(
                row_dict.get(k, 0) * matrix2_cols[col_idx].get(k, 0)
                for k in (set(row_dict) & set(matrix2_cols[col_idx]))
            )
            
            # Store only non-zero results
            if dot_product != 0:
                result_row[col_idx] = dot_product
        
        # Add non-empty rows to result
        if result_row:
            result[row_idx] = result_row
    
    return result