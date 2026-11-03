# 📘 Trees (BST) — Easy 04
# Topic: Tree Modification — Subtree Check
# Approach: Tree traversal + equality check
# Time: O(n * m) where n = s.size, m = t.size

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_sample_tree1():
    # Tree s
    #       3
    #      / \
    #     4   5
    #    / \
    #   1   2
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    return root


def create_sample_tree2():
    # Tree t (subtree of s)
    #     4
    #    / \
    #   1   2
    root = TreeNode(4)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    return root


def create_sample_tree3():
    #   4
    #  / \
    # 1   2
    root = TreeNode(4)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    return root


def is_subtree(s, t):
    """
    Returns True if tree t is a subtree of tree s.
    A subtree of s is a tree consists of a node in s and all of its descendants.
    """
    if not t:
        return True  # Empty tree is always a subtree
    if not s:
        return False  # Non-empty tree cannot be a subtree of empty tree

    # Check if s and t are the same tree, or if t is a subtree of s's left/right
    return is_same_tree(s, t) or is_subtree(s.left, t) or is_subtree(s.right, t)


def is_same_tree(p, q):
    """
    Checks if two trees are identical.
    """
    if not p and not q:
        return True
    if not p or not q:
        return False
    return (p.val == q.val and
            is_same_tree(p.left, q.left) and
            is_same_tree(p.right, q.right))


if __name__ == "__main__":
    import unittest

    class TestSubtreeCheck(unittest.TestCase):
        def setUp(self):
            # s:       3
            #        / \
            #       4   5
            #      / \
            #     1   2
            self.s = TreeNode(3)
            self.s.left = TreeNode(4)
            self.s.right = TreeNode(5)
            self.s.left.left = TreeNode(1)
            self.s.left.right = TreeNode(2)

        def test_subtree_exists(self):
            # t:       4
            #        / \
            #       1   2
            t = TreeNode(4)
            t.left = TreeNode(1)
            t.right = TreeNode(2)
            self.assertTrue(is_subtree(self.s, t))

        def test_subtree_not_exists(self):
            # t:       4
            #        / \
            #       1   3
            t = TreeNode(4)
            t.left = TreeNode(1)
            t.right = TreeNode(3)
            self.assertFalse(is_subtree(self.s, t))

        def test_empty_subtree(self):
            self.assertTrue(is_subtree(self.s, None))

        def test_empty_tree(self):
            self.assertTrue(is_subtree(None, None))

    # Demo
    demo_s = create_sample_tree1()
    demo_t = create_sample_tree2()
    print(f"Tree s:       {demo_s.val}")
    print(f"           /    \\")
    print(f"          {demo_s.left.val}    {demo_s.right.val}")
    print(f"         / \\")
    print(f"        {demo_s.left.left.val}   {demo_s.left.right.val}")
    print()
    print(f"Tree t:       {demo_t.val}")
    print(f"           /    \\")
    print(f"          {demo_t.left.val}  {demo_t.right.val}")
    print()
    print(f"Is t a subtree of s? {is_subtree(demo_s, demo_t)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
