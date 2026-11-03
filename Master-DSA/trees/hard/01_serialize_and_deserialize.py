# 📘 Trees (BST) — Hard 01
# Topic: Advanced — Serialize & Deserialize Binary Tree
# Approach: Preorder traversal with markers for null nodes
# Time: O(n) | Space: O(n)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    """
    Serializes a binary tree to a string.
    Uses preorder traversal with 'X' as a marker for null nodes.
    Result: "1,2,X,X,3,X,X" where X represents a null node.
    """
    result = []
    def serialize_helper(node):
        if not node:
            result.append('X')
            return
        result.append(str(node.val))
        serialize_helper(node.left)
        serialize_helper(node.right)

    serialize_helper(root)
    return ','.join(result)


def deserialize(data):
    """
    Deserializes a string back to a binary tree.
    """
    if not data:
        return None

    nodes = data.split(',')
    index = [0]

    def deserialize_helper():
        if nodes[index[0]] == 'X':
            index[0] += 1
            return None

        node = TreeNode(int(nodes[index[0]]))
        index[0] += 1
        node.left = deserialize_helper()
        node.right = deserialize_helper()
        return node

    return deserialize_helper()


def serialize_brute(root):
    """
    Alternative: Using level order (BFS) serialization.
    """
    if not root:
        return ""

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node:
            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append('X')

    # Remove trailing 'X' markers
    while result and result[-1] == 'X':
        result.pop()

    return ','.join(result)


def deserialize_brute(data):
    """
    Alternative: Build tree from level order representation.
    """
    if not data:
        return None

    nodes = data.split(',')
    root = TreeNode(int(nodes[0]))
    queue = [root]
    i = 1

    while queue and i < len(nodes):
        node = queue.pop(0)

        # Left child
        if i < len(nodes) and nodes[i] != 'X':
            node.left = TreeNode(int(nodes[i]))
            queue.append(node.left)
        i += 1

        # Right child
        if i < len(nodes) and nodes[i] != 'X':
            node.right = TreeNode(int(nodes[i]))
            queue.append(node.right)
        i += 1

    return root


def print_preorder(root):
    if not root:
        return []
    return [root.val] + print_preorder(root.left) + print_preorder(root.right)


if __name__ == "__main__":
    import unittest

    class TestSerializeDeserialize(unittest.TestCase):
        def setUp(self):
            # Build tree:     1
            #                / \
            #               2   3
            #              /   / \
            #             4   5   6
            self.root = TreeNode(1)
            self.root.left = TreeNode(2)
            self.root.right = TreeNode(3)
            self.root.left.left = TreeNode(4)
            self.root.right.left = TreeNode(5)
            self.root.right.right = TreeNode(6)

        def test_serialize_deserialize(self):
            data = serialize(self.root)
            new_root = deserialize(data)
            self.assertEqual(print_preorder(self.root), print_preorder(new_root))

        def test_empty(self):
            data = serialize(None)
            self.assertIsNone(deserialize(data))

        def test_single_node(self):
            data = serialize(TreeNode(1))
            self.assertEqual(deserialize(data).val, 1)

    # Demo
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.right.left = TreeNode(5)
    tree.right.right = TreeNode(6)

    print(f"Original tree preorder: {print_preorder(tree)}")
    print(f"Serialized: '{serialize(tree)}'")
    new_root = deserialize(serialize(tree))
    print(f"Deserialized preorder: {print_preorder(new_root)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)