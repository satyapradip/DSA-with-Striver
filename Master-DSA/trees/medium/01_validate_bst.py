# 📘 Trees (BST) — Medium 01
# Topic: BST Properties — Validate Binary Search Tree
# Approach: BST property with range constraint (min_val, max_val)
# Time: O(n) | Space: O(h)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_sample_bst():
    #       2
    #      / \
    #     1   3
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    return root


def create_invalid_bst():
    #       5
    #      / \
    #     1   4
    #        / \
    #       3   6
    # 3 is in the right subtree of 5 but less than 5 → invalid BST
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    return root


def validate_bst(root):
    """
    Returns True if the binary tree is a valid BST.
    Uses the BST property: every node's value must be
    within a valid range (min_val, max_val).
    Left subtree: values < current node's value
    Right subtree: values > current node's value
    """
    def validate(node, min_val, max_val):
        if not node:
            return True
        if not (min_val < node.val < max_val):
            return False
        # Left subtree: values must be < node.val
        # Right subtree: values must be > node.val
        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))

    return validate(root, float('-inf'), float('inf'))


def validate_bst_inorder(root):
    """
    Alternative approach: Inorder traversal should give sorted values for a BST.
    Uses O(n) space for the traversal result.
    """
    def inorder_traversal(node):
        if not node:
            return []
        return (inorder_traversal(node.left) +
                [node.val] +
                inorder_traversal(node.right))

    values = inorder_traversal(root)
    return all(values[i] < values[i + 1] for i in range(len(values) - 1))


def validate_bst_brute(root):
    """
    Brute force: check each node against its ancestors.
    """
    def is_valid(node, min_val, max_val):
        if not node:
            return True
        if node.val <= min_val or node.val >= max_val:
            return False
        return (is_valid(node.left, min_val, node.val) and
                is_valid(node.right, node.val, max_val))

    return is_valid(root, float('-inf'), float('inf'))


if __name__ == "__main__":
    import unittest

    class TestValidateBST(unittest.TestCase):
        def test_valid_bst(self):
            root = create_sample_bst()
            self.assertTrue(validate_bst(root))

        def test_invalid_bst(self):
            root = create_invalid_bst()
            self.assertFalse(validate_bst(root))

        def test_inorder_method_valid(self):
            root = create_sample_bst()
            self.assertTrue(validate_bst_inorder(root))

        def test_empty(self):
            self.assertTrue(validate_bst(None))

        def test_single_node(self):
            root = TreeNode(1)
            self.assertTrue(validate_bst(root))

        def test_duplicate_values(self):
            # In a BST, duplicates are typically not allowed
            root = TreeNode(1)
            root.left = TreeNode(1)
            self.assertFalse(validate_bst(root))

    # Demo
    demo = create_sample_bst()
    print(f"Tree:       {demo.val}")
    print(f"           /    \\")
    print(f"          {demo.left.val}    {demo.right.val}")
    print(f"Valid BST? {validate_bst(demo)}")
    print()
    invalid = create_invalid_bst()
    print(f"Invalid BST:           {invalid.val}")
    print(f"                       /    \\")
    print(f"                      {invalid.left.val}    {invalid.right.val}")
    print(f"                     /    \\")
    print(f"                    {invalid.right.left.val}  {invalid.right.right.val}")
    print(f"Valid BST? {validate_bst(invalid)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
