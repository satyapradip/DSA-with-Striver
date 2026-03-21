# Brute forse solution, time complexity=O(n × m × (n + m)) , space complexity = O(k) (k = number of zeros),
def set_matrix_zeros(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    zero_positions = []

    # Step 1: Find all zero positions
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_positions.append((i, j))

    # Step 2: Mark rows and columns
    for i, j in zero_positions:
        # mark row
        for col in range(cols):
            matrix[i][col] = 0

        # mark column
        for row in range(rows):
            matrix[row][j] = 0

    return matrix

if __name__ == "__main__":
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print(set_matrix_zeros(matrix))


# Better Solution, time complexity = O(n × m), space complexity = O(n + m) (for row and col arrays)
def set_matrix_zeros_better(matrix):
    n = len(matrix)  # number of rows
    m = len(matrix[0]) # number of columns
#    Create two arrays to keep track of rows and columns that need to be set to zero 
    row = [0] * n
    col = [0] * m
#   Traverse the matrix to find all the zeros and mark the corresponding rows and columns in the row and col arrays
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0: 
                row[i] = 1
                col[j] = 1
# Traverse the matrix again and set the elements to zero if their corresponding row or column is marked in the row or col arrays
    for i in range(n):
        for j in range(m):
            if row[i] == 1 or col[j] == 1:
                matrix[i][j] = 0

    return matrix

if __name__ == "__main__":    
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print(set_matrix_zeros_better(matrix))


# Optimal Solution, time complexity = O(n × m), space complexity = O(1) (using the first row and first column of the matrix itself to keep track of rows and columns that need to be set to zero)
def set_matrix_zeros_optimal(matrix):
    n = len(matrix)  # number of rows
    m = len(matrix[0]) # number of columns
    col0 = 1
    # Traverse the matrix to find all the zeros and mark the corresponding rows and columns in the first row and first column of the matrix
    for i in range(n):
        if matrix[i][0] == 0:
            col0 = 0
        for j in range(1, m):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

# Traverse the matrix again and set the elements to zero if their corresponding row or column is marked in the first row or first column of the matrix
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
# Finally, check if the first row and first column need to be set to zero based on the markers in the first row and first column of the matrix
    if matrix[0][0] == 0:
        for j in range(m):
            matrix[0][j] = 0
# Check if the first column needs to be set to zero based on the col0 variable
    if col0 == 0:
        for i in range(n):
            matrix[i][0] = 0

    return matrix

if __name__ == "__main__":
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print(set_matrix_zeros_optimal(matrix))

