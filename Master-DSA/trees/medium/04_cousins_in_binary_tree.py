# 📘 Trees (BST) — Medium 04
# Topic: Binary Tree — Cousins in Binary Tree
# Approach: BFS level order traversal
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


def is_cousins(root, x, y):
    """
    Returns True if nodes with values x and y are cousins.
    Two nodes are cousins if:
    - They have the same depth
    - They have different parents
    """
    if not root:
        return False

    queue = [root]
    while queue:
        level_size = len(queue)
        found_x = False
        found_y = False
        parent_x = None
        parent_y = None

        for _ in range(level_size):
            node = queue.pop(0)

            # Check left child
            if node.left:
                queue.append(node.left)
                if node.left.val == x:
                    found_x = True
                    parent_x = node
                if node.left.val == y:
                    found_y = True
                    parent_y = node

            # Check right child
            if node.right:
                queue.append(node.right)
                if node.right.val == x:
                    found_x = True
                    parent_x = node
                if node.right.val == y:
                    found_y = True
                    parent_y = node

        # If both found at this level, check if they have different parents
        if found_x and found_y:
            return parent_x != parent_y

        # If only one found, they're not cousins
        if found_x or found_y:
            return False

    return False


def is_cousins_brute(root, x, y):
    """
    Brute force: Find depth and parent of both nodes using DFS.
    """
    def find_node(node, target, depth=0, parent=None):
        if not node:
            return None
        if node.val == target:
            return (depth, parent)
        left_result = find_node(node.left, target, depth + 1, node)
        if left_result:
            return left_result
        return find_node(node.right, target, depth + 1, node)

    result_x = find_node(root, x)
    result_y = find_node(root, y)

    if not result_x or not result_y:
        return False

    depth_x, parent_x = result_x
    depth_y, parent_y = result_y

    return depth_x == depth_y and parent_x != parent_y


if __name__ == "__main__":
    import unittest

    class TestCousins(unittest.TestCase):
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

        def test_cousins_yes(self):
            self.assertTrue(is_cousins(self.root, 5, 6))

        def test_cousins_no(self):
            self.assertFalse(is_cousins(self.root, 4, 5))

        def test_cousins_not_same_depth(self):
            self.assertFalse(is_cousins(self.root, 4, 3))

        def test_brute(self):
            self.assertTrue(is_cousins_brute(self.root, 5, 6))
            self.assertFalse(is_cousins_brute(self.root, 4, 5))

    # Demo
    demo = create_sample_tree()
    print(f"Tree:       {demo.val}")
    print(f"           /    \\")
    print(f"          {demo.left.val}    {demo.right.val}")
    print(f"         / \\   \\")
    print(f"        {demo.left.left.val} {demo.left.right.val} {demo.right.right.val}")
    print(f"\nAre 4 and 5 cousins? {is_cousins(demo, 4, 5)}")
    print(f"Are 5 and 6 cousins? {is_cousins(demo, 5, 6)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
