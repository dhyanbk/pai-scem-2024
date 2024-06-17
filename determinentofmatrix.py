def determinant_2x2(matrix):
    if len(matrix) != 2 or len(matrix[0]) != 2:
        raise ValueError("The matrix must be 2x2")
    
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

# Example usage
matrix = [
    [4, 6],
    [3, 8]
]

det = determinant_2x2(matrix)
print("Determinant of the matrix is:", det)