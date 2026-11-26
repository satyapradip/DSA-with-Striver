# 📘 Trees (Medium 09)
# Topic: Maximum Path Sum in Binary Tree
# Approach: DFS with state tracking
# Time: O(n) | Space: O(log n) [recursion stack]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root):
    """
    Find the maximum path sum in a binary tree.
    A path is any sequence of nodes from some starting node to any node
    in the tree along the edges. The path must contain at least one node.
    """
    max_sum = float('-inf')

    def dfs(node):
        nonlocal max_sum
        if not node:
            return 0

        # Recursively get max path sum from left and right subtrees
        # Only consider positive contributions
        left_gain = max(dfs(node.left), 0)
        right_gain = max(dfs(node.right), 0)

        # Current path sum through this node
        current_path = node.val + left_gain + right_gain

        # Update max sum
        max_sum = max(max_sum, current_path)

        # Return max gain for parent path (only one side)
        return node.val + max(left_gain, right_gain)

    dfs(root)
    return max_sum


def max_path_sum_brute(root):
    """
    Brute force: O(n²) approach.
    For each node, compute max path sum passing through that node.
    """
    def get_max_path(node):
        if not node:
            return 0

        # Max path sum through this node
        left_gain = max(get_max_path(node.left), 0)
        right_gain = max(get_max_path(node.right), 0)

        current_path = node.val + left_gain + right_gain

        # Max path sum in subtree
        max_path = max(
            current_path,
            get_max_path(node.left),
            get_max_path(node.right)
        )

        return max_path

    return get_max_path(root) if root else 0


if __name__ == "__main__":
    import unittest

    class TestMaxPathSum(unittest.TestCase):
        def test_max_path_sum(self):
            #     1
            #    / \
            #   2   3
            root = TreeNode(1)
            root.left = TreeNode(2)
            root.right = TreeNode(3)
            self.assertEqual(max_path_sum(root), 6)

        def test_max_path_sum_negative(self):
            #    -10
            #    /  \
            #   9   20
            #      /  \
            #     15   7
            root = TreeNode(-10)
            root.left = TreeNode(9)
            root.right = TreeNode(20, TreeNode(15), TreeNode(7))
            self.assertEqual(max_path_sum(root), 42)

        def test_max_path_sum_single(self):
            root = TreeNode(1)
            self.assertEqual(max_path_sum(root), 1)

        def test_max_path_sum_brute(self):
            root = TreeNode(-10)
            root.left = TreeNode(9)
            root.right = TreeNode(20, TreeNode(15), TreeNode(7))
            self.assertEqual(max_path_sum_brute(root), 42)

    # Demo
    demo = TreeNode(-10)
    demo.left = TreeNode(9)
    demo.right = TreeNode(20, TreeNode(15), TreeNode(7))
    print(f"Max path sum: {max_path_sum(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)