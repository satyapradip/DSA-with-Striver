# 📘 Graphs (BFS/DFS) — Hard 01
# Topic: Grid/BFS — Pacific Atlantic Water Flow
# Approach: Reverse BFS from both oceans
# Time: O(M * N) | Space: O(M * N)

from collections import deque

def pacific_atlantic_water_flow(matrix):
    """
    Returns a list of coordinates where water can flow to both Pacific and Atlantic oceans.
    Pacific Ocean touches the TOP and LEFT edges.
    Atlantic Ocean touches the BOTTOM and RIGHT edges.
    Water can only flow to adjacent cells with equal or lower height.
    """
    if not matrix or not matrix[0]:
        return []

    rows, cols = len(matrix), len(matrix[0])

    # visited_pacific[row][col] = True if water can reach Pacific
    pacific = [[False] * cols for _ in range(rows)]
    # visited_atlantic[row][col] = True if water can reach Atlantic
    atlantic = [[False] * cols for _ in range(rows)]

    # Initialize queue with cells on Pacific edges
    pacific_queue = deque()
    for r in range(rows):
        pacific[r][0] = True
        pacific_queue.append((r, 0))
    for c in range(cols):
        pacific[0][c] = True
        pacific_queue.append((0, c))

    # Initialize queue with cells on Atlantic edges
    atlantic_queue = deque()
    for r in range(rows):
        atlantic[r][cols - 1] = True
        atlantic_queue.append((r, cols - 1))
    for c in range(cols):
        atlantic[rows - 1][c] = True
        atlantic_queue.append((rows - 1, c))

    def bfs(queue, visited):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols and
                    not visited[nr][nc] and
                    matrix[nr][nc] >= matrix[r][c]):  # Water can flow to lower/equal height
                    visited[nr][nc] = True
                    queue.append((nr, nc))

    bfs(pacific_queue, pacific)
    bfs(atlantic_queue, atlantic)

    # Find cells that can reach both oceans
    result = []
    for r in range(rows):
        for c in range(cols):
            if pacific[r][c] and atlantic[r][c]:
                result.append([r, c])

    return result


# Alternative: BFS from both oceans (same logic but with separate queues)
def pacific_atlantic_water_flow_v2(matrix):
    """
    Similar to above but with slightly different implementation.
    """
    if not matrix or not matrix[0]:
        return []

    rows, cols = len(matrix), len(matrix[0])

    def bfs(start_queue, visited):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while start_queue:
            r, c = start_queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols and
                    not visited[nr][nc] and
                    matrix[nr][nc] >= matrix[r][c]):
                    visited[nr][nc] = True
                    start_queue.append((nr, nc))

    # Pacific edges (top and left)
    pacific_queue = deque()
    for r in range(rows):
        pacific_queue.append((r, 0))
    for c in range(cols):
        pacific_queue.append((0, c))

    # Atlantic edges (bottom and right)
    atlantic_queue = deque()
    for r in range(rows):
        atlantic_queue.append((r, cols - 1))
    for c in range(cols):
        atlantic_queue.append((rows - 1, c))

    # Mark all edge cells as reachable
    pacific = [[False] * cols for _ in range(rows)]
    atlantic = [[False] * cols for _ in range(rows)]

    for r in range(rows):
        pacific[r][0] = True
    for c in range(cols):
        pacific[0][c] = True

    for r in range(rows):
        atlantic[r][cols - 1] = True
    for c in range(cols):
        atlantic[rows - 1][c] = True

    # Process both oceans
    bfs(pacific_queue, pacific)
    bfs(atlantic_queue, atlantic)

    # Find intersection
    result = []
    for r in range(rows):
        for c in range(cols):
            if pacific[r][c] and atlantic[r][c]:
                result.append([r, c])

    return result


if __name__ == "__main__":
    import unittest

    class TestPacificAtlantic(unittest.TestCase):
        def test_water_flow(self):
            matrix = [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ]
            result = pacific_atlantic_water_flow(matrix)
            # Expected: [[0,2],[1,2],[2,0],[2,1],[2,2]]
            self.assertEqual(len(result), 5)

        def test_single_element(self):
            matrix = [[1]]
            result = pacific_atlantic_water_flow(matrix)
            self.assertEqual(result, [[0, 0]])

    # Demo
    demo = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(f"Water flow matrix:")
    for row in demo:
        print(' '.join(map(str, row)))
    print(f"\nPacific-Atlanic common cells: {pacific_atlantic_water_flow(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)