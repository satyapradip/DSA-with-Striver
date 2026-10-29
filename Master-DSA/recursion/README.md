# 📚 Recursion — Master Guide

> A complete, placement-oriented guide to **recursion** — the foundation of
> Dynamic Programming and Tree/Graph traversals. Covers: recursion fundamentals,
> backtracking, and advanced recursive patterns.

---

## 🗺️ Recursion Pattern Map

| Pattern | Difficulty | Key Problems | Key Idea |
|---|---|---|---|
| **1. Basic Recursion** | Easy | Factorial, Fibonacci, Sum of first N | Base case + recursive case |
| **2. Recursion with Array/List** | Easy→Medium | Print 1..N, Reverse array, Subset sum | Manipulate indices |
| **3. Backtracking** | Medium→Hard | N-Queens, Combination Sum, Permutations | Try → Undo → Try again |
| **4. Recursion + Memoization (DP)** | Hard | Fibonacci with memoization, Climbing stairs, Longest increasing subsequence | Store results to avoid re-computation |
| **5. Advanced Recursion** | Hard | Subset generation, Permutations, Partition to K equal sum subsets | Complex state tracking |

---

## 🧠 The Core Recursion Mindset

### The 3 Steps of Every Recursive Function

1. **Base Case** — When to stop (without base case → infinite recursion → stack overflow)
2. **Recursive Case** — How to break the problem into smaller subproblems
3. **Combine** — How to merge subproblem solutions into the final answer

### Anatomy of a Recursive Function

```python
def recursive_function(data, parameter):
    # 1. Base case
    if base_condition(data):
        return base_result

    # 2. Recursive case
    smaller_data = reduce_data(data, parameter)
    result = recursive_function(smaller_data, parameter)

    # 3. Combine
    return combine(result, data)
```

---

## 📐 Template 1: Count/Sum Recursion

```python
def count_or_sum(arr, index=0):
    # Base case: reached end of array
    if index == len(arr):
        return 0

    # Recursive case: count current + rest
    return 1 + count_or_sum(arr, index + 1)
```

### Template 2: Boolean Recursion (Search/Check)

```python
def check(arr, index=0, target=None):
    # Base case: reached end
    if index == len(arr):
        return False  # or True, depending on the problem

    # Recursive case: check current OR rest
    return (arr[index] == target) or check(arr, index + 1, target)
```

### Template 3: Array Manipulation Recursion

```python
def reverse_array(arr, left, right):
    # Base case: crossed pointers
    if left >= right:
        return arr

    # Swap and recurse
    arr[left], arr[right] = arr[right], arr[left]
    return reverse_array(arr, left + 1, right - 1)
```

---

## 📖 Problem Mapping

| # | Pattern | Easy | Medium | Hard |
|---|---|---|---|---|
| **1. Basic Recursion** | Print N times, Print 1..N, Sum of N, Factorial, Fibonacci | Print N, Sum of N, Factorial, Fibonacci | — |
| **2. Array Recursion** | Reverse array, Check sorted, Check sorted & rotated | Reverse array, Check if sorted & rotated | — |
| **3. Backtracking** | — | N-Queens (medium), Combination Sum (medium) | N-Queens II, Generate parentheses (hard) |
| **4. Recursion + Memoization** | — | Fibonacci with cache, Climbing stairs | Partition to K equal sum subsets |
| **5. Advanced Recursion** | — | — | Print all subsequences with sum K |

---

## 🔗 Next After Recursion

After mastering recursion, move to:
1. **Linked Lists** — `Master-DSA/linked_list/` *(to be created)*
2. **Stacks & Queues** — `Master-DSA/stack_queue/`
3. **Trees (BST)** — `Master-DSA/trees/`
4. **Graphs (BFS/DFS)** — `Master-DSA/graphs/`
5. **Dynamic Programming** — `Master-DSA/dynamic_programming/`

---

## ✅ Final Checklist (Before Moving On)

- [ ] Can define recursion in one sentence ("a function that calls itself")
- [ ] Can write factorial, Fibonacci, sum from memory
- [ ] Can reverse an array using recursion
- [ ] Can check if an array is sorted using recursion
- [ ] Can trace a recursion tree on paper
- [ ] Understands the call stack and how recursion uses memory
- [ ] Knows the difference between recursion and iteration (time/space trade-off)
- [ ] Can explain when recursion is preferred over iteration
