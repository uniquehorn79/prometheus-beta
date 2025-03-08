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
    
    # Compute dimensions and transpose matrix2 for efficient multiplication
    matrix2_transposed = {}
    for row, row_dict in matrix2.items():
        for col, val in row_dict.items():
            if col not in matrix2_transposed:
                matrix2_transposed[col] = {}
            matrix2_transposed[col][row] = val
    
    # Perform multiplication
    result = {}
    for row in matrix1:
        # Skip rows with no non-zero elements
        if not matrix1[row]:
            continue
        
        result[row] = {}
        for col in matrix2_transposed:
            # Compute dot product of row from matrix1 with column from matrix2
            dot_product = sum(
                matrix1[row].get(k, 0) * matrix2_transposed[col].get(k, 0)
                for k in set(matrix1[row]) & set(matrix2_transposed[col])
            )
            
            # Only store non-zero values
            if dot_product != 0:
                result[row][col] = dot_product
        
        # Remove rows with no non-zero elements
        if not result[row]:
            del result[row]
    
    return result