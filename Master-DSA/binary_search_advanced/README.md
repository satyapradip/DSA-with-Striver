# 📚 Binary Search — Advanced Master Guide

> A complete, placement-oriented guide to **advanced binary search** patterns.
> Builds on the basics (from the `Binary Search` folder) and covers: search on answer,
> rotated arrays with duplicates, unbounded binary search, and binary search on
> continuous domains.

---

## 🗺️ Advanced Binary Search Pattern Map

| Pattern | Difficulty | Key Problems | Key Idea |
|---|---|---|---|
| **1. Binary Search (Standard)** | Easy→Medium | LC 704, 35 | Closed interval `left <= right` |
| **2. Binary Search (Half-Open)** | Medium | LC 34 | `left < right`, `right = mid` |
| **3. Search on Answer** | Medium→Hard | LC 875, 1482, 1283 | Search the answer space, not the array |
| **4. Rotated Sorted Array** | Medium | LC 33, 81, 153 | Exactly one half is sorted |
| **5. Unbounded Binary Search** | Medium | LC 278, 65 | Search space unknown ahead of time |
| **6. Binary Search on Continuous** | Hard | LC 4, 1283 | Search over floats/ratios |

---

## 🧠 The Two Core Templates

### Template 1: Closed Interval (`left <= right`)
```python
def binary_search_closed(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

**Key insights:**
- `left` and `right` are **inclusive** indices
- Loop ends when `left > right` (interval empty)
- `mid` can be `left` or `right` (careful with overflow in other languages)

### Template 2: Half-Open Interval (`left < right`)
```python
def binary_search_half_open(nums, target):
    left, right = 0, len(nums)  # right is EXCLUDED
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return -1
```

**Key insights:**
- `right` is **exclusive** (interval is `[left, right)`)
- `mid` is always `left` when `left = right - 1`
- Great for **insertion positions** and **lower/upper bounds**

---

## 🔍 When to Use Binary Search

| Signal | Use |
|---|---|
| **Sorted array + search for a value** | Standard binary search |
| **Search for insertion position** | Half-open template |
| **Find first/last occurrence** | Two binary searches |
| **Sorted & rotated** | Find pivot, then binary search |
| **Answer is "minimize X" or "maximize X"** | Binary search on answer |
| **Can you check "is it possible in K steps?"** | Search on answer |
| **Search space unknown but monotonic** | Unbounded binary search |

---

## 📊 Complexity Cheat Sheet

| Scenario | Time | Space |
|---|---|---|
| Standard binary search | O(log n) | O(1) |
| Search on answer | O(log M) where M = answer range | O(1) |
| Rotated sorted | O(log n) | O(1) |
| Unbounded binary search | O(log n) | O(1) |
| Continuous binary search | O(log(1/eps)) iterations | O(1) |

---

## 📚 Resources

| Resource | Link |
|---|---|
| LeetCode Binary Search | https://leetcode.com/tag/binary-search/ |
| LeetCode "Search a 2D Matrix" | https://leetcode.com/problems/search-a-2d-matrix/ |
| LeetCode "Find Minimum in Rotated Sorted Array" | https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/ |
| GFG Binary Search | https://www.geeksforgeeks.org/binary-search/ |
