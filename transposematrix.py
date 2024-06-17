def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = transpose_matrix(matrix)
print("Original matrix:")
for row in matrix:
    print(row)

print("\nTransposed matrix:")
for row in transposed:
    print(row)