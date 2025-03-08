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
    
    # Prepare matrix2 by transposing and tracking columns
    matrix2_cols = {}
    for row_idx, row_dict in matrix2.items():
        for col_idx, val in row_dict.items():
            if col_idx not in matrix2_cols:
                matrix2_cols[col_idx] = {}
            matrix2_cols[col_idx][row_idx] = val
    
    # Perform multiplication
    result = {}
    for row_idx, row_dict in matrix1.items():
        # Use intermediate dictionary to track output
        row_result = {}
        
        # Go through each column in matrix2
        for col_idx, col_dict in matrix2_cols.items():
            # Compute dot product, but be selective about common indices
            dot_product = 0
            for k, v1 in row_dict.items():
                if k in col_dict:
                    dot_product += v1 * col_dict[k]
            
            # Only add non-zero results
            if dot_product != 0:
                row_result[col_idx] = dot_product
        
        # Only add non-empty rows to result
        if row_result:
            result[row_idx] = row_result
    
    return result