# 📚 Linked Lists — Master Guide

> A complete, placement-oriented guide to **Linked Lists** — the foundational
> data structure for dynamic memory allocation. Covers: singly linked lists,
> doubly linked lists, and the key patterns you need for interviews.

---

## 🗺️ Linked List Pattern Map

| Pattern | Difficulty | Key Problems | Key Idea |
|---|---|---|---|
| **1. Singly Linked List Basics** | Easy | Insert, Delete, Traverse, Length | Node + pointer manipulation |
| **2. Fast & Slow Pointers** | Easy→Medium | Middle of LL, Cycle detection | Two pointers moving at different speeds |
| **3. Reversal** | Easy→Medium | Reverse LL, Reverse in groups | Update pointers in-place |
| **4. Two Pointers (Sorted)** | Medium | Merge two sorted LLs, Remove Nth from end | One pointer tracks position |
| **5. In-Place Manipulation** | Easy→Medium | Delete node, Remove duplicates | Modify pointers directly |
| **6. Advanced Linked Lists** | Hard | Palindrome check, Sort LL, Split/Interleave | Complex pointer manipulation |

---

## 🧠 The Core Linked List Mindset

### The Node Structure
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val      # Data
        self.next = next    # Pointer to next node
```

### The 3 Golden Rules of Linked Lists
1. **Always check for None** — `next` can be None
2. **Return the head** — always return the changed head if it changed
3. **Use dummy node** for head manipulation (avoids special cases)

### Dummy Node Pattern
```python
dummy = ListNode(0)
dummy.next = head
prev = dummy
while prev.next:
    # ... manipulation ...
    prev = prev.next
return dummy.next  # Return the new head
```

---

## 📐 Key Templates

### Template 1: Fast & Slow Pointers
```python
def middle_of_linked_list(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow  # slow is the middle
```

### Template 2: Reverse a Linked List
```python
def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next  # Save next
        current.next = prev        # Reverse pointer
        prev = current             # Move prev forward
        current = next_node        # Move current forward
    return prev  # New head
```

### Template 3: Merge Two Sorted Linked Lists
```python
def merge_two_sorted_lists(l1, l2):
    dummy = ListNode(0)
    tail = dummy
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 if l1 else l2
    return dummy.next
```

### Template 4: Remove Nth Node from End
```python
def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n + 1):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next  # Remove
    return dummy.next
```

---

## 📖 Problem Mapping

| # | Pattern | Easy | Medium | Hard |
|---|---|---|---|---|
| **1. Singly LL Basics** | Insert, Delete, Traverse | Reverse LL, Middle of LL, Length | Delete middle, Sort LL |
| **2. Fast & Slow** | Middle of LL, Cycle detection | Palindrome check, Find loop start | — |
| **3. Reversal** | Reverse LL, Reverse in groups | — | — |
| **4. Two Pointers (Sorted)** | Merge two sorted LLs | Remove Nth from end | — |
| **5. In-Place Manipulation** | Delete node, Remove duplicates | — | Split/Interleave, Rotate |

---

## 🚀 Placement Strategy

### Phase 1: Basics (Day 1)
- Run `01_basic.py` to understand the node structure
- Code `02_operations_in_LL.py` from memory
- Understand `03_traversal_of_singly_LL.py`

### Phase 2: Core Patterns (Day 2)
- Code `11_Reverse_a_Linked_List.py` from memory
- Code `12_middle_of_LL.py` using fast/slow pointers
- Code `13_detect_loop_in_LL.py` (Floyd's cycle detection)

### Phase 3: Two Pointers (Day 3)
- Code `18_Remove Nth node from the back of the LL.py` using two pointers
- Code `20_Sort a Linked List.py` (merge sort)

### Phase 4: Advanced (Day 4)
- Code `21_Add Two Numbers.py` (linked list as numbers)
- Code `15_Check if a LinkedList is Palindrome or Not.py`

---

## 📚 Resources

| Resource | Link |
|---|---|
| LeetCode Linked List | https://leetcode.com/tag/linked-list/ |
| GFG Singly Linked List | https://www.geeksforgeeks.org/singly-linked-list/ |
| GFG Doubly Linked List | https://www.geeksforgeeks.org/doubly-linked-list/ |
| NeetCode Linked List | https://neetcode.io/practice/data-structures/linked-list |

---

## ✅ Final Checklist

- [ ] Can define a linked list node from memory
- [ ] Can reverse a linked list in O(1) space
- [ ] Can find the middle using fast/slow pointers
- [ ] Can detect a cycle (Floyd's algorithm)
- [ ] Can remove Nth node from end in one pass
- [ ] Can merge two sorted linked lists
- [ ] Can add two numbers represented as linked lists
- [ ] Can find the start of a cycle in a linked list
- [ ] Can sort a linked list (merge sort on LL)
- [ ] Can check if a linked list is a palindrome
