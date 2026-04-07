#
def rotate_matrix_by_90_degree(matrix):  # O(n^2) time and O(1) space
    n = len(matrix)
    
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
    
    return matrix 


# 
def rotate_matrix_by_90_degree_inplace(matrix):  # O(n^2) time and O(1) space
    n = len(matrix)
    
    # Rotate the matrix layer by layer
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            # Save the top element
            temp = matrix[i][j]
            
            # Move left to top
            matrix[i][j] = matrix[n - j - 1][i]
            
            # Move bottom to left
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            
            # Move right to bottom
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            
            # Move top to right
            matrix[j][n - i - 1] = temp
    
    return matrix