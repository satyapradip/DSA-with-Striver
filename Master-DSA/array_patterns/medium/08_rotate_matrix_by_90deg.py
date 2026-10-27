# 📘 Array Patterns — Medium 08
# Topic: Matrix Patterns — Rotate Matrix by 90 Degrees
# Approach: Transpose + Reverse rows (in-place, O(1) space)
# Time: O(n^2) | Space: O(1)

def rotate_matrix_90_degrees(matrix):
    """
    Rotates an n x n matrix by 90 degrees clockwise (in-place).
    Step 1: Transpose (swap matrix[i][j] with matrix[j][i])
    Step 2: Reverse each row
    """
    n = len(matrix)
    if n == 0:
        return matrix

    # Step 1: Transpose
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()

    return matrix


def rotate_matrix_90_degrees_brute(matrix):
    """
    Brute force: create new matrix, fill rotated position.
    """
    n = len(matrix)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n - 1 - i] = matrix[i][j]
    return result


if __name__ == "__main__":
    import unittest

    class TestRotateMatrix(unittest.TestCase):
        def test_basic(self):
            matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            expected = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
            rotate_matrix_90_degrees(matrix)
            self.assertEqual(matrix, expected)

        def test_single(self):
            matrix = [[1]]
            rotate_matrix_90_degrees(matrix)
            self.assertEqual(matrix, [[1]])

    # Demo
    demo = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Input:")
    for row in demo:
        print(row)
    rotate_matrix_90_degrees(demo)
    print("Rotated by 90°:")
    for row in demo:
        print(row)
    print("Running unit tests...")
    unittest.main(verbosity=0)
