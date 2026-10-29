# 📘 Recursion — Medium 01
# Topic: Backtracking — N-Queens
# Approach: Backtracking (place queens row by row, backtrack on conflict)
# Time: O(N!) | Space: O(N)
# Note: Classic backtracking problem — place N queens so no two attack each other.

def solve_n_queens(n):
    """
    Returns all distinct solutions to the N-Queens problem.
    Each solution is a board configuration where 'Q' is a queen and '.' is empty.
    """
    def is_safe(board, row, col):
        # Check column
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        # Check upper-left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        # Check upper-right diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True

    def backtrack(row, board, results):
        # Base case: all rows filled
        if row == n:
            results.append([''.join(row_board) for row_board in board])
            return

        # Try placing queen in each column of current row
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                backtrack(row + 1, board, results)
                board[row][col] = '.'  # Backtrack: undo placement

    board = [['.' for _ in range(n)] for _ in range(n)]
    results = []
    backtrack(0, board, results)
    return results


def solve_n_queens_count(n):
    """
    Returns the number of distinct solutions to the N-Queens problem.
    More efficient: only counts, doesn't store all boards.
    """
    def is_safe(board, row, col):
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True

    def backtrack(row):
        if row == n:
            return 1
        count = 0
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                count += backtrack(row + 1)
                board[row][col] = '.'
        return count

    board = [['.' for _ in range(n)] for _ in range(n)]
    return backtrack(0)


if __name__ == "__main__":
    import unittest

    class TestNQueens(unittest.TestCase):
        def test_basic(self):
            solutions = solve_n_queens(4)
            self.assertEqual(len(solutions), 2)

        def test_n_queens_1(self):
            self.assertEqual(solve_n_queens(1), [["Q"]])

        def test_count(self):
            self.assertEqual(solve_n_queens_count(4), 2)

    # Demo
    demo_n = 4
    print(f"N-Queens with n = {demo_n}:")
    solutions = solve_n_queens(demo_n)
    for i, sol in enumerate(solutions):
        print(f"Solution {i + 1}:")
        for row in sol:
            print(row)
    print(f"Total solutions: {len(solutions)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
