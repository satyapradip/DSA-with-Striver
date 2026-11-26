# 📘 Trees (Easy 05)
# Topic: Symmetric Tree (Mirror Tree)
# Approach: DFS/BFS comparison
# Time: O(n) | Space: O(n) [recursion/queue]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root):
    """
    Check if a binary tree is symmetric around its center.
    """
    if not root:
        return True

    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val and
                is_mirror(left.left, right.right) and
                is_mirror(left.right, right.left))

    return is_mirror(root.left, root.right)


def is_symmetric_iterative(root):
    """
    Check if a binary tree is symmetric using iterative approach (BFS).
    """
    if not root:
        return True

    queue = [(root.left, root.right)]

    while queue:
        left, right = queue.pop(0)

        if not left and not right:
            continue
        if not left or not right:
            return False
        if left.val != right.val:
            return False

        queue.append((left.left, right.right))
        queue.append((left.right, right.left))

    return True


if __name__ == "__main__":
    import unittest

    class TestIsSymmetric(unittest.TestCase):
        def test_symmetric(self):
            #     1
            #    / \
            #   2   2
            #  / \ / \
            # 3  4 4  3
            root = TreeNode(1)
            root.left = TreeNode(2, TreeNode(3), TreeNode(4))
            root.right = TreeNode(2, TreeNode(4), TreeNode(3))
            self.assertTrue(is_symmetric(root))

        def test_not_symmetric(self):
            #     1
            #    / \
            #   2   2
            #    \   \
            #     3   3
            root = TreeNode(1)
            root.left = TreeNode(2, None, TreeNode(3))
            root.right = TreeNode(2, None, TreeNode(3))
            self.assertFalse(is_symmetric(root))

        def test_symmetric_iterative(self):
            root = TreeNode(1)
            root.left = TreeNode(2, TreeNode(3), TreeNode(4))
            root.right = TreeNode(2, TreeNode(4), TreeNode(3))
            self.assertTrue(is_symmetric_iterative(root))

    # Demo
    demo = TreeNode(1)
    demo.left = TreeNode(2, TreeNode(3), TreeNode(4))
    demo.right = TreeNode(2, TreeNode(4), TreeNode(3))
    print(f"Is symmetric? {is_symmetric(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)