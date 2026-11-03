# 📘 Trees (BST) — Hard 03
# Topic: Advanced — Kth Smallest Element in BST
# Approach: Inorder traversal (gives sorted order in BST)
# Time: O(H + K) where H = tree height
# Space: O(H) for recursion stack

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_sample_bst():
    #       5
    #      / \
    #     3   6
    #    / \
    #   2   4
    #  /
    # 1
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    return root


def kth_smallest_bst(root, k):
    """
    Returns the kth smallest element in a BST.
    Uses inorder traversal which visits nodes in sorted order.
    Time: O(H + K) where H = tree height
    Space: O(H) for recursion stack
    """
    count = [0]
    result = [None]

    def inorder(node):
        if not node or count[0] >= k:
            return
        # Left subtree first
        inorder(node.left)
        if count[0] >= k:
            return
        # Process current node
        count[0] += 1
        if count[0] == k:
            result[0] = node.val
            return
        # Right subtree
        inorder(node.right)

    inorder(root)
    return result[0]


def kth_smallest_bst_iterative(root, k):
    """
    Iterative version using explicit stack.
    """
    stack = []
    current = root
    count = 0

    while stack or current:
        # Go left
        while current:
            stack.append(current)
            current = current.left

        # Process current
        current = stack.pop()
        count += 1
        if count == k:
            return current.val

        # Go right
        current = current.right

    return None


def kth_smallest_brute(root, k):
    """
    Brute force: Inorder traversal, store all elements, return kth.
    """
    def inorder(node, result):
        if not node:
            return
        inorder(node.left, result)
        result.append(node.val)
        inorder(node.right, result)

    values = []
    inorder(root, values)
    return values[k - 1] if 0 < k <= len(values) else None


if __name__ == "__main__":
    import unittest

    class TestKthSmallest(unittest.TestCase):
        def setUp(self):
            #       5
            #      / \
            #     3   6
            #    / \
            #   2   4
            #  /
            # 1
            self.root = TreeNode(5)
            self.root.left = TreeNode(3)
            self.root.right = TreeNode(6)
            self.root.left.left = TreeNode(2)
            self.root.left.right = TreeNode(4)
            self.root.left.left.left = TreeNode(1)

        def test_kth_smallest(self):
            self.assertEqual(kth_smallest_bst(self.root, 3), 3)
            self.assertEqual(kth_smallest_bst(self.root, 1), 1)
            self.assertEqual(kth_smallest_bst(self.root, 5), 5)
            self.assertEqual(kth_smallest_bst(self.root, 6), 6)

        def test_iterative(self):
            self.assertEqual(kth_smallest_bst_iterative(self.root, 3), 3)
            self.assertEqual(kth_smallest_bst_iterative(self.root, 1), 1)

        def test_brute(self):
            self.assertEqual(kth_smallest_brute(self.root, 3), 3)
            self.assertEqual(kth_smallest_brute(self.root, 6), 6)

    # Demo
    demo = create_sample_bst()
    print(f"BST:")
    print(f"       {demo.val}")
    print(f"      /    \\")
    print(f"     {demo.left.val}    {demo.right.val}")
    print(f"    / \\")
    print(f"   {demo.left.left.val}   {demo.left.right.val}")
    print(f"  /")
    print(f" {demo.left.left.left.val}")
    print(f"\nKth smallest (k=3): {kth_smallest_bst(demo, 3)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)