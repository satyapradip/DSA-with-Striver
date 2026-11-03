# 📘 Trees (BST) — Easy 01
# Topic: Tree Traversals — Preorder, Inorder, Postorder
# Approach: Three recursive traversals
# Time: O(n) | Space: O(h) where h = tree height

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_sample_tree():
    """Create a sample binary tree for demonstration."""
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


def preorder_traversal(root):
    """
    Preorder traversal: Root → Left → Right
    Returns list of node values in preorder.
    """
    result = []
    def traverse(node):
        if not node:
            return
        result.append(node.val)
        traverse(node.left)
        traverse(node.right)
    traverse(root)
    return result


def inorder_traversal(root):
    """
    Inorder traversal: Left → Root → Right
    In a BST, this returns values in sorted order!
    """
    result = []
    def traverse(node):
        if not node:
            return
        traverse(node.left)
        result.append(node.val)
        traverse(node.right)
    traverse(root)
    return result


def postorder_traversal(root):
    """
    Postorder traversal: Left → Right → Root
    """
    result = []
    def traverse(node):
        if not node:
            return
        traverse(node.left)
        traverse(node.right)
        result.append(node.val)
    traverse(root)
    return result


def traversals_brute(root):
    """
    Brute force using iterative approach with explicit stack.
    """
    def preorder_iterative(root):
        if not root: return []
        stack, result = [root], []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
        return result

    def inorder_iterative(root):
        stack, result = [], []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        return result

    def postorder_iterative(root):
        if not root: return []
        stack, result = [root], []
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return result[::-1]

    return {
        'preorder': preorder_iterative(root),
        'inorder': inorder_iterative(root),
        'postorder': postorder_iterative(root)
    }


if __name__ == "__main__":
    import unittest

    class TestTreeTraversals(unittest.TestCase):
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

        def test_preorder(self):
            self.assertEqual(preorder_traversal(self.root), [1, 2, 4, 5, 3])

        def test_inorder(self):
            self.assertEqual(inorder_traversal(self.root), [4, 2, 5, 1, 3])

        def test_postorder(self):
            self.assertEqual(postorder_traversal(self.root), [4, 5, 2, 3, 1])

        def test_all_traversals(self):
            result = traversals_brute(self.root)
            self.assertEqual(result['preorder'], [1, 2, 4, 5, 3])
            self.assertEqual(result['inorder'], [4, 2, 5, 1, 3])
            self.assertEqual(result['postorder'], [4, 5, 2, 3, 1])

        def test_inorder_bst_sorted(self):
            # Create a BST
            bst = TreeNode(4)
            bst.left = TreeNode(2)
            bst.right = TreeNode(6)
            bst.left.left = TreeNode(1)
            bst.left.right = TreeNode(3)
            bst.right.left = TreeNode(5)
            bst.right.right = TreeNode(7)
            self.assertEqual(inorder_traversal(bst), [1, 2, 3, 4, 5, 6, 7])

    # Demo
    demo = create_sample_tree()
    print(f"Tree:       {demo.val}")
    print(f"           /    \\")
    print(f"          {demo.left.val}    {demo.right.val}")
    print(f"         / \\")
    print(f"        {demo.left.left.val}   {demo.left.right.val}")
    print(f"\nPreorder:    {preorder_traversal(demo)}")
    print(f"Inorder:     {inorder_traversal(demo)}")
    print(f"Postorder:   {postorder_traversal(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
