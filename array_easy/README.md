# 📚 Array (Easy) Learning Path — Basic to Advanced

Welcome! This is your complete guide to mastering **Arrays** (the easy level)
from scratch to interview-level problem solving. Follow this path in order.

---

## 📁 What's Inside This Folder

| File | Topic | Key Idea |
|---|---|---|
| `01_largest_element.py` | Largest element | Single-pass max scan |
| `02_second_largest_element.py` | Second largest | Two variables, one pass |
| `03_check_if_sorted.py` | Check if sorted | Compare neighbours |
| `04_check_roated_and_sorted.py` | Sorted & rotated? | Count "drops" with `% n` |
| `05_rotate_left_by_k.py` | Rotate left by k | Temp array + modulo index |
| `06_move_zeros_to_end.py` | Move zeros to end | Write pointer, then fill tail |
| `07_linear_search.py` | Linear search | Return index or -1 |
| `08_union_of_two_sorted_arr.py` | Union of 2 sorted arrays | Two-pointer merge + dedup |
| `09_find_missing_number.py` | Missing number | Gauss sum formula |
| `10_most_consecutive_ones.py` | Max consecutive ones | Running counter + reset |
| `11_single_number.py` | Single number | Brute force → hash → XOR |
| `12_longest_subarray.py` | Longest subarray with sum k | Sliding window |
| `13_longest_subarray_sum0.py` | Longest subarray with sum 0 | Prefix sum + hashmap |

Run any file with: `python 01_largest_element.py`

---

## 🗺️ The Roadmap

### Phase 1: Foundations — The Single Pass (Day 1–2)
1. Run `01_largest_element.py` — track a running `max` in one scan
2. Run `02_second_largest_element.py` — watch how duplicate large values are skipped
3. Run `03_check_if_sorted.py` — compare each element with the previous one

**Milestone:** Answer this without looking:
> Why does `second_largest` check `arr[i] < largest` before updating?
> What should `[5, 5, 5]` return as its second largest?

---

### Phase 2: Sortedness & Rotation (Day 3–4)
1. Run `04_check_roated_and_sorted.py` — count "drops" where `arr[i] > arr[(i+1) % n]`
2. Understand WHY at most 1 drop means "sorted and rotated" (0 drops = plain sorted)
3. Run `05_rotate_left_by_k.py` — understand `k %= n` (k can be bigger than n!) and
   the `(i + k) % n` index mapping

**Milestone:** Do this on paper:
> Trace `[3, 4, 5, 1, 2]` — how many drops does it have?
> Rotate `[1, 2, 3, 4, 5]` left by 7 → what do you get?
> Challenge: rewrite rotation in **O(1) space** using the reverse-technique.

---

### Phase 3: Rearrangement — The Write Pointer (Day 5–6)
1. Run `06_move_zeros_to_end.py` — `insert_pos` marks where the next non-zero goes
2. Understand the second loop: it fills the leftover tail with zeros
3. Notice the **order is preserved** — we copy, we don't shuffle!

**Milestone:** Code "Move Zeroes" from memory:
- O(n) time, O(1) extra space
- Stable (relative order of non-zeros must not change)

---

### Phase 4: Search & Merge (Day 7–8)
1. Run `07_linear_search.py` — the simplest possible O(n) search
2. Run `08_union_of_two_sorted_arr.py` — this is the **merge step of Merge Sort**!
3. Study the dedup trick: `if not union or union[-1] != x`

**Milestone:** Explain to yourself:
> Why do BOTH pointers advance when `arr1[i] == arr2[j]`?
> Why is this O(n + m), while the naive "concat + set" approach surprises people
> in interviews (order gets destroyed)?

---

### Phase 5: Math, Counting & Bits (Day 9–11)
1. Run `09_find_missing_number.py` — Gauss trick: `n(n+1)/2 - sum(arr)`
2. Run `10_most_consecutive_ones.py` — running counter, reset on 0, and note the
   final `max(max_count, current_count)` catches a run that ends at the array's tail
3. Run `11_single_number.py` — climb the 3 rungs: O(n²) brute → O(n) hash →
   O(n) time / O(1) space with XOR

**Milestone:** Solve without hints:
> LeetCode 268 (Missing Number) and LeetCode 136 (Single Number).
> Explain out loud: why does `a ^ a = 0` and `a ^ 0 = a`?

---

### Phase 6: Subarrays — Where Interviews Really Happen (Day 12–14) ⭐
This is the **gold** of array-easy — everything in `array_medium` builds on this.

1. Run `12_longest_subarray.py` — sliding window: shrink from the left while `sum > k`
2. Understand WHY the window works here: **the elements are non-negative**
3. Run `13_longest_subarray_sum0.py` — prefix sum + hashmap, with `prefixSum[0] = -1`
4. Understand the bridge: with negatives the window breaks → store prefix sums in a
   map and look up `running_sum - k` instead

**Milestone:** Solve "Longest Subarray with Sum K" (GFG) WITHOUT hints, and answer:
> When do I use a sliding window vs a prefix sum hashmap?

---

## 🧠 Mental Model Cheat Sheet

| Scenario | Technique | Why |
|---|---|---|
| "Largest / second largest" | Single-pass two-variable scan | O(n), one comparison per step |
| "Is it sorted? rotated?" | Compare neighbours, count drops with `% n` | ≤ 1 drop ⇒ sorted + rotated |
| "Move/remove elements, keep order" | Write pointer (two pointers) | In-place, O(1) extra space |
| "Merge two sorted arrays" | Two-pointer advance | Same as the merge step of Merge Sort |
| "Missing value in 1..n" | Gauss sum formula | Math cancels everything except the answer |
| "Every value appears twice except one" | XOR | `a ^ a = 0`, order doesn't matter |
| "Longest run of X" | Running counter + reset | Update max BEFORE resetting the counter |
| "Longest subarray sum = k (no negatives)" | Sliding window | Shrink from left while sum is too big |
| "Longest subarray sum = k (negatives OK)" | Prefix sum + hashmap | O(1) lookup of `running_sum - k` |
| "Does target exist / where?" | Linear search → hash set | O(n) now; O(1) with hashing later |

---

## 🔑 Pattern Recognition (The Secret to Problem Solving)

### Pattern 1: Single-Pass Scan (max / second max / running count)
**How to spot it:** "largest, second largest, most frequent run, count while traversing"

```python
def second_largest(arr):
    largest = second = -1
    for x in arr:
        if x > largest:          # new champion → old champion becomes second
            second, largest = largest, x
        elif x < largest and x > second:
            second = x           # strict < skips duplicates
    return second
```

### Pattern 2: Write Pointer (rearrange in place)
**How to spot it:** "move X to the end/front", "remove element in place", "partition"

```python
def move_zeroes(arr):
    j = 0                        # where the next NON-zero element belongs
    for x in arr:
        if x != 0:
            arr[j] = x
            j += 1
    while j < len(arr):          # fill the leftover tail
        arr[j] = 0
        j += 1
```

### Pattern 3: Two-Pointer Merge of Sorted Arrays
**How to spot it:** "union / intersection / merge / both arrays are sorted"

```python
def union(arr1, arr2):
    i = j = 0
    out = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            val, i = arr1[i], i + 1
        elif arr1[i] > arr2[j]:
            val, j = arr2[j], j + 1
        else:
            val, i, j = arr1[i], i + 1, j + 1   # equal → take once, advance both
        if not out or out[-1] != val:           # skip duplicates
            out.append(val)
    while i < len(arr1):                        # drain arr1's tail
        if not out or out[-1] != arr1[i]:
            out.append(arr1[i])
        i += 1
    while j < len(arr2):                        # drain arr2's tail
        if not out or out[-1] != arr2[j]:
            out.append(arr2[j])
        j += 1
    return out
```

### Pattern 4: Prefix Sum + Hashmap (the subarray workhorse)
**How to spot it:** "subarray / contiguous sum equals k", "negatives allowed", "sum 0"

```python
def longest_subarray_sum_k(arr, k):
    prefix = {0: -1}             # empty prefix → index -1 (subarray starting at 0)
    running = best = 0
    for i, x in enumerate(arr):
        running += x
        if running - k in prefix:               # subarray (prefix[r-k]+1 .. i) sums to k
            best = max(best, i - prefix[running - k])
        else:
            prefix[running] = i                 # keep FIRST occurrence → longest
    return best
```
> `13_longest_subarray_sum0.py` is exactly this template with `k = 0`
> (so `running - k` is just `running`).

### Pattern 5: Math / Bit Cancellation
**How to spot it:** "one element appears once, others twice", "missing number in 1..n"

- **XOR:** fold the whole array → pairs cancel (`a ^ a = 0`), the lone value survives
- **Sum:** expected `n(n+1)//2` minus actual sum = the missing value

---

## 📝 30-Day Practice Schedule

| Day | Topic | Problem Set |
|---|---|---|
| 1 | Array basics | Run `01_largest_element.py`, rewrite from memory |
| 2 | Second largest | Run `02_second_largest_element.py`, GFG Second Largest |
| 3 | Sorted check | Run `03` + `04`, count drops on paper |
| 4 | Rotate array | Run `05_rotate_left_by_k.py`, LeetCode 189 |
| 5 | Move zeros | Run `06_move_zeros_to_end.py`, LeetCode 283 ⭐ |
| 6 | Linear search | Run `07_linear_search.py`, GFG Linear Search |
| 7 | Review week 1 | Re-run files 01–07 WITHOUT looking at the code |
| 8 | Union of sorted arrays | Run `08_union_of_two_sorted_arr.py`, GFG Union |
| 9 | Missing number | Run `09_find_missing_number.py`, LeetCode 268 |
| 10 | Max consecutive ones | Run `10_most_consecutive_ones.py`, LeetCode 485 |
| 11 | Single number (XOR) | Run `11_single_number.py`, LeetCode 136 |
| 12 | Sliding window | Run `12_longest_subarray.py`, GFG Longest Subarray Sum K |
| 13 | Prefix sum + hashmap | Run `13_longest_subarray_sum0.py`, GFG Longest Subarray 0 Sum |
| 14 | Review week 2 | Solve LeetCode 283 + 136 from complete memory |
| 15 | Hashing intro | Two Sum (1) |
| 16 | Greedy single pass | Best Time to Buy and Sell Stock (121) |
| 17 | Count with a hash map | Majority Element (169) |
| 18 | Two pointers | Remove Duplicates from Sorted Array (26) |
| 19 | Two pointers backwards | Merge Sorted Array (88) |
| 20 | Sets | Intersection of Two Arrays (349) |
| 21 | Review week 3 | Re-solve all Level 1 problems |
| 22 | Sorted + two pointers | Squares of a Sorted Array (977) |
| 23 | Edge-case hunting | Valid Mountain Array (941) |
| 24 | Running max/min | Third Maximum Number (414) |
| 25 | Subarray classic ⭐ | Maximum Subarray (53) — preview of array_medium |
| 26 | Rearrangement | Rearrange Array Elements by Sign (2149) |
| 27 | Hash map + window | Contains Duplicate II (219) |
| 28 | Review week 4 | Re-solve all Level 2 problems |
| 29 | Mock interview | 45-min session, 2 problems |
| 30 | MOCK INTERVIEW DAY | 3 problems — full simulation |

---

## 💡 Advice From a Mentor

1. **Don't just read** — write every solution by hand, from an empty file
2. **Draw boxes with indices** — label `0` and `n-1`; most array bugs are off-by-one
3. **Dry run on paper** — walk `i`, `j`, `left`, `right` one row at a time
4. **Explain out loud** — the "rubber duck" method works!
5. **Spaced repetition** — redo problems at Day 7, 14, 21, 30
6. **Patterns > Memorization** — learn to RECOGNIZE "write pointer", "merge", and
   "prefix lookup" moments in a problem statement
7. **Know your costs** — most array problems are O(n) time; aim for O(1) extra
   space unless a hash map clearly buys you the O(n²) → O(n) jump
8. **Ask "are there negatives?"** — that one question decides sliding window vs
   prefix sum + hashmap, the #1 array interview trap. (Also: Python `list` is a
   DYNAMIC array — `append` is amortized O(1), but `pop(0)` is O(n); that's what
   `collections.deque` fixes — see the Queue module!)

---

## 🔗 LeetCode / GFG Problem Links (Copy into browser)

**LeetCode:**
- Move Zeroes: https://leetcode.com/problems/move-zeroes/
- Rotate Array: https://leetcode.com/problems/rotate-array/
- Check if Array Is Sorted and Rotated: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
- Missing Number: https://leetcode.com/problems/missing-number/
- Max Consecutive Ones: https://leetcode.com/problems/max-consecutive-ones/
- Single Number: https://leetcode.com/problems/single-number/
- Two Sum: https://leetcode.com/problems/two-sum/
- Best Time to Buy and Sell Stock: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
- Majority Element: https://leetcode.com/problems/majority-element/
- Remove Duplicates from Sorted Array: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
- Merge Sorted Array: https://leetcode.com/problems/merge-sorted-array/
- Intersection of Two Arrays: https://leetcode.com/problems/intersection-of-two-arrays/
- Squares of a Sorted Array: https://leetcode.com/problems/squares-of-a-sorted-array/
- Valid Mountain Array: https://leetcode.com/problems/valid-mountain-array/
- Third Maximum Number: https://leetcode.com/problems/third-maximum-number/
- Maximum Subarray: https://leetcode.com/problems/maximum-subarray/
- Rearrange Array Elements by Sign: https://leetcode.com/problems/rearrange-array-elements-by-sign/
- Contains Duplicate II: https://leetcode.com/problems/contains-duplicate-ii/

**GeeksforGeeks:**
- Largest in Array (practice): https://www.geeksforgeeks.org/problems/largest-element-in-array4009/1
- Second Largest Element in an Array: https://www.geeksforgeeks.org/dsa/find-second-largest-element-array/
- Check if an Array is Sorted: https://www.geeksforgeeks.org/dsa/program-check-array-sorted-not-iterative-recursive/
- Check if an Array is Sorted and Rotated: https://www.geeksforgeeks.org/dsa/check-if-an-array-is-sorted-and-rotated/
- Linear Search: https://www.geeksforgeeks.org/dsa/linear-search/
- Union of Two Sorted Arrays: https://www.geeksforgeeks.org/dsa/union-of-two-sorted-arrays/
- Longest Subarray With Sum K: https://www.geeksforgeeks.org/dsa/longest-sub-array-sum-k/
- Longest Subarray with 0 Sum: https://www.geeksforgeeks.org/dsa/find-the-largest-subarray-with-0-sum/

---

## ✅ Final Checklist Before Moving to Array (Medium)

- [ ] Can find largest & second largest in one pass from memory
- [ ] Can check "sorted" and "sorted & rotated" from memory
- [ ] Can rotate an array by k from memory (including `k > n`)
- [ ] Solved Move Zeroes (283) 3 times independently
- [ ] Can code the two-pointer union of sorted arrays without hints
- [ ] Can derive the Gauss sum formula and explain the XOR trick
- [ ] Solved Missing Number (268) without help
- [ ] Solved Single Number (136) without help
- [ ] Can code the sliding window template for sum = k (non-negative numbers)
- [ ] Can explain WHY sliding window fails with negatives → prefix sum + hashmap
- [ ] Can code the prefix sum + hashmap template from memory
- [ ] Built intuition for: "two pointers for order, hashing for lookup, window for
      contiguous non-negative sums"
- [ ] Solved at least 20 array problems total

> When you finish this roadmap, `array_medium` and `array_hard` will feel far
> less scary — traversal, two pointers, sliding window, and prefix sum are the
> backbone of almost every array interview problem. Next stop: Array (Medium).
> Good luck — you've got this! 🚀



