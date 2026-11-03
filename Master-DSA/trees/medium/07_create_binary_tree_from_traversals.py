# 📘 Trees (BST) — Medium 07
# Topic: Tree Serialization — Build Binary Tree from Preorder + Inorder
# Approach: Recursion with index mapping
# Time: O(n) | Space: O(n)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_from_preorder_inorder(preorder, inorder):
    """
    Builds a binary tree from its preorder and inorder traversals.
    Preorder: Root → Left → Right
    Inorder: Left → Root → Right
    """
    if not preorder or not inorder:
        return None

    # Create a map for inorder indices (for O(1) lookups)
    inorder_map = {val: idx for idx, val in enumerate(inorder)}

    def build(pre_start, pre_end, in_start, in_end):
        if pre_start > pre_end or in_start > in_end:
            return None

        # First element in preorder is the root
        root_val = preorder[pre_start]
        root = TreeNode(root_val)

        # Find root's position in inorder
        root_idx = inorder_map[root_val]

        # Calculate size of left subtree
        left_size = root_idx - in_start

        # Recursively build left and right subtrees
        root.left = build(pre_start + 1, pre_start + left_size, in_start, root_idx - 1)
        root.right = build(pre_start + left_size + 1, pre_end, root_idx + 1, in_end)

        return root

    return build(0, len(preorder) - 1, 0, len(inorder) - 1)


def build_tree_from_postorder_inorder(postorder, inorder):
    """
    Alternative: Build binary tree from postorder and inorder.
    Postorder: Left → Right → Root
    """
    if not postorder or not inorder:
        return None

    # Create a map for inorder indices
    inorder_map = {val: idx for idx, val in enumerate(inorder)}

    def build(post_start, post_end, in_start, in_end):
        if post_start > post_end or in_start > in_end:
            return None

        # Last element in postorder is the root
        root_val = postorder[post_end]
        root = TreeNode(root_val)

        # Find root's position in inorder
        root_idx = inorder_map[root_val]

        # Calculate size of right subtree
        right_size = in_end - root_idx

        # Recursively build right and left subtrees
        root.right = build(post_end - right_size, post_end - 1, root_idx + 1, in_end)
        root.left = build(post_start, post_end - right_size - 1, in_start, root_idx - 1)

        return root

    return build(0, len(postorder) - 1, 0, len(inorder) - 1)


def print_tree_preorder(root):
    """Helper for demo: returns preorder traversal."""
    if not root:
        return []
    return [root.val] + print_tree_preorder(root.left) + print_tree_preorder(root.right)


if __name__ == "__main__":
    import unittest

    class TestBuildTree(unittest.TestCase):
        def test_preorder_inorder(self):
            preorder = [3, 9, 20, 15, 7]
            inorder = [9, 3, 15, 20, 7]

            root = build_tree_from_preorder_inorder(preorder, inorder)

            # Verify by checking preorder
            self.assertEqual(print_tree_preorder(root), preorder)
            # Verify by checking inorder
            self.assertEqual(self.inorder_traversal(root), inorder)

        def test_postorder_inorder(self):
            postorder = [9, 15, 7, 20, 3]
            inorder = [9, 3, 15, 20, 7]

            root = build_tree_from_postorder_inorder(postorder, inorder)

            # Verify by checking postorder
            self.assertEqual(self.postorder_traversal(root), postorder)
            # Verify by checking inorder
            self.assertEqual(self.inorder_traversal(root), inorder)

        def inorder_traversal(self, root):
            if not root:
                return []
            return self.inorder_traversal(root.left) + [root.val] + self.inorder_traversal(root.right)

        def postorder_traversal(self, root):
            if not root:
                return []
            return self.postorder_traversal(root.left) + self.postorder_traversal(root.right) + [root.val]

    # Demo
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    print(f"Preorder: {preorder}")
    print(f"Inorder:  {inorder}")
    root = build_tree_from_preorder_inorder(preorder, inorder)
    print(f"Reconstructed tree preorder: {print_tree_preorder(root)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
