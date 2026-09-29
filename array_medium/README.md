# 📚 Array (Medium) Learning Path — Basic to Advanced

Welcome! This is your complete guide to mastering **Arrays** (the medium level)
from scratch to interview-level problem solving. Follow this path in order.

> **Prerequisite:** finish `array_easy` first — traversal, two pointers,
> sliding window, and prefix sums are assumed knowledge here. Medium level is
> where every file starts teaching the **brute → better → optimal** ladder
> you'll climb in every real interview.

---

## 📁 What's Inside This Folder

| File | Topic | Key Idea |
|---|---|---|
| `01_two_sum.py` | Two Sum (LC 1) | Brute O(n²) → hashmap O(n) → two pointers |
| `02_sort_array_0_and_1.py` | Sort 0s/1s/2s (LC 75) | Count → two pointers → Dutch National Flag |
| `03_majority_element_1.py` | Majority Element (LC 169) | Brute → hashmap → Moore's voting O(1) space |
| `04_maximam_subarray_sum.py` | Maximum subarray sum (LC 53) | O(n³) → O(n²) → Kadane O(n) |
| `05_maximum_subarray_sum.py` | Max subarray WITH indices | Kadane + track `start` / `ansStart` / `ansEnd` |
| `06_best_time_buy_and_sell_stock.py` | Buy & Sell Stock (LC 121) | One pass: best min price vs best profit |
| `07_rearrange_array_by_sign.py` | Rearrange by sign (LC 2149) | pos/neg buckets → even/odd indices + unequal variety |
| `08_next_permutation.py` | Next Permutation (LC 31) | Find dip → swap → reverse suffix |
| `09_longest_consecutive_sequence.py` | Longest Consecutive (LC 128) | O(n²) search → sort O(n log n) → set O(n) |
| `10_set_martix_zeros.py` | Set Matrix Zeroes (LC 73) | Store positions → row/col arrays → first row/col O(1) |
| `11_rotate_matrix_by_90deg.py` | Rotate Image (LC 48) | Transpose + reverse rows ↔ layer-by-layer swap |
| `12_spiral_matrix.py` | Spiral Matrix (LC 54) | 4 boundaries shrink after each leg |
| `13_count_sub_array_sum.py` | Count subarrays sum = k (LC 560) | Brute → prefix sum + hashmap seeded `{0: 1}` |

Run any file with: `python 01_two_sum.py`

> Heads-up: `08`, `11`, `12`, `13` print nothing — they only define
> functions — add your own `if __name__ == "__main__":` demo (copy the style
> from `04`) so you can SEE them work.

---

## 🗺️ The Roadmap

### Phase 1: Two Sum — The Hashing Gateway (Day 1–2)
1. Run `01_two_sum.py` — three rungs: brute `O(n²)` → hashmap `O(n)` time /
   `O(n)` space → two pointers
2. Understand the hashmap trick: at index `i` ask — have I already seen
   `target - nums[i]`? The map remembers EVERYTHING to the left in O(1)
3. ⚠️ Critical caveat: `two_sum_two_pointers` only works on a **sorted**
   array (the demo `[2, 7, 11, 15]` happens to be sorted!). LC 1 asks for
   ORIGINAL indices, so the hashmap version is the real interview answer

**Milestone:** Solve without looking:
> LeetCode 1 in under 15 minutes. Then answer: why can't I sort and use two
> pointers here? (Because the returned indices would belong to the sorted
> array, not the original one.)

---

### Phase 2: Rearrangement — Dutch National Flag & Sign Alternation (Day 3–6)
1. Run `02_sort_array_0_and_1.py` — three rungs: count zeros then refill →
   two pointers (0s vs 1s) → **Dutch National Flag** (`low`/`mid`/`high`)
   handling 0s, 1s AND 2s in one pass
2. Understand the three-way invariant: `[0..low-1] = 0`,
   `[low..mid-1] = 1`, `[high+1..n-1] = 2`, `[mid..high] = unknown` —
   only `mid` moves into unknown territory
3. Run `07_rearrange_array_by_sign.py` — positives land on EVEN indices
   (`pos_index += 2`), negatives on ODD (`neg_index += 2`), both in one pass
4. Study the second variety: pairs fill first, leftovers go at the end —
   but its leftover loop writes EVERY leftover to `arr[n-1]`, so with 2+
   leftovers they overwrite each other. Reproduce it, then fix it (fill
   forward from `2 * min(len(pos), len(neg))` with a moving index)

**Milestone:** Code from memory:
> Sort `[2, 0, 2, 1, 1, 0]` → LC 75, one pass, O(1) space.
> Rearrange `[1, 2, 3, 4, -1, -2]` → `[1, -1, 2, -2, 3, 4]` (and make the
> file's second variety actually produce that!)

---

### Phase 3: Majority Element — Moore's Voting Starts Here (Day 7–8)
1. Run `03_majority_element_1.py` — three rungs: brute `O(n²)` → hashmap
   `O(n)` time / `O(n)` space → **Moore's voting** `O(n)` / `O(1)`
2. Understand the vote: `count == 0` → current number becomes candidate;
   match → `count += 1`; mismatch → `count -= 1` (one canceling pair dies)
3. Understand the verify step (`arr.count(candidate) > len(arr) / 2`) —
   voting only finds a POTENTIAL majority; the re-count confirms it
4. ⚠️ The file's loop starts at `range(1, len(arr))`, which SKIPS index 0 —
   try `majority_element_1_moore_voting([1, 2, 1])` and watch it wrongly
   return `-1` (brute correctly says `1`). Fix it to `range(len(arr))`,
   re-test, and you'll never forget why the full scan matters
5. This exact algorithm grows up into `array_hard`'s Majority Element II
   (two candidates, `> n/3`) — learn it once, reuse it there

**Milestone:** Explain out loud:
> Why does a candidate with count > 0 survive every cancelation?
> Trace `[2, 2, 1, 1, 2, 2]` step by step.
> Why MUST the verify pass exist? (Boyer-Moore guarantees at most ONE
> candidate — not that the candidate is real.)

---

### Phase 4: Subarrays ⭐ — Kadane & Prefix-Sum Counting (Day 9–13)
1. Run `04_maximam_subarray_sum.py` (yes, the filename has a typo!) — climb
   `O(n³)` brute → `O(n²)` better (running `current_sum`) → **Kadane `O(n)`**
2. Understand Kadane's rule: add `arr[i]` → update `max_sum` → reset
   `current_sum` to 0 if it went negative. Because `max_sum` starts at
   `-inf`, all-negative arrays stay correct
3. Run `05_maximum_subarray_sum.py` — the SAME Kadane that remembers INDICES:
   when the sum resets, `start = i`; when a new max lands, save
   `ansStart`/`ansEnd` → demo prints subarray `[4 -1 2 1]` with sum 6
4. Run `13_count_sub_array_sum.py` — the comment says brute is O(n³), but
   the running `current_sum` actually makes it **O(n²)**; the optimal version
   is prefix sum + hashmap in O(n)
5. Understand the `{0: 1}` seed: the empty prefix has sum 0 exactly once —
   without it you'd miss every subarray that starts at index 0
6. See the family: this is the COUNTING cousin of `array_easy`'s longest
   subarray with sum 0 — same running-sum, different question

**Milestone:** Solve without hints:
> LC 53 (max sum) and LC 560 (count subarrays = k). Then answer: why does
> Kadane update the max BEFORE the reset? What does `[-3, -1, -2]` return?

---

### Phase 5: Greedy One-Pass & The Permutation Trick (Day 14–16)
1. Run `06_best_time_buy_and_sell_stock.py` — `min_price` = best buy seen so
   far, `max_profit` = best sale seen so far; ONE loop does everything
2. Understand the order: min updates FIRST, then profit is tested with
   today's price — you can't sell before you buy
3. Run `08_next_permutation.py` — the universal 3-step recipe:
   - scan right→left for the first dip `arr[i] < arr[i+1]` (no dip = fully
     descending → the answer is the smallest arrangement: reverse everything)
   - swap `arr[i]` with the smallest value on its right that is still bigger
   - reverse the suffix `arr[i+1:]` — it was descending, reversing makes it
     the smallest possible continuation
4. The file prints nothing — add your own demo and test `[1, 3, 2]`,
   `[3, 2, 1]`, `[1, 2, 3]` (the three representative cases)

**Milestone:** Code both from memory:
> LC 121 (profit 5 for `[7, 1, 5, 3, 6, 4]`) and LC 31 — then draw on paper
> how `[1, 3, 2]` becomes `[2, 1, 3]` using the 3 steps.

---

### Phase 6: Sets — Longest Consecutive Sequence (Day 17–18)
1. Run `09_longest_consecutive_sequence.py` — three rungs: linear-search
   brute `O(n²)` → sort `O(n log n)` → **set `O(n)`**
2. Understand the set trick: only start counting when `num - 1 NOT in set` —
   the smallest element of each streak opens it, so every element is visited
   at most once inside a streak → true O(n)
3. Note how the sorting version survives duplicates:
   `if arr[i] == arr[i-1]: continue`

**Milestone:** Solve LC 128 in under 15 minutes, then answer:
> Why iterate the SET, not the list? Why does the sort version give up
> O(n log n)? When would the brute version accidentally be O(n²) AND slow?

---

### Phase 7: The Matrix Trilogy — Zeros, Rotate, Spiral ⭐ (Day 19–24)
1. Run `10_set_martix_zeros.py` — three rungs: store zero positions →
   `row[]`/`col[]` marker arrays → **first row/col AS the O(1) markers**
   guarded by the `col0` flag
2. Understand `col0`: `matrix[0][0]` can't tell 'row 0 has a zero' from
   'col 0 has a zero', so column 0's own fate lives in a separate variable —
   clear the inner block first, THEN row 0, THEN column 0 (order matters!)
3. Run `11_rotate_matrix_by_90deg.py` — two ways: **transpose + reverse
   each row** (simple, hard to mess up) ↔ **layer-by-layer 4-way rotation**
   (pointer-heavy, great practice); both O(n²) time / O(1) space
4. Run `12_spiral_matrix.py` — shrink 4 boundaries: top → right → bottom →
   left. The `if top <= bottom` and `if left <= right` guards stop you from
   re-walking an already-consumed row/column (deadly on 1×N and N×1 inputs!)
5. Files 11, 12 print nothing — write your own driver and TEST a 1×1 matrix,
   a 1×3 matrix, and a 3×1 matrix; guard bugs love edge cases

**Milestone:** Solve from memory, no hints:
> LC 73, LC 48, LC 54 — then answer: what does each of the 4 spiral
> boundary variables guarantee (invariant) after every full loop turn?

---

## 🧠 Mental Model Cheat Sheet

| Scenario | Technique | Why |
|---|---|---|
| "Find 2 numbers that sum to target" | Hash the complement → index | O(1) lookup remembers everything to the left |
| "Sort 0s / 1s / 2s in one pass" | Dutch National Flag: `low`/`mid`/`high` | Three regions grow into place, O(1) space |
| "Element appearing > n/2 times" | Moore's voting + verify pass | O(n) time, O(1) space — cancel-and-replace |
| "Max subarray SUM" | Kadane: add → record → reset on negative | A negative running prefix can never help |
| "The max subarray itself (indices)" | Track `start` on reset, save on improve | Same pass, remember the boundaries |
| "Count subarrays summing to k" | Prefix sum + hashmap of counts | `prefix - k` seen ⇒ that many subarrays end HERE |
| "Buy once, sell once, max profit" | Min price so far vs today's price | Every day tests one candidate sale |
| "Next lexicographic arrangement" | Find dip → swap with next-bigger → reverse suffix | The universal 3-step recipe (LC 31) |
| "Longest run of consecutive numbers" | Set + only start at streak heads (`num-1 ∉ set`) | Each element joins ≤ 1 streak → true O(n) |
| "Zero whole rows and columns" | Use row 0 / col 0 as markers (+ `col0`) | The matrix IS your O(1) marker space |
| "Rotate matrix 90° in place" | Transpose, then reverse each row | Clockwise 90° = flip over diagonal + mirror |
| "Walk a matrix in spiral order" | 4 boundaries, shrink after each leg | `if top <= bottom` / `if left <= right` guards |

---

## 🔑 Pattern Recognition (The Secret to Problem Solving)

### Pattern 1: Hash Map = Remember What You Saw
**How to spot it:** "pair with target", "count occurrences", "have I seen
this before", "complement"

```python
def two_sum_hashmap(nums, target):
    seen = {}                          # value → index of everything to the left
    for i, x in enumerate(nums):
        if target - x in seen:         # O(1): did we already pass the partner?
            return [seen[target - x], i]
        seen[x] = i                    # remember this one for later partners
    return []
```
> Used in: `01_two_sum.py` (partner lookup), `03` (count occurrences),
> `13_count_sub_array_sum.py` (count PAST prefix sums), and every
> "grouping / anagram / duplicate" problem you'll meet next.

### Pattern 2: Moore's Voting (cancel-and-replace, then verify)
**How to spot it:** "majority element", "appears more than n/2 times",
WITH an O(1) space constraint

```python
def moore_majority(nums):
    candidate, count = None, 0
    for x in nums:                     # NOTE: full scan — index 0 included!
        if count == 0:
            candidate, count = x, 1    # empty seat → sit down
        elif x == candidate:
            count += 1                 # supporter arrives
        else:
            count -= 1                 # supporter cancels one opponent
    # verify pass — voting only finds a POTENTIAL majority
    if nums.count(candidate) > len(nums) // 2:
        return candidate
    return -1
```
> Used in: `03_majority_element_1.py` — then it grows into `array_hard`'s
> two-candidate version for `> n/3`. The verify pass is NOT optional.

---

### Pattern 3: Kadane + the Prefix-Count Family (running sum questions)
**How to spot it:** `max subarray sum`, `longest subarray`, `count subarrays
summing to k` — anything about a CONTIGUOUS range

```python
def kadane(nums):
    best = float('-inf')        # safe for all-negative input
    run = 0
    for x in nums:
        run += x                # 1) extend the current subarray
        best = max(best, run)   # 2) record BEFORE resetting!
        if run < 0:
            run = 0             # 3) a negative prefix is dead weight
    return best
```
> MAXIMIZE → Kadane (`04`, `05`). COUNT instead → keep a hashmap of prefix
> sums and add `prefix_sum_count[prefix_sum - k]` (`13`, seeded `{0: 1}`).
> MAXIMIZE LENGTH with non-negatives → sliding window (`array_easy`).
> Same running-sum brain, three different questions.

### Pattern 4: The Matrix Toolkit (mark, transpose, shrink)
**How to spot it:** matrix problems that say `in place`, `rotate`, `zero`,
`spiral`, `set` — matrices never need fancy algorithms, just disciplined
boundaries:

```python
# ROTATE 90° clockwise — the simple way (11_rotate_matrix_by_90deg.py)
for i in range(n):                          # transpose: swap across diagonal
    for j in range(i, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
for row in matrix:                          # mirror: reverse every row
    row.reverse()
```
```python
# ZERO rows + columns in O(1) space — mark then clear (10_set_martix_zeros.py)
#   matrix[i][0] = 0  →  row i must die        matrix[0][j] = 0  →  col j must die
#   col0 flag         →  does column 0 itself die?  (matrix[0][0] can't say)
#   ORDER: clear inner (1..n, 1..m) first, then row 0, then column 0
```
```python
# SPIRAL — shrink 4 boundaries, guard every leg (12_spiral_matrix.py)
while top <= bottom and left <= right:
    ... top row ...      top    += 1        # consumed
    ... right column ... right  -= 1        # consumed
    if top <= bottom: ... bottom row ...   bottom -= 1   # guard: may be gone
    if left <= right:  ... left column ... left  += 1    # guard: may be gone
```

---

## 📝 30-Day Practice Schedule

| Day | Topic | Problem Set |
|---|---|---|
| 1 | Two Sum, 3 rungs | Run `01_two_sum.py`, solve LC 1 with the hashmap |
| 2 | Two pointers caveat | Re-code all 3 from memory; explain why sorting breaks LC 1 |
| 3 | Sort 0s and 1s | Run `02` count + two-pointer versions |
| 4 | Dutch National Flag ⭐ | Trace `low`/`mid`/`high` on paper, solve LC 75 |
| 5 | Rearrange by sign | Run `07` first two approaches, LC 2149 |
| 6 | Unequal-counts variety | Reproduce the leftover bug, fix it, re-test |
| 7 | Review week 1 | Rewrite `01` + `02` + `07` from memory |
| 8 | Majority Element | Run `03` brute + hashmap, LC 169 |
| 9 | Moore's voting ⭐ | Reproduce the `[1, 2, 1]` bug, fix the `range`, re-test |
| 10 | Kadane ⭐ | Run `04` (all 3 rungs), solve LC 53 |
| 11 | Subarray + indices | Run `05`, re-derive index tracking, GFG Kadane's Algorithm |
| 12 | Count subarrays = k | Run `13`, solve LC 560 |
| 13 | Prefix-sum deep dive | Explain the `{0: 1}` seed out loud, re-solve LC 560 blind |
| 14 | Review week 2 | Re-solve LC 53 + LC 560 without hints |
| 15 | Buy & sell stock | Run `06`, LC 121, GFG max one transaction |
| 16 | Next permutation | Run `08` + add your own demo, LC 31 |
| 17 | Next permutation blind | GFG Next Permutation, draw `[1, 3, 2]` → `[2, 1, 3]` on paper |
| 18 | Longest consecutive | Run `09` (all 3 rungs), LC 128 |
| 19 | Streak-head trick | GFG Longest Consecutive Subsequence |
| 20 | Set matrix zeros | Run `10` (all 3 rungs), LC 73 |
| 21 | O(1) space zeros | Re-derive the `col0` trick from memory, LC 73 again |
| 22 | Rotate 90° | Run `11` both ways, LC 48 |
| 23 | Spiral traversal | Run `12` + add demo + test 1×1 / 1×3 / 3×1, LC 54 |
| 24 | Review week 3 | Re-run all 3 matrix files blind, LC 73 timed (25 min) |
| 25 | Matrix GFG drill | GFG Spirally Traversing a Matrix + Rotate by 90 degree |
| 26 | Backfill | LC 189 Rotate Array (rotate thinking, one-dimension) |
| 27 | Backfill timed | LC 75 in 15 min + LC 1 in 10 min |
| 28 | Timed pair | Set Matrix Zeroes 25 min + Next Permutation 15 min |
| 29 | Mock interview | 45-min session, 2 problems |
| 30 | MOCK INTERVIEW DAY | 3 problems — full simulation |

---

## 💡 Advice From a Mentor

1. **Don't just read** — write every solution by hand, from an empty file
2. **Climb every ladder** — each file presents brute → better → optimal; if
   you can't say WHY the brute is slow, the optimal won't stick in your head
3. **Sortedness is the license for two pointers** — `01`'s two-pointer version
   silently assumes a sorted array; always ask 'is this sorted?' before
   reaching for left/right
4. **Moore's = cancel pairs, then VERIFY** — voting finds at most ONE
   candidate, never proof; the re-count is part of the algorithm
5. **Kadane order matters** — record the max BEFORE resetting, and start
   `max_sum` at `-inf` so all-negative arrays don't lie to you
6. **Draw the matrix** — label `top/bottom/left/right` (or `i/j`) on paper;
   every matrix bug is an off-by-one guard or a wrong clear order
7. **Spaced repetition** — redo problems at Day 7, 14, 21, 30 (the schedule
   bakes this in)
8. **Patterns > Memorization** — Two Sum / counting / prefix lookups are ONE
   pattern; Kadane / prefix counting / sliding window are ONE family;
   zeros / rotate / spiral are ONE toolkit
9. **Know your file quirks** — and turn them into exercises:
   - typos in names: `04_maximam_subarray_sum.py` and its `maximaum_*`
     functions, `08_next_permutation.py`'s `next_permnuatation`,
     `10_set_martix_zeros.py` — Python doesn't care, but fix them before you
     copy-paste between files
   - `07_rearrange_array_by_sign.py` has a stray `from turtle import pos`
     import — unused, just delete it
   - `03_majority_element_1.py` Moore's loop starts at `range(1, len(arr))`,
     so `majority_element_1_moore_voting([1, 2, 1])` wrongly returns `-1`
     — fix it to `range(len(arr))` (Day 9)
   - `07`'s second variety writes every leftover to `arr[n-1]`, so
     `[1, 2, 3, 4, -1, -2]` comes back as `[1, -1, 2, -2, -1, 4]` instead of
     `[1, -1, 2, -2, 3, 4]` — fix the leftover fill (Day 6)
   - `13`'s brute-force comment claims O(n³), but the running `current_sum`
     already makes it O(n²) — never trust a comment you didn't verify
   - `08`, `11`, `12`, `13` have no `print` demo — write your own driver

---

## 🔗 LeetCode / GFG Problem Links (Copy into browser)

**LeetCode:**
- Two Sum (1): https://leetcode.com/problems/two-sum/
- Sort Colors (75): https://leetcode.com/problems/sort-colors/
- Majority Element (169): https://leetcode.com/problems/majority-element/
- Maximum Subarray (53): https://leetcode.com/problems/maximum-subarray/
- Best Time to Buy and Sell Stock (121): https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
- Rearrange Array Elements by Sign (2149): https://leetcode.com/problems/rearrange-array-elements-by-sign/
- Next Permutation (31): https://leetcode.com/problems/next-permutation/
- Longest Consecutive Sequence (128): https://leetcode.com/problems/longest-consecutive-sequence/
- Set Matrix Zeroes (73): https://leetcode.com/problems/set-matrix-zeroes/
- Rotate Image (48): https://leetcode.com/problems/rotate-image/
- Spiral Matrix (54): https://leetcode.com/problems/spiral-matrix/
- Subarray Sum Equals K (560): https://leetcode.com/problems/subarray-sum-equals-k/

**GeeksforGeeks:**
- Sort 0s, 1s and 2s (practice): https://www.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1
- Majority Element (practice): https://www.geeksforgeeks.org/problems/majority-element-1587115620/1
- Kadane's Algorithm (practice): https://www.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1
- Stock Buy and Sell — Max one Transaction Allowed: https://www.geeksforgeeks.org/problems/buy-stock-2/1
- Next Permutation (practice): https://www.geeksforgeeks.org/problems/next-permutation5226/1
- Longest Consecutive Subsequence: https://www.geeksforgeeks.org/problems/longest-consecutive-subsequence2449/1
- Set Matrix Zeros (practice): https://www.geeksforgeeks.org/problems/set-matrix-zeroes/1
- Rotate by 90 degree: https://www.geeksforgeeks.org/problems/rotate-by-90-degree-1587115621/1
- Spirally Traversing a Matrix: https://www.geeksforgeeks.org/problems/spirally-traversing-a-matrix-1587115621/1

---

## ✅ Final Checklist Before Moving to Array (Hard)

- [ ] Can code Two Sum in all 3 ways and say when two pointers is legal (sorted only!)
- [ ] Can sort 0s/1s/2s in one pass (Dutch National Flag) from memory
- [ ] Can state the three-region invariant of `low`/`mid`/`high` without looking
- [ ] Can code Moore's voting + verify pass, and explain WHY it's O(1) space
- [ ] Fixed and re-tested the two bugs in `03` and `07`
- [ ] Can derive Kadane in under 60 seconds, including all-negative input
- [ ] Can print the max subarray's indices, not just its sum
- [ ] Can count subarrays summing to k with a prefix map, including why `{0: 1}` is seeded
- [ ] Solved Buy/Sell Stock (121) without help
- [ ] Can perform Next Permutation's 3-step recipe on paper from memory
- [ ] Solved Longest Consecutive (128) with the O(n) set approach
- [ ] Can derive Set Matrix Zeroes in O(1) space (first row/col + `col0`)
- [ ] Can rotate a matrix 90° two different ways
- [ ] Can write spiral traversal that survives 1×1, 1×N, and N×1 inputs
- [ ] Solved at least 30 array problems total (all three folders combined)

> When you finish this roadmap, you own all three levels of the array journey:
> `array_easy` gave you traversal, `array_medium` gave you patterns — hashing,
> voting, Kadane, and the matrix toolkit — and `array_hard` will push them to
> their limits (n/3 voting, kSum, pruning). Next stop: **Array (Hard)**.
> Good luck — you've got this! 🚀







