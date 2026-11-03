# 📘 Trees (BST) — Medium 06
# Topic: Binary Tree Paths — Path Sum
# Approach: DFS with target sum tracking
# Time: O(n) | Space: O(h)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_sample_tree():
    #       5
    #      / \
    #     4   8
    #    /   / \
    #   11  13  4
    #  /  \      \
    # 7    2      1
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    return root


def has_path_sum(root, target_sum):
    """
    Returns True if there exists a root-to-leaf path where the sum of values equals target_sum.
    """
    if not root:
        return False

    # If this is a leaf node, check if remaining sum equals node value
    if not root.left and not root.right:
        return root.val == target_sum

    # Subtract current node's value and check children
    remaining = target_sum - root.val
    return (has_path_sum(root.left, remaining) or
            has_path_sum(root.right, remaining))


def path_sum_brute(root, target_sum):
    """
    Brute force: returns all root-to-leaf paths that sum to target_sum.
    """
    def dfs(node, current_sum, current_path, all_paths):
        if not node:
            return

        current_sum += node.val
        current_path.append(node.val)

        # Check if leaf node
        if not node.left and not node.right:
            if current_sum == target_sum:
                all_paths.append(list(current_path))
        else:
            dfs(node.left, current_sum, current_path, all_paths)
            dfs(node.right, current_sum, current_path, all_paths)

        current_path.pop()

    if not root:
        return []

    all_paths = []
    dfs(root, 0, [], all_paths)
    return all_paths


def path_sum_count(root, target_sum):
    """
    Returns the count of root-to-leaf paths that sum to target_sum.
    """
    if not root:
        return 0

    count = 0

    def dfs(node, current_sum):
        nonlocal count
        current_sum += node.val

        if not node.left and not node.right:
            if current_sum == target_sum:
                count += 1
            return

        if node.left:
            dfs(node.left, current_sum)
        if node.right:
            dfs(node.right, current_sum)

    dfs(root, 0)
    return count


if __name__ == "__main__":
    import unittest

    class TestPathSum(unittest.TestCase):
        def setUp(self):
            #       5
            #      / \
            #     4   8
            #    /   / \
            #   11  13  4
            #  /  \      \
            # 7    2      1
            self.root = TreeNode(5)
            self.root.left = TreeNode(4)
            self.root.right = TreeNode(8)
            self.root.left.left = TreeNode(11)
            self.root.left.left.left = TreeNode(7)
            self.root.left.left.right = TreeNode(2)
            self.root.right.left = TreeNode(13)
            self.root.right.right = TreeNode(4)
            self.root.right.right.right = TreeNode(1)

        def test_has_path_sum(self):
            self.assertTrue(has_path_sum(self.root, 22))  # 5+4+11+2 = 22
            self.assertFalse(has_path_sum(self.root, 100))

        def test_paths(self):
            result = path_sum_brute(self.root, 22)
            self.assertEqual(len(result), 1)
            self.assertEqual(result[0], [5, 4, 11, 2])

        def test_count(self):
            self.assertEqual(path_sum_count(self.root, 22), 1)

    # Demo
    demo = create_sample_tree()
    print(f"Tree:")
    print(f"       {demo.val}")
    print(f"      /    \\")
    print(f"     {demo.left.val}    {demo.right.val}")
    print(f"    /    /    \\")
    print(f"   {demo.left.left.val}  {demo.right.left.val}  {demo.right.right.val}")
    print(f"  / \\            \\")
    print(f" {demo.left.left.left.val} {demo.left.left.right.val}        {demo.right.right.right.val}")
    print(f"\nPath sum = 22? {has_path_sum(demo, 22)} (5+4+11+2)")
    print(f"Paths with sum 22: {path_sum_brute(demo, 22)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
