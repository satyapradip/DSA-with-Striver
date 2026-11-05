# 📘 Graphs (BFS/DFS) — Hard 02
# Topic: Grid/BFS — Shortest Bridge
# Approach: 1. Find one island with BFS. 2. BFS from island to find shortest path to second island.
# Time: O(M * N) | Space: O(M * N)

from collections import deque

def shortest_bridge(grid):
    """
    Given a 2D grid consisting of 0s (water) and 1s (land),
    find the shortest bridge (minimum number of 0s to flip to 1s)
    to connect two separate islands.

    Algorithm:
    1. Find the first island using BFS (without modifying the grid)
    2. Record all cells of the first island
    3. BFS from the first island's cells, expanding into water cells
    4. When hitting a cell with 1 (second island, not in first island), return the distance
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])

    # Step 1: Find the first island (without modifying the grid)
    first_island = []
    found = False

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # BFS to find all connected 1s
                island = []
                queue = [(r, c)]

                while queue:
                    curr_r, curr_c = queue.pop(0)
                    if (curr_r, curr_c) not in island:
                        island.append((curr_r, curr_c))
                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nr, nc = curr_r + dr, curr_c + dc
                            if (0 <= nr < rows and 0 <= nc < cols and
                                    grid[nr][nc] == 1 and (nr, nc) not in island):
                                queue.append((nr, nc))

                first_island = island
                found = True
                break
        if found:
            break

    if not first_island:
        return 0

    # Convert first_island to a set for O(1) lookups
    first_island_set = set(first_island)

    # Step 2: BFS from the first island to find shortest path to second island
    # Queue: (row, col, distance)
    queue = deque([(r, c, 0) for r, c in first_island])
    visited = set((r, c) for r, c in first_island)

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        r, c, dist = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == 1 and (nr, nc) not in first_island_set:
                    # Found the second island (not part of the first island)!
                    return dist
                elif grid[nr][nc] == 0 and (nr, nc) not in visited:
                    # This is water, mark it and continue BFS
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))

    return -1


if __name__ == "__main__":
    import unittest

    class TestShortestBridge(unittest.TestCase):
        def test_shortest_bridge(self):
            grid = [
                [0, 1],
                [1, 0]
            ]
            # Should be able to connect with 1 flip (diagonal connection)
            # The shortest path is from (0,1) to (1,0) through (0,0) or (1,1)
            # Both are 1 flip away
            result = shortest_bridge(grid)
            self.assertEqual(result, 1)

        def test_bridge_2_flips(self):
            grid = [
                [0, 1, 0],
                [0, 0, 0],
                [0, 0, 1]
            ]
            # Two islands at opposite corners
            # Path: (0,1) -> (1,1) -> (2,2), flip (1,1) only = 1 flip
            result = shortest_bridge(grid)
            self.assertEqual(result, 1)

        def test_adjacent_islands(self):
            grid = [
                [1, 1],
                [0, 1]
            ]
            # One island, no second island
            result = shortest_bridge(grid)
            self.assertEqual(result, 0)

    # Demo
    demo = [
        [0, 1],
        [1, 0]
    ]
    print(f"Grid:")
    for row in demo:
        print(' '.join(map(str, row)))
    print(f"\nShortest bridge (flips needed): {shortest_bridge(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)