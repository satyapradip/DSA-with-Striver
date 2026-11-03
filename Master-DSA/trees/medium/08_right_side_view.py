# 📘 Trees (BST) — Medium 08
# Topic: Binary Tree — Right Side View
# Approach: BFS level order traversal (rightmost element at each level)
# Time: O(n) | Space: O(w)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_sample_tree():
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    return root


def right_side_view(root):
    """
    Returns the values of nodes visible from the right side.
    Only the rightmost node at each level is included.
    """
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.pop(0)
            # Add left child first, then right child
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            # The last node processed at this level is the rightmost
            if i == level_size - 1:
                result.append(node.val)

    return result


def right_side_view_brute(root):
    """
    Alternative: DFS that processes right subtree first.
    """
    result = []

    def dfs(node, depth):
        if not node:
            return
        # If first time visiting this depth, add to result
        if depth == len(result):
            result.append(node.val)
        # Process right subtree first (so right node is at each depth)
        dfs(node.right, depth + 1)
        dfs(node.left, depth + 1)

    dfs(root, 0)
    return result


if __name__ == "__main__":
    import unittest

    class TestRightSideView(unittest.TestCase):
        def setUp(self):
            #       1
            #      / \
            #     2   3
            #    / \   \
            #   4   5   6
            self.root = TreeNode(1)
            self.root.left = TreeNode(2)
            self.root.right = TreeNode(3)
            self.root.left.left = TreeNode(4)
            self.root.left.right = TreeNode(5)
            self.root.right.right = TreeNode(6)

        def test_right_side_view(self):
            result = right_side_view(self.root)
            self.assertEqual(result, [1, 3, 6])

        def test_right_side_view_brute(self):
            self.assertEqual(right_side_view_brute(self.root), [1, 3, 6])

        def test_single_node(self):
            self.assertEqual(right_side_view(TreeNode(1)), [1])

        def test_empty(self):
            self.assertEqual(right_side_view(None), [])

    # Demo
    demo = create_sample_tree()
    print(f"Tree:       {demo.val}")
    print(f"           /    \\")
    print(f"          {demo.left.val}    {demo.right.val}")
    print(f"         / \\   \\")
    print(f"        {demo.left.left.val} {demo.left.right.val} {demo.right.right.val}")
    print(f"\nRight Side View: {right_side_view(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
