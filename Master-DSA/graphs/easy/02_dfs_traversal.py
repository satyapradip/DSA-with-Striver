# 📘 Graphs (BFS/DFS) — Easy 02
# Topic: Graph Basic — Depth-First Search (DFS)
# Approach: Recursion-based (or stack-based iterative)
# Time: O(V + E) | Space: O(V)

def dfs_recursive(graph, node, visited=None):
    """
    Performs DFS traversal on a graph using recursion.
    """
    if visited is None:
        visited = set()
    visited.add(node)
    order = [node]

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            order.extend(dfs_recursive(graph, neighbor, visited))

    return order


def dfs_iterative(graph, start):
    """
    Performs DFS traversal using an explicit stack.
    """
    visited = set()
    stack = [start]
    visited.add(start)
    order = []

    while stack:
        node = stack.pop()
        order.append(node)

        # Reverse to maintain same order as recursive version
        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return order


def dfs_paths_recursive(graph, start, end, path=None, visited=None):
    """
    Finds all paths from start to end using DFS.
    """
    if path is None:
        path = []
    if visited is None:
        visited = set()

    path = path + [start]
    visited.add(start)

    if start == end:
        return [path]

    paths = []
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            new_paths = dfs_paths_recursive(graph, neighbor, end, path, visited)
            paths.extend(new_paths)

    return paths


def dfs_paths_iterative(graph, start, end):
    """
    Iterative version to find paths using stack.
    """
    if start == end:
        return [[start]]

    paths = []
    stack = [(start, [start], {start})]

    while stack:
        node, path, visited = stack.pop()

        for neighbor in graph.get(node, []):
            if neighbor == end:
                paths.append(path + [neighbor])
            elif neighbor not in visited:
                stack.append((neighbor, path + [neighbor], visited | {neighbor}))

    return paths


if __name__ == "__main__":
    import unittest

    class TestDFS(unittest.TestCase):
        def setUp(self):
            self.graph = {
                'A': ['B', 'C'],
                'B': ['A', 'D', 'E'],
                'C': ['A', 'F'],
                'D': ['B'],
                'E': ['B', 'F'],
                'F': ['C', 'E']
            }

        def test_dfs_recursive(self):
            result = dfs_recursive(self.graph, 'A')
            self.assertEqual(result, ['A', 'B', 'D', 'E', 'F', 'C'])

        def test_dfs_iterative(self):
            result = dfs_iterative(self.graph, 'A')
            self.assertEqual(result, ['A', 'C', 'F', 'E', 'B', 'D'])

        def test_dfs_paths(self):
            paths = dfs_paths_recursive(self.graph, 'A', 'F')
            self.assertIn(['A', 'C', 'F'], paths)
            self.assertIn(['A', 'B', 'E', 'F'], paths)

    # Demo
    demo = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    print(f"Graph: {demo}")
    print(f"DFS Recursive from 'A': {dfs_recursive(demo, 'A')}")
    print(f"DFS Iterative from 'A': {dfs_iterative(demo, 'A')}")
    print(f"All paths from 'A' to 'F': {dfs_paths_recursive(demo, 'A', 'F')}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
