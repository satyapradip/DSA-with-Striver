# 📘 Graphs (BFS/DFS) — Medium 01
# Topic: Grid/Connected Components — Number of Islands
# Approach: DFS or BFS on grid
# Time: O(R * C) where R = rows, C = cols | Space: O(R * C)

def num_islands(grid):
    """
    Returns the number of islands in a 2D grid.
    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def dfs(r, c):
        # Boundary check and water check
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0' or (r, c) in visited:
            return

        visited.add((r, c))

        # Explore all 4 directions
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                islands += 1
                dfs(r, c)

    return islands


def num_islands_bfs(grid):
    """
    Alternative using BFS instead of DFS.
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def bfs(r, c):
        queue = deque([(r, c)])
        visited.add((r, c))

        while queue:
            curr_r, curr_c = queue.popleft()

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = curr_r + dr, curr_c + dc
                if (0 <= nr < rows and 0 <= nc < cols and
                    grid[nr][nc] == '1' and (nr, nc) not in visited):
                    visited.add((nr, nc))
                    queue.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                islands += 1
                bfs(r, c)

    return islands


def num_islands_union_find(grid):
    """
    Alternative using Union-Find.
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    parent = {}

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # Path compression
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_x] = root_y

    # Initialize parent for each cell
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                parent[(r, c)] = (r, c)

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols and
                            grid[nr][nc] == '1'):
                        union((r, c), (nr, nc))

    # Count unique roots
    roots = set()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                roots.add(find((r, c)))

    return len(roots)


if __name__ == "__main__":
    import unittest

    class TestNumberOfIslands(unittest.TestCase):
        def test_basic(self):
            grid = [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"]
            ]
            self.assertEqual(num_islands(grid), 1)

        def test_multiple_islands(self):
            grid = [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"]
            ]
            self.assertEqual(num_islands(grid), 3)

        def test_empty_grid(self):
            self.assertEqual(num_islands([]), 0)

        def test_no_islands(self):
            grid = [
                ["0", "0", "0"],
                ["0", "0", "0"]
            ]
            self.assertEqual(num_islands(grid), 0)

    # Demo
    demo_grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print(f"Grid:")
    for row in demo_grid:
        print(' '.join(row))
    print(f"\nNumber of islands: {num_islands(demo_grid)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
