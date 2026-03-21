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


# Better Solution, 

