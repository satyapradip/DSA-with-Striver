# 📘 Graphs (BFS/DFS) — Easy 01
# Topic: Graph Basic — Breadth-First Search (BFS)
# Approach: Queue-based traversal
# Time: O(V + E) | Space: O(V)

from collections import deque

def bfs(graph, start):
    """
    Performs BFS traversal on a graph and returns the order of visited nodes.
    """
    visited = set()
    queue = deque([start])
    visited.add(start)
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


def bfs_shortest_path(graph, start, target):
    """
    Finds the shortest path (in number of edges) from start to target.
    Returns the path as a list, or None if target is unreachable.
    """
    if start == target:
        return [start]

    visited = set([start])
    queue = deque([(start, [start])])  # (node, path)

    while queue:
        node, path = queue.popleft()

        for neighbor in graph.get(node, []):
            if neighbor == target:
                return path + [neighbor]
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None  # Target not reachable


if __name__ == "__main__":
    import unittest

    class TestBFS(unittest.TestCase):
        def setUp(self):
            #       A
            #      / \
            #     B   C
            #    / \   \
            #   D   E   F
            self.graph = {
                'A': ['B', 'C'],
                'B': ['A', 'D', 'E'],
                'C': ['A', 'F'],
                'D': ['B'],
                'E': ['B'],
                'F': ['C']
            }

        def test_bfs(self):
            result = bfs(self.graph, 'A')
            self.assertEqual(result, ['A', 'B', 'C', 'D', 'E', 'F'])

        def test_shortest_path(self):
            self.assertEqual(bfs_shortest_path(self.graph, 'A', 'F'),
                             ['A', 'C', 'F'])

        def test_shortest_path_no_path(self):
            self.assertIsNone(bfs_shortest_path(self.graph, 'A', 'Z'))

        def test_shortest_path_to_self(self):
            self.assertEqual(bfs_shortest_path(self.graph, 'A', 'A'), ['A'])

    # Demo
    demo = self.graph if 'self' in dir() else {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B'],
        'F': ['C']
    }
    print(f"Graph: {demo}")
    print(f"BFS from 'A': {bfs(demo, 'A')}")
    print(f"Shortest path from 'A' to 'F': {bfs_shortest_path(demo, 'A', 'F')}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
