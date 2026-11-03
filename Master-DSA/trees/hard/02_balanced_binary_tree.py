# 📘 Trees (BST) — Hard 02
# Topic: Advanced — Balanced Binary Tree
# Approach: Recursion with height calculation and balance check simultaneously
# Time: O(n) | Space: O(h)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_sample_tree_balanced():
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


def create_sample_tree_unbalanced():
    #       1
    #      /
    #     2
    #    /
    #   3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    return root


def is_balanced(root):
    """
    Returns True if the binary tree is height-balanced.
    A tree is balanced if the depth of the two subtrees of every node
    never differs by more than 1.
    """
    def check_balance(node):
        if not node:
            return 0, True

        left_height, left_balanced = check_balance(node.left)
        right_height, right_balanced = check_balance(node.right)

        # Current node is balanced if both subtrees are balanced
        # and their heights differ by at most 1
        is_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1

        return max(left_height, right_height) + 1, is_balanced

    _, balanced = check_balance(root)
    return balanced


def is_balanced_brute(root):
    """
    Brute force: Calculate height of left and right subtrees at every node.
    Time: O(n^2) in worst case
    """
    def height(node):
        if not node:
            return 0
        return 1 + max(height(node.left), height(node.right))

    if not root:
        return True
    if abs(height(root.left) - height(root.right)) > 1:
        return False
    return is_balanced_brute(root.left) and is_balanced_brute(root.right)


if __name__ == "__main__":
    import unittest

    class TestBalancedTree(unittest.TestCase):
        def setUp(self):
            self.balanced_tree = TreeNode(3)
            self.balanced_tree.left = TreeNode(9)
            self.balanced_tree.right = TreeNode(20)
            self.balanced_tree.right.left = TreeNode(15)
            self.balanced_tree.right.right = TreeNode(7)

            self.unbalanced_tree = TreeNode(1)
            self.unbalanced_tree.left = TreeNode(2)
            self.unbalanced_tree.left.left = TreeNode(3)

            self.single_node = TreeNode(1)

        def test_balanced_tree(self):
            self.assertTrue(is_balanced(self.balanced_tree))

        def test_unbalanced_tree(self):
            self.assertFalse(is_balanced(self.unbalanced_tree))

        def test_single_node(self):
            self.assertTrue(is_balanced(self.single_node))

        def test_empty(self):
            self.assertTrue(is_balanced(None))

        def test_brute_force_balanced(self):
            self.assertTrue(is_balanced_brute(self.balanced_tree))

        def test_brute_force_unbalanced(self):
            self.assertFalse(is_balanced_brute(self.unbalanced_tree))

    # Demo
    demo = create_sample_tree_balanced()
    print(f"Balanced tree: {demo.val}")
    print(f"           /    \\")
    print(f"          {demo.left.val}  {demo.right.val}")
    print(f"                 /    \\")
    print(f"                {demo.right.left.val}  {demo.right.right.val}")
    print(f"Is balanced? {is_balanced(demo)}")
    print()
    demo2 = create_sample_tree_unbalanced()
    print(f"Unbalanced tree: {demo2.val}")
    print(f"               /")
    print(f"              {demo2.left.val}")
    print(f"             /")
    print(f"            {demo2.left.left.val}")
    print(f"Is balanced? {is_balanced(demo2)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
