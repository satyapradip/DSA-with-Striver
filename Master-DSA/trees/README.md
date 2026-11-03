# 📚 Trees (BST) — Master Guide

> A complete, placement-oriented guide to **Trees and Binary Search Trees** — the
> hierarchical data structures that appear in almost every technical interview.
> Covers: tree traversals, BST properties, recursion on trees, and advanced tree algorithms.

---

## 🗺️ Tree Patterns Map

| Pattern | Difficulty | Key Problems | Key Idea |
|---|---|---|---|
| **1. Tree Traversals** | Easy | Preorder, Inorder, Postorder, Level Order | Recursion + BFS |
| **2. BST Properties** | Easy | Search, Insert, Validate BST | Left < Root < Right |
| **3. Tree Depth & Height** | Easy | Max Depth, Min Depth, Height | Recursive depth calculation |
| **4. Tree Modification** | Easy→Medium | Invert Tree, Subtree Check | Recursion + pointer reassignment |
| **5. Binary Tree Paths** | Medium | Root-to-Leaf Paths | DFS + backtracking |
| **6. LCA (Lowest Common Ancestor)** | Medium | LCA in BST, LCA in Binary Tree | Recursion + BST property |
| **7. Tree Serialization** | Hard | Serialize & Deserialize, Build from traversal | Preorder + Inorder or Level Order |
| **8. Advanced Tree Problems** | Hard | Kth Smallest, Balanced Check, Flatten Tree | Advanced recursion + BST property |

---

## 🧠 The Core Mindset

### Binary Tree Node Structure
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### The 3 Key Tree Traversals (Recursive)
```python
def preorder(root):      # Root → Left → Right
    if not root: return
    print(root.val)
    preorder(root.left)
    preorder(root.right)

def inorder(root):       # Left → Root → Right  (sorted in BST)
    if not root: return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

def postorder(root):     # Left → Right → Root
    if not root: return
    postorder(root.left)
    postorder(root.right)
    print(root.val)
```

### Level Order Traversal (BFS)
```python
from collections import deque

def level_order(root):
    if not root: return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result
```

---

## 📖 Problem Mapping

| # | Pattern | Easy | Medium | Hard |
|---|---|---|---|---|
| **1. Tree Traversals** | Easy | Preorder, Inorder, Postorder | N-ary Tree Traversal | — |
| **2. BST Properties** | Easy | Search BST, Validate BST | Insert into BST, Delete Node | — |
| **3. Tree Depth** | Easy | Max Depth, Min Depth | — | — |
| **4. Tree Modification** | Easy | Invert/Flip Binary Tree | Subtree Check | Flatten Binary Tree |
| **5. Tree Paths** | Medium | — | Binary Tree Paths, Path Sum | — |
| **6. LCA** | Medium | — | LCA in BST, LCA in BT | — |
| **7. Tree Serialization** | Hard | — | Build from Preorder + Inorder | — |
| **8. Advanced** | Hard | — | Kth Smallest in BST | Balanced Binary Tree |

---

## 🚀 Placement Strategy

### Phase 1: Traversals (Day 1)
- Code all 3 recursive traversals from memory
- Code level order traversal using BFS
- Run all easy problems

### Phase 2: BST Properties (Day 2)
- Code search, insert, delete in BST
- Code validate BST (with range constraint)
- Run easy/medium problems

### Phase 3: Tree Recursion (Day 3)
- Code invert tree, subtree check
- Code max depth, min depth
- Run medium problems

### Phase 4: Tree Paths & LCA (Day 4)
- Code root-to-leaf paths
- Code LCA in BST
- Run medium problems

### Phase 5: Advanced (Day 5)
- Code serialize/deserialize
- Code kth smallest
- Run hard problems

---

## 📚 Resources

| Resource | Link |
|---|---|
| LeetCode Trees | https://leetcode.com/tag/tree/ |
| GFG Binary Tree | https://www.geeksforgeeks.org/binary-tree/ |
| GFG BST | https://www.geeksforgeeks.org/binary-search-tree/ |
| NeetCode Trees | https://neetcode.io/practice/data-structures/binary-tree |
