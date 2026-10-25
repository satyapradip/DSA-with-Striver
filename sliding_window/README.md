# 📚 Sliding Window — Master Guide

> A complete, placement-oriented guide to the **Sliding Window** pattern.
> This folder is designed to take you from **concept → pattern recognition → 3 rungs of mastery (brute → better → optimal) → placement confidence**.

---

## 🔍 What is Sliding Window?

**Sliding Window** is a pattern where instead of recomputing a result over and over (e.g., re-calculating the sum of a subarray from scratch each time), we **reuse and update** a running computation as the window "slides" across the array/string.

> **Core idea:**  
> Instead of two nested loops (`O(n²)`), we maintain a *window* with a `left` and `right` pointer, expanding and shrinking it in a single pass (`O(n)`).

### When to use it
| Signal | What to do |
|---|---|
| "Find **longest/shortest** subarray / substring with sum / product / avg / max / min" | Sliding Window |
| "Count subarrays with sum ≤ K" | Fixed or Variable window |
| "Maximum average subarray of size K" | Fixed-size window |
| "Sequence of consecutive integers" | Running sum / two pointers |
| **Negatives present** + sum problem | Sliding window **fails** → use prefix sum + hashmap |

### Window Types
| Type | Description | Example |
|---|---|---|
| **Fixed-size** | Window size is constant `K` | Max subarray sum of size `K` |
| **Variable-size** | Window grows/shrinks based on condition | Longest substring without repeating chars |
| **Sliding + Two Pointers** | One pointer tracks the "best start", other tracks end | Min window substring |

---

## 🧠 The Master Template (Always Adopt)

```python
def sliding_window(nums, target):
    n = len(nums)
    left = 0
    current_sum = 0          # running window sum
    max_len = 0              # or min_len = inf

    for right in range(n):
        current_sum += nums[right]      # expand right

        # shrink window while condition is violated
        while condition_violated(current_sum):
            current_sum -= nums[left]   # shrink left
            left += 1

        # update answer (longest / shortest / max / min)
        update_answer(current_sum, left, right)

    return max_len   # or result
```

**Key rule:** The window only moves forward (`left ≤ right ≤ right+1`), so the whole algorithm is **O(n)**.

---

## 📁 Folder Structure — What's Inside

| Folder | Purpose |
|---|---|
| `easy/` | Foundational sliding window problems (fixed window, basic variable window) |
| `medium/` | Variable windows, min/max subarray, substring problems |
| `hard/` | Advanced: product-based, complex constraints, binary arrays |
| `PATTERNS.md` | How to spot Sliding Window in array problems — copied in this guide |
| `FAST-TRACK.md` | 1-page placement revision checklist |

---

## 🚀 How to Master Sliding Window (Placement Strategy)

### Phase 1: Learn the Concept (Day 1)
1. Read this README fully.
2. Understand the **master template** above.
3. Trace `01_max_consecutive_ones.py` on paper with `[1,1,0,1,1,1,0,1,1]`.
4. Run all 3 rungs (`brute_better_optimal`) for `02_max_subarray_sum_fixed_size.py`.

### Phase 2: Pattern Recognition (Day 2)
1. Open `PATTERNS.md` and memorize the **recognition checklist**.
2. Solve 3 easy problems WITHOUT looking at the code.
3. Time yourself: 15 minutes per problem.

### Phase 3: Build Speed (Days 3–5)
1. Practice medium problems using **only the template**.
2. Record the time taken for each:
   - Easy: 10 min
   - Medium: 20 min
   - Hard: 30+ min
3. Re-solve each problem after 24 hours (spaced repetition).

### Phase 4: Placement Drill (Day 6–7)
1. Switch to **blind solving**: no editor, no hints, just pen/paper or mental running.
2. Simulate real interview conditions:
   - 30–45 min per medium problem
   - 45–60 min per hard problem
3. Track your **accuracy + speed**:
   - 📌 Use `FAST-TRACK.md` as a final one-page cheat sheet

---

## 🧪 When to Use Sliding Window vs Alternatives

| Problem Type | Best Approach |
|---|---|
| Fixed window sum / product | Sliding window (O(n)) |
| Longest/shortest substring without repeating | Sliding window (O(n)) |
| Sum ≤ K, count subarrays | Prefix sum + hashmap (O(n)) — *only if negatives exist* |
| All-negative array | Prefix sum / Kadane |
| Two separate conditions | Two pointers / sliding window combined |
| Non-contiguous subarray | DP / greedy, NOT sliding window |

---

## 📖 LeetCode & GFG Problem Mapping

### Easy (Start Here)
| # | Problem | Platform |
|---|---|---|
| 1 | Max Consecutive Ones | LC 485 |
| 2 | Max Subarray Sum of Size K | GFG / LC 209 (fixed window) |
| 3 | Longest Substring Without Repeating Characters | LC 3 |
| 4 | Count Occurrences of Anagram | GFG |

### Medium
| # | Problem | Platform |
|---|---|---|
| 1 | Subarray Sum Equals K | LC 560 |
| 2 | Minimum Size Subarray Sum | LC 209 |
| 3 | Longest Substring with At Most K Distinct Characters | LC 340 |
| 4 | Minimum Window Substring | LC 76 |
| 5 | Count Subarrays With Product Less Than K | LC 713 |

### Hard
| # | Problem | Platform |
|---|---|---|
| 1 | Minimum Window Sorted | GFG |
| 2 | Count Number of Nice Subarrays | LC 1248 |
| 3 | Shortest Subarray with Sum at Least K | LC 862 |

---

## ✅ Final Checklist (Before Moving to Hard Arrays)

- [ ] Can trace the sliding window template on paper in <5 minutes
- [ ] Can identify "sliding window" vs "prefix sum + hashmap" within 10 seconds
- [ ] Can code `04_longest_substring_without_repeating_chars.py` from memory
- [ ] Can code `05_min_size_subarray_sum.py` from memory
- [ ] Can code `06_minimum_window_substring.py` with the `need` map pattern
- [ ] Know when sliding window **fails** (negatives) and what to use instead
- [ ] Solved all 10 easy/medium problems in <45 min total
- [ ] Can explain "why O(n) not O(n²)" out loud

> **Pro tip:** The goal is not to memorise code — it's to **recognise the pattern in 30 seconds** and then *adapt* the template. That's what lands you interview offers. 🚀
