# Recursion

A comprehensive tutorial and problem set on recursion in Python, progressing from functional recursion fundamentals to advanced combinatorial problems.

## What is Recursion?

Recursion is a programming technique where a function **calls itself** to solve a smaller version of the same problem. Every recursive solution has two parts:

- **Base Case** - the condition that stops the recursion (the "answer is trivial" case).
- **Recursive Case** - the function calls itself on a smaller sub-problem, moving toward the base case.

### Mental Model

Think of recursion like a stack of nested boxes: you don't open the inner box until you're done with the outer one, and you solve each layer only when the smaller layers beneath it are already solved.

```
f(n) = f(n-1) + something    # recursive case
f(0) = base_answer             # base case
```

### Anatomy of a Recursive Function

```
def solve(subproblem):
    if (base condition):       # 1. BASE CASE - stop recursing
        return answer
    # 2. RECURSIVE CASE - reduce the problem and call self
    return solve(smaller_subproblem)
```

Key rules:
1. **Always define a base case** - otherwise you get infinite recursion (stack overflow).
2. **Ensure progress toward the base case** - every recursive call should shrink the problem.
3. **Combine results** of the recursive call with the current frame's work.

### The Call Stack (function call stack)

Python keeps each recursive call's local variables on the **call stack**. When the base case returns, the stack "unwinds" and returns values back up. Deep recursion risks `RecursionError` (maximum depth exceeded) — Python's default limit is 1000.

## Subfolder: functional_recursion

Functional recursion means the function does its work during the **unwinding** phase (returns, doesn't print on the way down). Useful for reversing, slicing, aggregations.

| File | Problem | Technique |
|------|---------|-----------|
| `01_reverse_array.py` | Reverse an array in place | Two-pointer + recursion (swap outer, recurse inner) |
| `02_check_if_string_is_palindrome.py` | Check string is palindrome | Compare outer chars, recurse inner substring |
| `03_nth_fibonacci.py` | N-th Fibonacci number | `F(n) = F(n-1) + F(n-2)`, bases 0 and 1 |
| `04_print_all_subsequences.py` | Generate all subsequences of an array | Pick / not-pick at each index |
| `05_print_all_subSequences_with_sum_k.py` | Subsequences summing to `k` | Pick / not-pick with running sum pruning |

## Root Files: Advanced Problems

- `01_Combination Sum.py` — LeetCode 39. Find all unique combinations from `candidates` (unlimited reuse) summing to `target`. Shows both pick/not-pick and for-loop recursion patterns.
- `02_N_Queens.py` — LeetCode 51. Place N queens on N×N board with no attacks; classic backtracking with collision checks.

## Core Recursion Patterns

### 1. Functional Recursion (return, don't print)
```python
def reverse(s, i, j):
    if i >= j:
        return
    s[i], s[j] = s[j], s[i]
    reverse(s, i + 1, j - 1)
# Work happens on the way DOWN; nothing to combine on way up.
```

### 2. Parameterized Recursion (carry state)
```python
def subseq(i, current, arr, target_sum, result):
    if i == len(arr):
        if sum(current) == target_sum:
            result.append(list(current))
        return
    current.append(arr[i])
    subseq(i + 1, current, arr, target_sum, result)   # PICK
    current.pop()
    subseq(i + 1, current, arr, target_sum, result)    # NOT PICK
```

### 3. Backtracking (Pick → recurse → un-pick)
The universal template for "explore all configurations":
```python
def backtrack(start, current):
    if goal_reached():
        result.append(list(current))
        return
    for i in range(start, n):
        current.append(arr[i])          # DO
        backtrack(i, current)            # RECURSE
        current.pop()                   # UNDO (backtrack)
```

### 4. Pick / Not-Pick Decision Tree
Each element forks two branches (include / exclude), yielding `2^n` leaves for n elements.

### 5. Subset / Combinatorial Generation
- **Subsets (power set)**: pick/not-pick over indices.
- **Combinations**: for-loop with start index to enforce ordering.
- **Permutations**: mark used elements (or swap in place).

## Common Recursion Pitfalls

- **Missing base case** → infinite recursion → `RecursionError: maximum recursion depth exceeded`.
- **No progress toward base case** (e.g. not decrementing n) → infinite recursion.
- **Mutating shared state** without backtracking (forgetting `current.pop()`).
- **Appending references** instead of copies (`result.append(current)` instead of `result.append(current[:])`).
- **Exceeding recursion limit** for large n → raise with `sys.setrecursionlimit`, or convert to iterative.

## Complexity Tips

- Recursion tree of branching factor `b` and depth `d` has up to `b^d` nodes.
- Each node may do O(k) work; total O(k * b^d).
- Space = O(d) stack + output storage.

## Practice Problems (LeetCode)

1. **Pow(x, n)** (LeetCode 50) - fast exponentiation via recursion (`x^n = x^(n/2) squared`).
2. **Subsets** (LeetCode 78) - generate all subsets.
3. **Combination Sum** (LeetCode 39) - unlimited reuse.
4. **Combinations** (LeetCode 77) - `C(n, k)`.
5. **Permutations** (LeetCode 46) - all arrangements.
6. **N-Queens** (LeetCode 51) - backtracking placement.
7. **Word Search** (LeetCode 79) - DFS on grid.
8. **Course Schedule** (LeetCode 207) - cycle detection in DAG.
9. **Generate Parentheses** (LeetCode 22).
10. **Fibonacci with memoization** (top-down DP).
11. **Restore IP Addresses** (LeetCode 93).
12. **Letter Combinations of a Phone Number** (LeetCode 17).

## Run

```bash
cd advance_Recursion
python functional_recursion\01_reverse_array.py
python "01_Combination Sum.py"
```