# 📘 Trees (BST) — Medium 02
# Topic: Tree Level Order Traversal (BFS)
# Approach: Breadth-First Search using a queue
# Time: O(n) | Space: O(w) where w = max width of tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_sample_tree():
    #       3
    #      / \
    #     9  20
    #        / \
    #       15  7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    return root


def level_order(root):
    """
    Returns level order traversal of the binary tree.
    Each level is a separate list in the result.
    """
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

    return result


def level_order_bottom(root):
    """
    Returns level order traversal from bottom to top.
    """
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.insert(0, level)
    return result


def level_order_brute(root):
    """
    Alternative: uses a helper function with depth tracking.
    """
    result = []

    def dfs(node, depth):
        if not node:
            return
        # If this is the first node at this depth, create a new level
        if depth == len(result):
            result.append([])
        result[depth].append(node.val)
        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)

    dfs(root, 0)
    return result


if __name__ == "__main__":
    import unittest

    class TestLevelOrder(unittest.TestCase):
        def setUp(self):
            #       3
            #      / \
            #     9  20
            #        / \
            #       15  7
            self.root = TreeNode(3)
            self.root.left = TreeNode(9)
            self.root.right = TreeNode(20)
            self.root.right.left = TreeNode(15)
            self.root.right.right = TreeNode(7)

        def test_level_order(self):
            result = level_order(self.root)
            self.assertEqual(result, [[3], [9, 20], [15, 7]])

        def test_level_order_bottom(self):
            result = level_order_bottom(self.root)
            self.assertEqual(result, [[15, 7], [9, 20], [3]])

        def test_level_order_single_node(self):
            root = TreeNode(1)
            self.assertEqual(level_order(root), [[1]])

        def test_level_order_empty(self):
            self.assertEqual(level_order(None), [])

    # Demo
    demo = create_sample_tree()
    print(f"Tree:       {demo.val}")
    print(f"           /    \\")
    print(f"          {demo.left.val}    {demo.right.val}")
    print(f"                 /    \\")
    print(f"                {demo.right.left.val}  {demo.right.right.val}")
    print(f"\nLevel Order (top to bottom):")
    for i, level in enumerate(level_order(demo)):
        print(f"  Level {i}: {level}")
    print(f"\nLevel Order (bottom to top):")
    for i, level in enumerate(level_order_bottom(demo)):
        print(f"  Level {i}: {level}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
