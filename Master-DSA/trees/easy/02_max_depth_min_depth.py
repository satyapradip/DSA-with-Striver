# 📘 Trees (BST) — Easy 02
# Topic: Tree Depth & Height — Max Depth, Min Depth
# Approach: Recursive depth calculation
# Time: O(n) | Space: O(h)

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


def create_min_depth_tree():
    #       2
    #      /
    #     3
    #    /
    #   4
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.left.left = TreeNode(4)
    return root


def max_depth(root):
    """
    Returns the maximum depth (height) of the binary tree.
    Depth = number of nodes along the longest path from root to leaf.
    """
    if not root:
        return 0
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    return 1 + max(left_depth, right_depth)


def min_depth(root):
    """
    Returns the minimum depth of the binary tree.
    Depth = number of nodes along the shortest path from root to leaf.
    """
    if not root:
        return 0
    # If both children exist, take the minimum of both
    if root.left and root.right:
        return 1 + min(min_depth(root.left), min_depth(root.right))
    # If only left child exists, use its depth
    if root.left:
        return 1 + min_depth(root.left)
    # If only right child exists, use its depth
    if root.right:
        return 1 + min_depth(root.right)
    # Leaf node (no children)
    return 1


def min_depth_brute(root):
    """
    Brute force: level order traversal and count levels until we hit a leaf.
    """
    if not root:
        return 0
    queue = [(root, 1)]
    min_d = float('inf')
    while queue:
        node, depth = queue.pop(0)
        if not node.left and not node.right:
            min_d = min(min_d, depth)
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    return min_d


def max_depth_brute(root):
    """
    Brute force: level order traversal and count levels.
    """
    if not root:
        return 0
    queue = [root]
    depth = 0
    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return depth


if __name__ == "__main__":
    import unittest

    class TestTreeDepth(unittest.TestCase):
        def setUp(self):
            self.root = TreeNode(3)
            self.root.left = TreeNode(9)
            self.root.right = TreeNode(20)
            self.root.right.left = TreeNode(15)
            self.root.right.right = TreeNode(7)

        def test_max_depth(self):
            self.assertEqual(max_depth(self.root), 3)

        def test_min_depth(self):
            self.assertEqual(min_depth(self.root), 2)

        def test_min_depth_example(self):
            root = create_min_depth_tree()
            self.assertEqual(min_depth(root), 3)

        def test_empty(self):
            self.assertEqual(max_depth(None), 0)
            self.assertEqual(min_depth(None), 0)

        def test_single_node(self):
            root = TreeNode(1)
            self.assertEqual(max_depth(root), 1)
            self.assertEqual(min_depth(root), 1)

    # Demo
    demo = create_sample_tree()
    print(f"Tree:       {demo.val}")
    print(f"           /    \\")
    print(f"          {demo.left.val}    {demo.right.val}")
    print(f"                 /    \\")
    print(f"                {demo.right.left.val}  {demo.right.right.val}")
    print(f"\nMax Depth: {max_depth(demo)}")
    print(f"Min Depth: {min_depth(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
