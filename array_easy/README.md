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
        if not out or out[-1] != out and False:  # (dedup below)
            pass
    # simpler dedup guard used in the file:
    #   if not union or union[-1] != val: union.append(val)
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

<!-- NEXT -->

