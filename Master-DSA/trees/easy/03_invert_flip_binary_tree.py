# 📘 Trees (BST) — Easy 03
# Topic: Tree Modification — Invert / Flip Binary Tree
# Approach: Recursive postorder traversal
# Time: O(n) | Space: O(h)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_sample_tree():
    #       4
    #      / \
    #     2   7
    #    / \ / \
    #   1  3 6  9
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    return root


def invert_tree(root):
    """
    Inverts a binary tree (mirrors it).
    Time: O(n) | Space: O(h)
    """
    if not root:
        return None
    # Swap left and right
    root.left, root.right = root.right, root.left
    # Recursively invert subtrees
    invert_tree(root.left)
    invert_tree(root.right)
    return root


def invert_tree_concise(root):
    """
    Concise version of invert tree using recursion.
    """
    if not root:
        return None
    return TreeNode(root.val, invert_tree(root.right), invert_tree(root.left))


def is_mirror(root1, root2):
    """
    Helper to check if two trees are mirrors of each other.
    """
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    return (root1.val == root2.val and
            is_mirror(root1.left, root2.right) and
            is_mirror(root1.right, root2.left))


def is_symmetric(root):
    """
    Checks if a tree is symmetric (mirror of itself).
    """
    if not root:
        return True
    return is_mirror(root.left, root.right)


def level_order_traversal(root):
    """Helper for demo: returns level order list."""
    if not root: return []
    result = []
    queue = [root]
    while queue:
        level = []
        next_queue = []
        for node in queue:
            level.append(node.val)
            if node.left: next_queue.append(node.left)
            if node.right: next_queue.append(node.right)
        result.append(level)
        queue = next_queue
    return result


if __name__ == "__main__":
    import unittest

    class TestInvertTree(unittest.TestCase):
        def setUp(self):
            #       4
            #      / \
            #     2   7
            #    / \ / \
            #   1  3 6  9
            self.root = TreeNode(4)
            self.root.left = TreeNode(2)
            self.root.right = TreeNode(7)
            self.root.left.left = TreeNode(1)
            self.root.left.right = TreeNode(3)
            self.root.right.left = TreeNode(6)
            self.root.right.right = TreeNode(9)

        def test_invert_tree(self):
            inverted = invert_tree(self.root)
            self.assertEqual(inverted.val, 4)
            self.assertEqual(inverted.left.val, 7)
            self.assertEqual(inverted.right.val, 2)
            self.assertEqual(inverted.left.left.val, 9)
            self.assertEqual(inverted.left.right.val, 6)
            self.assertEqual(inverted.right.left.val, 3)
            self.assertEqual(inverted.right.right.val, 1)

        def test_concise_invert(self):
            inverted = invert_tree_concise(self.root)
            self.assertEqual(inverted.val, 4)
            self.assertEqual(inverted.left.val, 7)
            self.assertEqual(inverted.right.val, 2)

        def test_symmetric_check(self):
            # Symmetric tree
            root = TreeNode(1)
            root.left = TreeNode(2)
            root.right = TreeNode(2)
            self.assertTrue(is_symmetric(root))

    # Demo
    demo = create_sample_tree()
    print(f"Original tree:")
    print(f"       {demo.val}")
    print(f"      /    \\")
    print(f"     {demo.left.val}  {demo.right.val}")
    print(f"    / \\ / \\")
    print(f"   {demo.left.left.val} {demo.left.right.val} {demo.right.left.val} {demo.right.right.val}")
    print()
    inverted = invert_tree(demo)
    print(f"Inverted tree:")
    print(f"       {inverted.val}")
    print(f"      /    \\")
    print(f"     {inverted.left.val}  {inverted.right.val}")
    print(f"    / \\ / \\")
    print(f"   {inverted.left.left.val} {inverted.left.right.val} {inverted.right.left.val} {inverted.right.right.val}")
    print("Checking if original is symmetric:", is_symmetric(demo))
    print("Running unit tests...")
    unittest.main(verbosity=0)
