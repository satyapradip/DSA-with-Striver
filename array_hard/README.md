# 📚 Array (Hard) Learning Path — Basic to Advanced

Welcome! This is your complete guide to mastering **Arrays** (the hard level)
from scratch to interview-level problem solving. Follow this path in order.

> **Prerequisite:** finish `array_easy` and `array_medium` first — sliding
> window, two pointers, prefix sums, and matrix traversal are assumed
> knowledge here. Hard level means: **multiple approaches per problem**, and
> you must be able to justify every complexity.

---

## 📁 What's Inside This Folder

| File | Topic | Key Idea |
|---|---|---|
| `01_pascal_triangle.py` | Pascal's Triangle (LC 118) | Build row `i` from row `i-1` |
| `02_majority_element2.py` | Majority Element II — appear > ⌊n/3⌋ | Hash counts → Boyer-Moore (2 candidates) |
| `03_3-sum.py` | 3Sum (LC 15) | Sort → fix `i` → two pointers + dedup |
| `04_4Sum.py` | 4Sum (LC 18) | Fix `i, j` → two pointers + min/max pruning |

Run any file with: `python 01_pascal_triangle.py`

> `03_3-sum.py` prints a demo comparing all four of its approaches — run it and
> confirm every approach returns the same triplets
> (`[(-1, -1, 2), (-1, 0, 1)]`).

---

## 🗺️ The Roadmap

### Phase 1: Pascal's Triangle — Build From the Previous Row (Day 1–3)
1. Run `01_pascal_triangle.py` — every row starts as `[1] * (i + 1)`, then the
   middle cells get `row[j] = result[i-1][j-1] + result[i-1][j]`
2. Understand WHY the edges stay `1` — the `for j in range(1, i)` loop simply
   never touches them
3. Notice the file **ends at a comment**: `# Approach 2: Return the Row` —
   Approach 2 is your TODO! Implement it yourself: return ONLY the `numRows`-th
   row (LeetCode 119) using `O(k)` extra space with the in-place
   `row[j] += row[j-1]` trick

**Milestone:** Answer without looking:
> How many total cells does an n-row triangle have? (O(n²) total — and you
> cannot beat that, it's the output size.)
> Row `i` of Pascal's triangle = which binomial coefficients? (`C(i, 0) … C(i, i)`)

---

### Phase 2: Majority Element II — Boyer-Moore Voting ⭐ (Day 4–7)
1. Run `02_majority_element2.py` — note the file defines `majority_Element2`
   **twice**. Python keeps the LAST definition, so the Boyer-Moore version is
   the one that "wins". Both are correct: Approach 1 (hash map) runs first in
   the file, Approach 2 (Boyer-Moore) overrides it
2. Understand the pigeonhole: only **2** elements can appear more than `n/3`
   times — 3 such elements would need more than `n` total slots
3. Study the vote: two `(candidate, count)` pairs. An empty seat takes the new
   number; otherwise BOTH counts decrement (one vote can't feed two candidates)
4. Study the **VERIFY pass** — candidates are only *potential* answers; an
   independent re-count confirms them
5. Generalize in your head: for "> n/k" you keep `k - 1` candidates

**Milestone:** Explain out loud:
> Why must we re-count at the end? What breaks if we skip the verify pass?
> Trace `[1, 1, 1, 2, 2, 2, 3, 3]` — which two candidates survive the vote?
> Rewrite Boyer-Moore for "> n/4" from memory (hint: 3 candidate slots).

---

### Phase 3: 3Sum — Sort + Two Pointers (Day 8–12) ⭐
1. Run `03_3-sum.py` — climb the 4 rungs: brute force `O(n³)` → hashing
   `O(n²)` (fix `i`, solve 2Sum with a `seen` set) → two pointers `O(n²)` →
   `optimal` (which is just the two-pointer version — the standard answer)
2. Understand WHY sorting makes two pointers legal: too small → move `left`
   rightward, too big → move `right` leftward. Without sorting you have no
   direction to walk
3. Study the **dedup rules** — the heart of the problem:
   - after fixing `i`: `if i > 0 and nums[i] == nums[i-1]: continue`
   - after a hit: skip equal `left` and equal `right` values before moving on
4. Dry-run `[-1, 0, 1, 2, -1, -4]` on paper — you must land on exactly
   `[(-1, -1, 2), (-1, 0, 1)]`, same as the demo output

**Milestone:** Code `three_sum_two_pointers` from memory:
- Sort first, dedup at BOTH levels, `O(n²)` time, `O(1)` extra space
- Solve LeetCode 15 in under 30 minutes, no hints

---

### Phase 4: 4Sum — One More Loop + Pruning (Day 13–17)
1. Run `04_4Sum.py` — the same 4 rungs one level deeper: brute `O(n⁴)` →
   hashing `O(n³)` (fix `i, j`, 2Sum with a set) → two pointers `O(n³)` →
   `Solution.fourSum`, the LeetCode-ready class version
2. Study the **pruning** in `Solution.fourSum` — this is the new hard-level
   skill:
   - `nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target` → **`break`** —
     the smallest possible completion is already too big, and every later `i`
     is bigger still
   - `nums[i] + nums[-1] + nums[-2] + nums[-3] < target` → **`continue`** —
     this `i` can never reach the target, but the next `i` still might
3. Notice the dedup rules are identical to 3Sum, just applied at TWO fixed
   levels (`i` and `j`) — `j`'s check is `j > i + 1`, not `j > 0`

**Milestone:** Solve without hints:
> LeetCode 18 (4Sum) in under 35 minutes, then LeetCode 16 (3Sum Closest) —
> closest tracks the `min` difference instead of exact equality, and must NOT
> dedup-skip before checking. Explain break vs continue for pruning.

---

### Phase 5: The kSum Generalization & Review (Day 18–20)
1. Write ONE helper `two_sum(nums, start, target)`, then rebuild 3Sum, 4Sum,
   and a generic `kSum(nums, k, target)` on top of it — recursion style. This
   is the template interviews actually reward
2. Re-run all four files and re-solve LC 15 + LC 18 from complete memory
3. Say the complexities out loud and precisely:
   - Pascal: `O(n²)` total cells generated (each cell is O(1) work)
   - Boyer-Moore: `O(n)` time, `O(1)` space (the hash-map approach is
     `O(n)` time but `O(n)` space — that's WHY voting exists)
   - 3Sum: `O(n²)` — sorting `O(n log n)` + n fix-loops × two-pointer sweep
   - 4Sum: `O(n³)` — two fixed loops × two-pointer sweep

**Milestone:** three problems, no breaks, one sitting:
> LC 15 → LC 18 → LC 16. If that felt routine, you're done with arrays.

---

## 🧠 Mental Model Cheat Sheet

| Scenario | Technique | Why |
|---|---|---|
| "Next Pascal row from the row above" | `row[j] = prev[j-1] + prev[j]` | Each cell is the sum of its two parents |
| "Elements appearing > ⌊n/3⌋ times" | Boyer-Moore: 2 candidates + verify pass | Pigeonhole: at most 2 such elements exist |
| "Elements appearing > ⌊n/k⌋ times" | Boyer-Moore: `k-1` candidates + verify | Same vote, more candidate slots |
| "k numbers that sum to target" | Sort → fix `k-2` indices → two pointers | Sorting turns the search into a directed walk |
| "All UNIQUE triplets/quadruplets" | Sort FIRST, skip duplicates at every level | Sorting clusters equals, so one skip removes them |
| "Search space explodes (n⁴ loops)" | Min/max pruning after each fixed index | `break`/`continue` kills hopeless branches early |
| "Is this approach even correct?" | Run every approach, print side by side | Proves equivalence — exactly the demo in `03_3-sum.py` |
| "O(n) time AND O(1) space majority" | Boyer-Moore voting instead of a hash map | Trading certainty for a verify pass buys O(1) space |

---

## 🔑 Pattern Recognition (The Secret to Problem Solving)

### Pattern 1: The kSum Template (sort → fix → two pointers)
**How to spot it:** "find k numbers that sum to target", "return all unique
triplets / quadruplets", "4Sum", "closest triplet"

```python
def two_sum(nums, start, target):
    lo, hi = start, len(nums) - 1
    while lo < hi:
        s = nums[lo] + nums[hi]
        if s == target:
            lo += 1                                  # collect the hit,
            hi -= 1                                  # then move BOTH
            while lo < hi and nums[lo] == nums[lo - 1]:   # skip duplicates
                lo += 1
            while lo < hi and nums[hi] == nums[hi + 1]:   # skip duplicates
                hi -= 1
        elif s < target:
            lo += 1                                  # too small → grow the sum
        else:
            hi -= 1                                  # too big → shrink the sum
```
> `03_3-sum.py` and `04_4Sum.py` are exactly this loop wrapped inside one or
> two fixed-index `for` loops. Learn it once, get 3Sum / 4Sum / kSum free.

### Pattern 2: Boyer-Moore Majority Voting
**How to spot it:** "more than n/2 … n/3 … n/k times", AND the constraints
demand **O(n) time + O(1) space**

```python
def majority_n3(nums):
    c1 = c2 = None          # two POTENTIAL candidates
    n1 = n2 = 0
    for x in nums:
        if x == c1:   n1 += 1
        elif x == c2: n2 += 1
        elif n1 == 0: c1, n1 = x, 1        # empty seat → sit down
        elif n2 == 0: c2, n2 = x, 1
        else:         n1 -= 1; n2 -= 1     # both lose one supporter
    # ALWAYS run a verify pass — candidates only "might" be majority
    # (see 02_majority_element2.py, Approach 2)
```

### Pattern 3: Pruning With Sorted Bounds
**How to spot it:** sorted array + exact-sum combination search + big `n` +
time-limit worries

- **smallest** possible completion `> target` → **`break`** out of the fixed
  loop (every remaining prefix is even larger)
- **largest** possible completion `< target` → **`continue`** (this prefix is
  too small; a later one might not be)

> That's the trick inside `Solution.fourSum` in `04_4Sum.py` — four lines that
> skip huge dead branches before the inner while-loop ever runs.

### Pattern 4: Generate From the Previous State (Pascal)
**How to spot it:** "triangle / grid where each cell comes from cells in the
row above"

- keep the previous row, build the next one from it — edges first, middles after
- `result[i]` only depends on `result[i-1]`: this is **dynamic programming in
  disguise**, the same shape as grid-DP and path-count problems you'll meet later

---

## 📝 30-Day Practice Schedule

| Day | Topic | Problem Set |
|---|---|---|
| 1 | Pascal's Triangle | Run `01_pascal_triangle.py`, solve LC 118 |
| 2 | Pascal row k | Finish the file's `# Approach 2` TODO, LC 119 |
| 3 | Majority II (hashing) | Run `02_majority_element2.py`, trace BOTH definitions |
| 4 | Boyer-Moore voting ⭐ | Rewrite Approach 2 from memory, LC 229 |
| 5 | Verify pass intuition | GFG Majority Element – More Than n/3 |
| 6 | Generalize to n/k | Keep `k-1` candidates — explain on paper |
| 7 | Review week 1 | Re-run files 01–02, rewrite both blind |
| 8 | 3Sum brute + hashing | Run `03_3-sum.py`, compare all 4 outputs |
| 9 | 3Sum two pointers | Trace `left`/`right` on paper: `[-1, 0, 1, 2, -1, -4]` |
| 10 | 3Sum from memory ⭐ | LeetCode 15, timed first try (≤ 30 min) |
| 11 | Dedup discipline | Re-solve LC 15, say every skip out loud |
| 12 | 3Sum variant | LeetCode 16 (3Sum Closest) |
| 13 | 4Sum brute + hashing | Run `04_4Sum.py`, compare all 4 approaches |
| 14 | Review week 2 | Re-solve LeetCode 15 without looking |
| 15 | 4Sum two pointers | Trace the `i → j → left/right` loops on paper |
| 16 | 4Sum from memory ⭐ | LeetCode 18, timed first try (≤ 35 min) |
| 17 | Pruning | Re-code with min/max pruning; explain `break` vs `continue` |
| 18 | 4Sum II (hash map style) | LeetCode 454 |
| 19 | Generic kSum | Write `two_sum(start)` + `kSum(k, target)` from memory |
| 20 | Review week 3 | Re-run all 4 files, re-solve LC 18 blind |
| 21 | Backfill: foundation | LeetCode 1 (Two Sum — the seed of every kSum) |
| 22 | Backfill: medium | LeetCode 31 (Next Permutation) |
| 23 | Backfill: medium | LeetCode 53 (Maximum Subarray — keep Kadane sharp) |
| 24 | Backfill: medium | LeetCode 54 (Spiral Matrix — index-boundary practice) |
| 25 | GFG practice | GFG Pascal Triangle |
| 26 | GFG practice | GFG All Triplets with Zero Sum |
| 27 | GFG practice | GFG 4 Sum – All Quadruples |
| 28 | Timed drill | 3Sum in 20 min + 4Sum in 30 min, zero hints |
| 29 | Mock interview | 45-min session, 2 problems |
| 30 | MOCK INTERVIEW DAY | 3 problems — full simulation |

---

## 💡 Advice From a Mentor

1. **Don't just read** — write every solution by hand, from an empty file
2. **Sort first** — the moment you sort, "find k numbers summing to target"
   stops being a search and becomes a directed walk with two pointers
3. **Dedup at every level** — skip equal values after fixing `i`, after fixing
   `j`, and after every pointer hit; duplicate triplets are THE #1 reason people
   fail 3Sum/4Sum on the first try
4. **Boyer-Moore candidates are only POTENTIAL answers** — always run the
   verify pass, and be able to prove the pigeonhole ("why at most 2 for n/3?")
5. **Prune like it matters** — after sorting, min/max checks turn O(n⁴) code
   into something that passes the judge; know when `break` is safe (loop order
   makes prefixes only larger) vs when you need `continue`
6. **Draw boxes with indices** — label `i`, `j`, `left`, `right`; dry-run one
   row at a time; most bugs are off-by-one or a forgotten skip
7. **Spaced repetition** — redo problems at Day 7, 14, 21, 30 (the schedule
   bakes this in)
8. **Patterns > Memorization** — 3Sum, 4Sum, and kSum are ONE template;
   n/2, n/3, and n/k majority are ONE algorithm; Pascal is one row-builder
9. **Know your file quirks** — `02_majority_element2.py` defines
   `majority_Element2` twice (the last definition wins; rename them if you want
   both callable), `01_pascal_triangle.py` intentionally stops at the Approach 2
   comment (your job to finish it), and `04_4Sum.py` imports `List` from `ast`
   (it works for annotations, but `typing.List` / plain `list[int]` is the
   standard choice)

---

## 🔗 LeetCode / GFG Problem Links (Copy into browser)

**LeetCode:**
- Pascal's Triangle (118): https://leetcode.com/problems/pascals-triangle/
- Pascal's Triangle II (119): https://leetcode.com/problems/pascals-triangle-ii/
- Majority Element II (229): https://leetcode.com/problems/majority-element-ii/
- 3Sum (15): https://leetcode.com/problems/3sum/
- 3Sum Closest (16): https://leetcode.com/problems/3sum-closest/
- 4Sum (18): https://leetcode.com/problems/4sum/
- 4Sum II (454): https://leetcode.com/problems/4sum-ii/
- Two Sum (1): https://leetcode.com/problems/two-sum/
- Next Permutation (31): https://leetcode.com/problems/next-permutation/
- Maximum Subarray (53): https://leetcode.com/problems/maximum-subarray/
- Spiral Matrix (54): https://leetcode.com/problems/spiral-matrix/

**GeeksforGeeks:**
- Pascal Triangle (practice): https://www.geeksforgeeks.org/problems/pascal-triangle0652/1
- Majority Element – More Than n/3 (practice): https://www.geeksforgeeks.org/problems/majority-vote/1
- All Triplets with Zero Sum (practice): https://www.geeksforgeeks.org/problems/find-all-triplets-with-zero-sum/1
- 4 Sum – All Quadruples (practice): https://www.geeksforgeeks.org/problems/find-all-four-sum-numbers1732/1

---

## ✅ Final Checklist Before Moving to Binary Search

- [ ] Can generate Pascal's Triangle AND the k-th row from memory (O(k) space)
- [ ] Can explain WHY at most 2 elements can appear more than n/3 times
- [ ] Can code Boyer-Moore (2 candidates + verify pass) from memory
- [ ] Can derive the n/k generalization (k-1 candidate slots)
- [ ] Solved 3Sum (15) three times independently
- [ ] Can state every dedup rule of the kSum template without looking
- [ ] Solved 4Sum (18) without help, including min/max pruning
- [ ] Can write a generic `kSum(nums, k, target)` from memory
- [ ] Solved 3Sum Closest (16) and/or 4Sum II (454)
- [ ] Can name the complexities exactly: Pascal O(n²) cells · Boyer-Moore O(n)
      time / O(1) space · 3Sum O(n²) · 4Sum O(n³)
- [ ] Can explain WHY the hash-map majority is O(n) space but voting is O(1)
- [ ] Solved at least 15 hard-level array problems total

> When you finish this roadmap, the hardest array step is DONE — row-building
> (Pascal), voting (Boyer-Moore), and sort + two pointers (kSum) are three
> interview patterns you'll reuse in Trees, Graphs, and DP. Next stop:
> **Binary Search** — where two pointers meet a decision predicate.
> Good luck — you've got this! 🚀




