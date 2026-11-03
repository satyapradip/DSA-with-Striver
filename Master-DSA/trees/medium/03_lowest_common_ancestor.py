# 📘 Trees (BST) — Medium 03
# Topic: LCA — Lowest Common Ancestor (BST & Binary Tree)
# Approach: BST property + Binary tree recursion
# Time: O(n) | Space: O(h)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_sample_bst():
    #       6
    #      / \
    #     2   8
    #    / \ / \
    #   0  4 7   9
    #     / \
    #    3   5
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    return root


def create_bst():
    #       6
    #      / \
    #     2   8
    #    / \
    #   0   4
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    return root


def create_bst_pq():
    #       6
    #      / \
    #     2   8
    #    / \
    #   0   4
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    return root


def lowest_common_ancestor_bst(root, p, q):
    """
    Finds the lowest common ancestor of two nodes in a BST.
    Uses BST property: all left nodes < current node < right nodes.
    Time: O(h) where h = tree height
    Space: O(h) for recursion stack
    """
    # Ensure p < q for consistency
    if p.val > q.val:
        p, q = q, p

    # If current node is between p and q, it's the LCA
    if p.val <= root.val <= q.val:
        return root

    # Both p and q are smaller → go left
    if q.val < root.val:
        return lowest_common_ancestor_bst(root.left, p, q)

    # Both p and q are larger → go right
    return lowest_common_ancestor_bst(root.right, p, q)


def lowest_common_ancestor_bt(root, p, q):
    """
    Finds the lowest common ancestor of two nodes in a binary tree.
    Uses recursion: if left and right both return non-None, current is LCA.
    Time: O(n) | Space: O(h)
    """
    # Base case: empty tree or found one of the nodes
    if not root or root == p or root == q:
        return root

    # Search left and right subtrees
    left = lowest_common_ancestor_bt(root.left, p, q)
    right = lowest_common_ancestor_bt(root.right, p, q)

    # Both found → current is LCA
    if left and right:
        return root

    # One found → return it
    return left if left else right


def lowest_common_ancestor_brute(root, p, q):
    """
    Brute force: find paths from root to p and q, then find common ancestor.
    """
    def find_path(node, target):
        if not node:
            return None
        if node == target:
            return [node]
        left_path = find_path(node.left, target)
        if left_path:
            return [node] + left_path
        right_path = find_path(node.right, target)
        if right_path:
            return [node] + right_path
        return None

    path_p = find_path(root, p)
    path_q = find_path(root, q)

    if not path_p or not path_q:
        return None

    # Find last common node
    lca = None
    for i in range(min(len(path_p), len(path_q))):
        if path_p[i] == path_q[i]:
            lca = path_p[i]
        else:
            break
    return lca


if __name__ == "__main__":
    import unittest

    class TestLowestCommonAncestor(unittest.TestCase):
        def setUp(self):
            #       6
            #      / \
            #     2   8
            #    / \ / \
            #   0  4 7   9
            #     / \
            #    3   5
            self.root = TreeNode(6)
            self.root.left = TreeNode(2)
            self.root.right = TreeNode(8)
            self.root.left.left = TreeNode(0)
            self.root.left.right = TreeNode(4)
            self.root.left.right.left = TreeNode(3)
            self.root.left.right.right = TreeNode(5)
            self.root.right.left = TreeNode(7)
            self.root.right.right = TreeNode(9)

        def test_lca_bst(self):
            p = self.root.left  # 2
            q = self.root.right  # 8
            self.assertEqual(lowest_common_ancestor_bst(self.root, p, q).val, 6)

        def test_lca_bst_edge(self):
            p = self.root.left.left  # 0
            q = self.root.left.right.right  # 5
            self.assertEqual(lowest_common_ancestor_bst(self.root, p, q).val, 2)

        def test_lca_binary_tree(self):
            p = self.root.left.left  # 0
            q = self.root.left.right.right  # 5
            self.assertEqual(lowest_common_ancestor_bt(self.root, p, q).val, 2)

    # Demo
    demo = create_sample_bst()
    p = demo.left  # 2
    q = demo.right  # 8
    print(f"Tree:       {demo.val}")
    print(f"           /    \\")
    print(f"          {demo.left.val}    {demo.right.val}")
    print(f"         / \\  / \\")
    print(f"        {demo.left.left.val} {demo.left.right.val} {demo.right.left.val} {demo.right.right.val}")
    print(f"LCA({p.val}, {q.val}) = {lowest_common_ancestor_bst(demo, p, q).val}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
