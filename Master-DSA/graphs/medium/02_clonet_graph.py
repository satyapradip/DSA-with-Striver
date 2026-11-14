# 📘 Graphs (BFS/DFS) — Medium 02
# Topic: Graph Representation — Clone Graph
# Approach: DFS or BFS with node mapping
# Time: O(V + E) | Space: O(V)

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        return f"Node({self.val})"


def clone_graph_dfs(node):
    """
    Clones a connected undirected graph using DFS.
    """
    if not node:
        return None

    old_to_new = {}

    def clone(node):
        # If already cloned, return the clone
        if node in old_to_new:
            return old_to_new[node]

        # Create clone
        clone_node = Node(node.val)
        old_to_new[node] = clone_node

        # Clone all neighbors
        for neighbor in node.neighbors:
            clone_node.neighbors.append(clone(neighbor))

        return clone_node

    return clone(node)


def clone_graph_bfs(node):
    """
    Clones a connected undirected graph using BFS.
    """
    if not node:
        return None

    old_to_new = {node: Node(node.val)}
    queue = deque([node])

    while queue:
        current = queue.popleft()

        for neighbor in current.neighbors:
            if neighbor not in old_to_new:
                old_to_new[neighbor] = Node(neighbor.val)
                queue.append(neighbor)

            # Add neighbor to current clone's neighbors
            old_to_new[current].neighbors.append(old_to_new[neighbor])

    return old_to_new[node]


def clone_graph_brute(node):
    """
    Brute force: DFS with explicit stack and mapping.
    """
    if not node:
        return None

    old_to_new = {node: Node(node.val)}
    stack = [node]

    while stack:
        current = stack.pop()

        for neighbor in current.neighbors:
            if neighbor not in old_to_new:
                old_to_new[neighbor] = Node(neighbor.val)
                stack.append(neighbor)

            old_to_new[current].neighbors.append(old_to_new[neighbor])

    return old_to_new[node]


def print_graph(node):
    """Helper to print graph structure."""
    if not node:
        return "None"
    visited = set()
    result = []
    queue = [node]
    visited.add(node)

    while queue:
        current = queue.pop(0)
        result.append(f"Node({current.val}) ->")
        for neighbor in current.neighbors:
            result.append(f"  -> {neighbor.val}")
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return ' '.join(result)


if __name__ == "__main__":
    import unittest

    class TestCloneGraph(unittest.TestCase):
        def test_clone_graph(self):
            # Build graph: 1 - 2, 2 - 3, 3 - 4, 4 - 1
            node1 = Node(1)
            node2 = Node(2)
            node3 = Node(3)
            node4 = Node(4)
            node1.neighbors = [node2, node4]
            node2.neighbors = [node1, node3]
            node3.neighbors = [node2, node4]
            node4.neighbors = [node3, node1]

            cloned = clone_graph_dfs(node1)

            self.assertEqual(cloned.val, 1)
            self.assertEqual(len(cloned.neighbors), 2)
            self.assertEqual(cloned.neighbors[0].val, 2)
            self.assertEqual(cloned.neighbors[1].val, 4)

    # Demo
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node3, node1]

    print("Original graph:")
    print(print_graph(node1))
    print()

    cloned = clone_graph_dfs(node1)
    print("Cloned graph:")
    print(print_graph(cloned))
    print("Running unit tests...")
    unittest.main(verbosity=0)
