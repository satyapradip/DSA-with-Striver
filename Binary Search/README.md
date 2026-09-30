# 📚 Binary Search Learning Path — Basic to Advanced

Welcome! This is your complete guide to mastering **Binary Search** — the two
core templates, boundary variants, rotated arrays, and the mighty
*binary-search-on-answer* pattern. Follow this path in order.

> **Prerequisite:** finish `array_easy` first (two-pointer comfort assumed),
> and ideally `array_medium`. In Striver's A2Z order, Binary Search follows
> **Arrays and Hashing** — if you haven't done `basic_hashing` yet, it's a
> two-day detour worth taking. Hard level here means: **two templates you
> must never confuse**, plus the on-answer skeleton interviews love.

---

## 📁 What's Inside This Folder

| File | Topic | Key Idea |
|---|---|---|
| `01_index_of_target.py` | Binary Search (LC 704) | The canonical `left <= right` template |
| `02_insert_position.py` | Search Insert Position (LC 35) | When the loop ends, `left` IS the answer |
| `03_first_and_last_occurance.py` | First & Last Occurrence (LC 34) | Two passes: keep going left / keep going right |
| `04_upper_bound_and_lower_bound.py` | Lower & upper bound | Half-open `[0, n)` with `right = mid` |
| `05_Search in rotated sorted array-I.py` | Rotated Search I (LC 33) | Exactly one half is sorted — test membership there |
| `06_search_in_rotated_sorted_array2.py` | Rotated Search II (LC 81) | Duplicates: shrink both ends when ambiguous |
| `07_find_minimum_in_sorted_array.py` | Find Min in Rotated (LC 153) | Compare `mid` vs `right` to chase the drop |
| `08_single_element_in_sorted_array.py` | Single Element (LC 540) | Pair-index alignment (even index → pair intact) |
| `09_find_peak_element.py` | Find Peak (LC 162) | Walk up the slope — any peak will do |
| `10_koko_eating_banas.py` | Koko Eating Bananas (LC 875) | Search the speed; O(n) check per mid |
| `11_Minimum days to make M bouquets.py` | Min Days for Bouquets (LC 1482) | Search days + adjacency feasibility scan |
| `12_Find the smallest divisor.py` | Smallest Divisor (LC 1283) | Three solutions, one idea: search the divisor |

Run any file from inside this folder: `cd "Binary Search"` then
`python 01_index_of_target.py` — names with spaces need quotes:
`python "05_Search in rotated sorted array-I.py"`

> **Heads-up on file quirks:**
> - `01`, `03`, `05`, `07`, `11` define functions only — **no demo output**.
>   Add your own `if __name__ == "__main__":` block (copy `02`'s style).
>   Meanwhile `04`, `08`, `09`, `10` print at the top level — they run the
>   moment you execute the file.
> - `03` does `from ast import List` — it survives only because `ast.List`
>   happens to exist; the standard is `typing.List` or plain `list[int]`
>   (same quirk as `array_hard/04_4Sum.py`).
> - `05` hides a real **bug**: the right-half test reads
>   `target <= arr[high - 1]` instead of `arr[high]`. Reproduce it with
>   `search_in_rotated_sorted_array([5, 1, 3], 3)` → returns `-1`, but `3`
>   sits at index `2`. One-character fix — see Phase 3.
> - `07`'s header comment warns about duplicates, but the code (LC 153)
>   assumes **distinct** values — it fails on `[3, 3, 1, 3]` (returns `3`,
>   the min is `1`). The duplicate variant is LC 154.
> - `12` defines `smallest_divisor` **twice** — Python keeps the last one
>   (the `math.ceil` version). `Solution.smallestDivisor` is the
>   LeetCode-ready class version.

---
## 🗺️ The Roadmap

### Phase 1: The Core Template — Shrink a Closed Interval (Day 1–3)
1. Run `01_index_of_target.py` — the six lines you must never forget:
   `while left <= right` · `mid = (left + right) // 2` · hit → return ·
   else `left = mid + 1` / `right = mid - 1`
2. Run `02_insert_position.py` — same template, different exit: when the
   loop dies, `left` is exactly where the target *would* sit → that's the
   answer (demo prints `2, 1, 4, 0`)
3. Internalise the invariant: the search space is always `[left, right]`
   inclusive; each iteration kills `mid` plus half the rest → **O(log n)**
4. Beat the interviewer to the overflow question:
   `mid = left + (right - left) // 2` — Python's ints never overflow, but
   C++/Java `(l + r) / 2` can; say it before they ask

**Milestone:** code LC 704 and LC 35 from memory in under 10 minutes, then
explain: why `while left <= right` (a 1-element window must still be
checked) vs the `left < right` variant in `04`?

---

### Phase 2: Boundaries — Lower/Upper Bound & First/Last ⭐ (Day 4–7)
1. Run `04_upper_bound_and_lower_bound.py` → `1` and `4` for target `2` in
   `[1, 2, 2, 2, 3]`
2. Learn the half-open template: `right = len(arr)`, `while left < right`,
   and `right = mid` on the "keep searching left" branch — no off-by-one at
   the end: `left` stops at the first slot where the condition flips. This
   is exactly C++ `std::lower_bound` / `std::upper_bound` and Python
   `bisect.bisect_left` / `bisect.bisect_right`
3. Run `03_first_and_last_occurance.py` — two closed-interval passes: on a
   hit, store `ans = mid` then go **further left** (`right = mid - 1`) for
   the first occurrence, **further right** (`left = mid + 1`) for the last
4. Cross-check the two worlds: `lower_bound` = first occurrence index, and
   `upper_bound − 1` = last occurrence — one idea, two spellings

**Milestone:** write LC 34 two ways — your two-pass version, then a
three-line `bisect` version (`[bisect_left(a, t), bisect_right(a, t) - 1]`
guarded by the "found" check). Then say what `lower_bound` returns when the
target is absent (the insertion point).

---

### Phase 3: Rotated Arrays — "Which Half Is Sorted?" ⭐ (Day 8–12)
1. Run `05` (after fixing the bug!) — each iteration exactly one half is
   *normally sorted*: `arr[low] <= arr[mid]` ⇒ left half sorted ⇒ if
   `target ∈ [arr[low], arr[mid])` go left, else go right; otherwise the
   right half is sorted and you test it instead
2. Reproduce the bug FIRST: `search_in_rotated_sorted_array([5, 1, 3], 3)`
   → `-1`, expected `2`. One-character fix: `arr[high - 1]` → `arr[high]`.
   This is why you trace edge cases where `target == arr[high]`
3. Run `06_search_in_rotated_sorted_array2.py` — duplicates destroy the
   "one half is sorted" certainty: when `arr[left] == arr[mid] ==
   arr[right]` you can't tell → shrink BOTH ends by one and retry. Worst
   case degrades to **O(n)** — exactly what LC 81's spec allows
4. Run `07_find_minimum_in_sorted_array.py` — no target needed:
   `nums[mid] > nums[right]` means the drop is to the right
   (`left = mid + 1`), else the min is at/before `mid` (`right = mid`).
   Note `while left < right` with `right = mid` — `left` converges ON the
   minimum

**Milestone:** from memory, trace `[4, 5, 6, 7, 0, 1, 2]`, target `0` →
index 4. Then explain why `07` returns `3` for `[3, 3, 1, 3]` — the `>`
comparison assumes distinct values (its header comment even hints at it),
and sketch what LC 154 needs instead (an extra branch for
`nums[mid] == nums[right]` → `right -= 1`).

---
### Phase 4: Index Predicates — Parity & Slopes (Day 13–15)
1. Run `08_single_element_in_sorted_array.py` → `2`. The trick: force `mid`
   to an even index (the start of a pair). If `nums[mid] == nums[mid+1]`
   the pair is intact → the single element is right (`left = mid + 2`);
   else the pairing broke at/left of `mid` (`right = mid`)
2. Run `09_find_peak_element.py` → `3`. No sortedness needed — follow the
   slope: `nums[mid] > nums[mid+1]` means you're descending, so a peak is
   at `mid` or leftward (`right = mid`); else climb (`left = mid + 1`).
   `while left < right` lands `left == right` on A peak — the array edges
   act like imaginary `-∞` guards, so you can never fall off

**Milestone:** answer without looking:
> Why must `08` align `mid` to even? (Pairs start at even offsets; the lone
> element breaks the parity.) For `09`, why is ANY peak acceptable? (The
> problem allows it — and the slope argument proves convergence.)

---

### Phase 5: Binary Search on the Answer ⭐⭐ (Day 16–21)
This is where interviews actually live: the answer isn't sitting in an
array — you *construct* the range and test feasibility.

1. Run `10_koko_eating_banas.py` → `4`. Answer space = eating speed
   `1..max(piles)`; `ok(mid)` = `sum(ceil(pile / mid)) <= h`; monotone — if
   speed `x` finishes, so does `x + 1` → binary-search the boundary
2. Run `11_Minimum days to make M bouquets.py` — answer space = days
   `1..max(bloomDay)`; `ok(mid)` = scan left-to-right counting **adjacent**
   runs of `k` bloomed flowers until you reach `m`. Don't skip the
   `m * k > n → -1` pre-check
3. Run `12_Find the smallest divisor.py` — answer space = divisor
   `1..max(nums)`; `ok(mid)` = `sum(ceil(num / mid)) <= threshold`. Note the
   two integer-ceil tricks: `(num - 1) // d + 1` (first solution, no floats)
   and `math.ceil(num / d)` (second solution — which wins the redefinition
   race); the `Solution` class is the LeetCode-ready third take
4. Recognise the shared skeleton: **pick the range → write `ok(x)` → prove
   monotone → standard shrink** — total cost `O(log(range) × cost(ok))`

**Milestone:** from memory: LC 875 in ≤ 20 min, LC 1482 in ≤ 30 min. Then
state `10`'s complexity in words: "`log(max(piles))` iterations × an O(n)
sum each."

---

### Phase 6: Review & Speed Run (Day 22–24)
1. Re-run all 12 files; keep the fix for `05` (re-apply it if you reverted)
2. Timed set: LC 704 (5 min) → LC 34 (15 min) → LC 33 (20 min) →
   LC 875 (20 min)
3. Recite cold: `left <= right` vs `left < right` — when each applies and
   why the shrink rules differ (`r = mid - 1` vs `r = mid`)

---
## 🧠 Mental Model Cheat Sheet

| Scenario | Template | Why |
|---|---|---|
| Exact target in a sorted array | `while l <= r` · hit → return · `l = mid+1` / `r = mid-1` | Closed interval: a 1-element window still gets checked |
| Insertion index / "first true" | `while l < r` · `r = mid` on left-moves · return `l` | Half-open interval converges on the boundary slot |
| First occurrence | on hit `ans = mid`, `r = mid - 1` | Keep pulling left past equal values |
| Last occurrence | on hit `ans = mid`, `l = mid + 1` | Mirror image |
| Rotated sorted array (distinct) | pick the sorted half via `arr[l] <= arr[mid]`, test membership | Exactly one half is "normally sorted" |
| Rotated + duplicates | `arr[l] == arr[m] == arr[r]` → shrink both ends | Ambiguous — the sorted half can't be identified |
| Find min in rotated array | `mid > right` → go right, else `r = mid` | The single "drop" decides where the min lives |
| Lone element among pairs | align `mid` to an even index, inspect `nums[mid+1]` | Pairing parity survives the one removal |
| Peak / "any valid index" | follow the slope: `a[mid] > a[mid+1]` → `r = mid` else `l = mid+1` | Climbing guarantees a local max |
| Min/max X such that `f(X)` is ok | binary-search the answer + O(n) `ok(mid)` | `f` is monotone: `ok(x) ⇒ ok(x+1)` |

---

## 🔑 Pattern Recognition (The Secret to Problem Solving)

### Pattern 1: Closed-Interval Exact Search
**How to spot it:** "find THE index of a value in a sorted (or rotated)
array" — files `01`, `02`, `03`, `05`, `06`.

- invariant to recite: *"the answer, if it exists, is inside `[left, right]`"*
- every branch must shrink that interval: `mid + 1`, `mid - 1` — never
  `mid` on both sides
- on a hit in first/last problems, DON'T return — store `ans` and keep
  narrowing (`r = mid - 1` or `l = mid + 1`)

### Pattern 2: Half-Open Boundary Seek (Lower/Upper Bound)
**How to spot it:** "first position where…", "insert at…", "count elements
less than…" — file `04`, plus every `bisect` rewrite.

- interval `[left, right)` of length `right - left`; write
  `mid = (left + right) // 2` and `right = mid` (never `mid - 1`) on the
  keep-left branch — `mid` itself is still a candidate
- when the loop ends, `left == right` = the flip point — even if the target
  is absent (that's your insertion index)
- it IS `bisect_left` / `bisect_right` — verify your answers against them

### Pattern 3: Rotated? Find the Sorted Half
**How to spot it:** a normally sorted array "that something happened to" —
files `05`, `06`, `07`.

- exactly one of `[low..mid]` / `[mid..high]` is contiguous in value space
  (with distinct values); test `target` membership in the sorted one
- duplicates (`06`) make both halves ambiguous → shrink both ends, accept
  O(n) worst case
- `07` is the degenerate case: no target, just ask "is the min to my right?"

### Pattern 4: Binary Search on the Answer ⭐⭐
**How to spot it:** "minimum speed / days / capacity / force such that…"
with a limit — files `10`, `11`, `12`.

- the array doesn't hold the answer — you invent a candidate `x` and write
  a feasibility check `ok(x)`
- prove monotonicity FIRST: "if `x` works, does `x + 1` also work?" — if
  yes, binary-search the boundary between working and failing
- cost is `O(log(answer range) × cost(ok))` — the range is usually
  **values**, not indices (`1..max(piles)`), which is why Koko is
  `O(n log max)`, not `O(log n)`

---
## 📝 30-Day Practice Schedule

| Day | Topic | Problem Set |
|---|---|---|
| 1 | Core template | Run `01` (add your own demo) · solve LC 704 |
| 2 | Insert position | Run `02` → 2, 1, 4, 0 · solve LC 35 |
| 3 | Template from memory | Write both in ≤ 10 min; explain `left <= right` |
| 4 | Lower/upper bound | Run `04` → 1, 4 · cross-check with `bisect` |
| 5 | First/last occurrence | Read `03`, add a `__main__` demo · solve LC 34 |
| 6 | bisect cross-check | Re-solve LC 34 in 3 lines with `bisect_left/right` |
| 7 | Review week 1 | Rewrite `01`–`04` blind; closed vs half-open aloud |
| 8 | Rotated search I ⭐ | Reproduce `05`'s bug on `[5, 1, 3]`, fix it, solve LC 33 |
| 9 | Rotated search II | Run `06` → True/False · why worst case is O(n) · LC 81 |
| 10 | Find min rotated | Trace `07` on `[4,5,6,7,0,1,2]` · solve LC 153 |
| 11 | Duplicates break things | Why `07` fails on `[3,3,1,3]` · try LC 154 |
| 12 | Review week 2 | Re-run `05`–`07`; teach "which half is sorted" aloud |
| 13 | Pair parity | Run `08` → 2 · explain even-index alignment · LC 540 |
| 14 | Slope climbing | Run `09` → 3 · solve LC 162 |
| 15 | Index predicates | Solve LC 162 a second way; state both complexities |
| 16 | On-answer intro ⭐⭐ | Read `10`; write `ok(speed)` on paper BEFORE coding |
| 17 | Koko | Run `10` → 4 · LC 875 timed (≤ 20 min) |
| 18 | Bouquets | Run `11` (add a demo) · LC 1482 (≤ 30 min) |
| 19 | Smallest divisor | Compare `12`'s three solutions · solve LC 1283 |
| 20 | Review week 3 | Say `log(range) × check` for `10`, `11`, `12` out loud |
| 21 | On-answer ×2 | LC 1011 (ship packages) + LC 1552 (magnetic force) |
| 22 | Harder backfill | LC 410 (Split Array Largest Sum) or LC 4 (median) |
| 23 | Timed set | LC 704 (5) → LC 34 (15) → LC 33 (20) minutes |
| 24 | Edge-case day | n = 1 · all equal · target at both ends · target absent |
| 25 | GFG practice | GFG: First and Last Occurrences of x |
| 26 | GFG practice | GFG: Binary Search practice problem |
| 27 | Speed drill | LC 35 + LC 875 in 25 minutes combined |
| 28 | Mock interview | 45-minute session: 1 classic + 1 on-answer |
| 29 | Review | Skim this README; tick every checklist box you can |
| 30 | MOCK INTERVIEW DAY | 3 problems — full simulation, camera on |

---
## 💡 Advice From a Mentor

1. **Draw the invariant** — every iteration, "the answer lives in
   `[left, right]`" must stay true. Write that sentence for `01`, `04`,
   and `10` — if a branch breaks it, you have a bug
2. **Two templates, know both cold** — `left <= right` closed (search a
   value) and `left < right` half-open (find a boundary). Never mix their
   shrink rules: `r = mid - 1` belongs to the first, `r = mid` to the
   second
3. **`mid` alone tells you nothing** — always ask ONE question: "is the
   answer left or right of mid?" One comparison per branch, no more
4. **On-answer search needs monotonicity** — prove `ok(x) ⇒ ok(x+1)` BEFORE
   writing the loop; articulating that proof is usually the whole interview
5. **Complexity is `log(range) × cost(check)`** — the range is often the
   *values* (Koko: `1..max(piles)`), not the indices. That's why those
   files are `O(n log M)`, not `O(log n)`
6. **`bisect` is your cross-check** — after coding lower/upper bound by
   hand, run `bisect_left`/`bisect_right` on the same inputs. When they
   disagree, one of you is wrong (and it's usually you 😉)
7. **Fix the bugs you meet** — `05`'s `arr[high - 1]`, `07`'s duplicate
   blind spot, `12`'s double definition. Understanding a bug beats
   routing around it
8. **Drill the edge cases** — n = 1, all elements equal, target at index 0,
   target at the last index, target missing entirely. Binary search bugs
   live there, nowhere else

---
## 🔗 LeetCode / GFG Problem Links (Copy into browser)

**LeetCode:**
- Binary Search (704): https://leetcode.com/problems/binary-search/
- Search Insert Position (35): https://leetcode.com/problems/search-insert-position/
- Find First and Last Position of Element in Sorted Array (34): https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
- Search in Rotated Sorted Array (33): https://leetcode.com/problems/search-in-a-rotated-sorted-array/
- Search in Rotated Sorted Array II (81): https://leetcode.com/problems/search-in-a-rotated-sorted-array-ii/
- Find Minimum in Rotated Sorted Array (153): https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
- Find Minimum in Rotated Sorted Array II (154): https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
- Single Element in a Sorted Array (540): https://leetcode.com/problems/single-element-in-a-sorted-array/
- Find Peak Element (162): https://leetcode.com/problems/find-peak-element/
- Koko Eating Bananas (875): https://leetcode.com/problems/koko-eating-bananas/
- Minimum Days to Make Bouquets (1482): https://leetcode.com/problems/minimum-days-to-make-bouquets/
- Find the Smallest Divisor Given a Threshold (1283): https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
- Capacity to Ship Packages Within D Days (1011): https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
- Magnetic Force Between Two Balls (1552): https://leetcode.com/problems/magnetic-force-between-two-balls/
- Split Array Largest Sum (410): https://leetcode.com/problems/split-array-largest-sum/
- Median of Two Sorted Arrays (4) — stretch: https://leetcode.com/problems/median-of-two-sorted-arrays/

**GeeksforGeeks:**
- Binary Search (practice): https://www.geeksforgeeks.org/problems/search-an-element-in-an-array-1587115620/1
- First and Last Occurrences of x (practice): https://www.geeksforgeeks.org/problems/first-and-last-occurrences-of-x3116/1
- Count number of occurrences in a sorted array: https://www.geeksforgeeks.org/dsa/count-number-of-occurrences-or-frequency-in-a-sorted-array/
- Binary search — identify, solve, interview: https://www.geeksforgeeks.org/dsa/binary-search-identify-solve-and-interview-questions/

---

## ✅ Final Checklist Before Moving to Strings

- [ ] Can recite the closed-interval template from memory (including WHY `left <= right`)
- [ ] Can recite the half-open bound template and say what it returns when the target is absent
- [ ] Can implement LC 34 two ways: two hand-rolled passes AND a 3-line `bisect` version
- [ ] Can state lower/upper bound semantics: first `>= target` / first `> target`
- [ ] Solved LC 33, including reproducing and fixing `05`'s `arr[high - 1]` bug myself
- [ ] Can explain why duplicates force the O(n) worst case (LC 81's triple-equal shrink)
- [ ] Can derive find-min-in-rotated from the single comparison `nums[mid] vs nums[right]`
- [ ] Can state the even-index alignment trick for LC 540 without looking
- [ ] Can explain why find-peak returns *A* peak, not *the* peak (slope + `-∞` guards)
- [ ] Can write the on-answer skeleton from memory: range → `ok(x)` → monotone → shrink
- [ ] Solved LC 875, LC 1482, and LC 1283 without help — and can state each as `O(n log M)`
- [ ] Can name both templates and pick correctly without hesitating
- [ ] Solved at least 20 binary-search problems total (this folder + practice links)

> Binary search is the rare trick that works on **indices, values, and
> invented answers** — three templates (closed, half-open, on-answer) cover
> almost everything an interviewer can throw at you, and `bisect` is your
> permanent safety net. Next stop: **Strings** — where the same two-pointer
> instincts meet character arrays. Good luck — you've got this! 🚀