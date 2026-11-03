# 📘 Trees (BST) — Medium 05
# Topic: Binary Tree Paths — Root-to-Leaf Paths
# Approach: DFS + backtracking
# Time: O(n) | Space: O(h)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_sample_tree():
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    return root


def binary_tree_paths(root):
    """
    Returns all root-to-leaf paths in the binary tree.
    Each path is a string like "1->2->4".
    """
    if not root:
        return []

    result = []

    def dfs(node, path):
        if not node:
            return

        # Add current node to path
        path.append(str(node.val))

        # If leaf node, add path to result
        if not node.left and not node.right:
            result.append("->".join(path))
        else:
            # Recurse left and right
            dfs(node.left, path)
            dfs(node.right, path)

        # Backtrack: remove current node from path
        path.pop()

    dfs(root, [])
    return result


def binary_tree_paths_brute(root):
    """
    Brute force: returns list of node lists, then convert to strings.
    """
    def find_paths(node, path, all_paths):
        if not node:
            return
        path.append(node.val)
        if not node.left and not node.right:
            all_paths.append(list(path))
        else:
            find_paths(node.left, path, all_paths)
            find_paths(node.right, path, all_paths)
        path.pop()

    if not root:
        return []

    all_paths = []
    find_paths(root, [], all_paths)
    return ["->".join(map(str, path)) for path in all_paths]


if __name__ == "__main__":
    import unittest

    class TestBinaryTreePaths(unittest.TestCase):
        def setUp(self):
            #       1
            #      / \
            #     2   3
            #    / \
            #   4   5
            self.root = TreeNode(1)
            self.root.left = TreeNode(2)
            self.root.right = TreeNode(3)
            self.root.left.left = TreeNode(4)
            self.root.left.right = TreeNode(5)

        def test_paths(self):
            result = binary_tree_paths(self.root)
            self.assertEqual(sorted(result), ["1->2->4", "1->2->5", "1->3"])

        def test_single_node(self):
            self.assertEqual(binary_tree_paths(TreeNode(1)), ["1"])

        def test_empty(self):
            self.assertEqual(binary_tree_paths(None), [])

    # Demo
    demo = create_sample_tree()
    print(f"Tree:       {demo.val}")
    print(f"           /    \\")
    print(f"          {demo.left.val}    {demo.right.val}")
    print(f"         / \\")
    print(f"        {demo.left.left.val}   {demo.left.right.val}")
    print()
    print(f"Root-to-Leaf Paths: {binary_tree_paths(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
