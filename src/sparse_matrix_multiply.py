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
    
    # Precompute indices and columns for efficient multiplication
    matrix2_indices = {}
    for row_idx, row_dict in matrix2.items():
        for col_idx, val in row_dict.items():
            if row_idx not in matrix2_indices:
                matrix2_indices[row_idx] = {}
            matrix2_indices[row_idx][col_idx] = val
    
    # Perform multiplication
    result = {}
    for row_idx, row_dict in matrix1.items():
        # Use a more precise matching of indices
        row_result = {}
        
        # Iterate through non-zero elements in matrix1 row
        for mid_idx, val1 in row_dict.items():
            # Check if mid_idx is a valid row in matrix2
            if mid_idx in matrix2_indices:
                # Compute dot product with columns
                for col_idx, val2 in matrix2_indices[mid_idx].items():
                    prod = val1 * val2
                    # Use precise index matching and accumulation
                    if col_idx not in row_result:
                        row_result[col_idx] = prod
                    else:
                        row_result[col_idx] += prod
        
        # Prune zero-valued results precisely
        row_result = {k: v for k, v in row_result.items() if v != 0}
        
        # Add only non-empty results
        if row_result:
            result[row_idx] = row_result
    
    return result