# 📚 Basic Hashing Learning Path — Basic to Advanced

Welcome! This is your complete guide to mastering **Hashing (the basics)** —
frequency arrays, the value-as-index trick, and the habit of *precompute
once, answer in O(1)*. Follow this path in order.

> **Where does this fit?** In Striver's A2Z sheet, **Hashing sits right after
> Arrays and before Binary Search**. Files `01`–`03` only need loops and
> arrays (a quick run through `array_easy` is enough), and `04` connects
> hashing to the sliding window you already met in `array_medium`. It's the
> smallest folder in this repo — treat it as a sharp two-day toolkit, not a
> mountain.

---

## 📁 What's Inside This Folder

| File | Topic | Key Idea |
|---|---|---|
| `01_character_hashing.py` | Character frequency | `ord(c) - ord('a')` maps a letter to a slot in a 26-cell array |
| `02_number_hashing.py` | Number frequency (interactive) | The value IS the index; guard the valid range |
| `03_hashing.py` | Hashing demo (hardcoded) | Build once → every query answers in O(1) |
| `04_maximum_frequency.py` | Maximum Frequency (LC 1838) | Sort + sliding window with `k` increments |

Run any file with: `python 01_character_hashing.py`

> **Heads-up on file quirks:**
> - `01` and `02` are **interactive** — they prompt for input. Handy inputs to
>   try: string `banana` with queries `a n r` (→ 3, 2, 0), and array
>   `1 3 2 1 3` with queries `1 4 2 3 12` (→ 2, 0, 1, 2, 0).
> - `01` understands **lowercase a–z only** — a space, digit, or capital
>   letter sends `ord(character) - ord('a')` out of range and the program
>   crashes with `IndexError`. That's the trade-off of a fixed 26-slot table
>   (fix: normalize first with `text.lower()` and a filter).
> - `04` has a **broken demo guard**: it reads `if __name__ == "main":` but
>   Python only compares against the literal `"__main__"`. The file
>   therefore **prints nothing** when you run it. Fix that one string and it
>   prints `3` (the answer for `maxFrequency(3, [1, 2, 3, 4])`).
> - `02` and `03` declare a `size` variable that is never used — the real
>   length comes from the input line / the hardcoded list. Harmless, but
>   don't copy that habit.

---
## 🗺️ The Roadmap

### Phase 1: Character Hashing — Turn a Letter Into an Index (Day 1–2)
1. Run `01_character_hashing.py` — sample run: string `banana`, 3 queries
   `a n r` → counts `3, 2, 0`
2. The whole hash function is one line: `ord(character) - ord('a')` — it
   re-bases ASCII so `a → 0`, `b → 1`, … `z → 25`
3. Two passes total: one **O(n) build** over the string, then each query is a
   bare array read — **O(1)**. No re-counting, ever
4. Break it on purpose: enter an uppercase letter → the slot is negative →
   `IndexError`. A frequency array only works when you fully control the key
   space

**Milestone:** answer without looking:
> Why is precomputing better than counting inside every query loop?
> (`O(n + Q)` total vs `O(n · Q)` — you trade a little memory for time.)
> What does subtracting `ord('a')` achieve? (It re-bases the codes so the
> alphabet starts at slot 0 — without it you'd need a 97-slot array.)

---

### Phase 2: Number Hashing — The Value Is the Index (Day 3–5)
1. Run `03_hashing.py` — the non-interactive version. Predict the output
   first, then run it: `[1, 3, 2, 1, 3]`, queries `[1, 4, 2, 3, 12]` →
   `2, 0, 1, 2, 0`
2. Run `02_number_hashing.py` interactively — same idea with safety rails:
   `hash_arr = [0] * 13` plus an `0 <= num < 13` check that warns on
   out-of-range values instead of silently corrupting counts
3. See the shape: `hash_arr[num] += 1` — **slot `v` stores the count of
   value `v`**. That IS the hash: `key → position`, no searching involved
4. Feel the constraint: the table must be `max_value + 1` cells wide. Values
   up to 12 here is cute — what if values reach 10⁹? You can't allocate
   that → Phase 3

**Milestone:** code from memory, in under 5 minutes:
> "Given an array and Q queries, print each value's frequency" — O(n) build,
> O(1) per query. Then explain exactly why `[10**9]` breaks the array
> approach and which Python structure replaces it (`dict` / `Counter`).

---

### Phase 3: Array vs Map — Choosing Your Table (Day 6–7)
No new file — this phase is the bridge to everything else in the repo:
1. Hash **array** (files `01`–`03`): fastest possible O(1), cache-friendly,
   but keys must be small, dense, and non-negative
2. Hash **map** (`dict` in Python, `unordered_map` in C++): any hashable key
   — strings, negatives, tuples — for a little overhead
3. Re-write `01` and `02` using `dict.get(key, 0) + 1` — one line each
4. Connect the dots: `array_medium/01_two_sum.py` ("have I already seen
   `target - x`?") is THIS table used for *lookup* instead of *counting* —
   same idea, different question

**Milestone:** say out loud:
> Frequency array vs `Counter` — when does each win? (Dense, small, known
> range → array. Anything else → map. Never size an array to 10⁹ "just in
> case".)

---

### Phase 4: Maximum Frequency — Hashing Meets Sliding Window ⭐ (Day 8–11)
1. Read `04_maximum_frequency.py` — LeetCode 1838: using at most `k`
   increment operations, what is the largest achievable frequency?
2. Sort first — `[1, 2, 3, 4]` — then a window can be levelled to its
   maximum iff `nums[right] * window_size <= total + k`
3. Trace the shrink loop on `[1, 2, 3, 4]`, `k = 3`: the window grows to
   `[1, 2, 3]` for free (`3×3 = 9 ≤ 6+3`); adding `4` costs `4×4 − 10 = 6 > 3`
   → drop `1` → `[2, 3, 4]` costs `4×3 − 9 = 3 ≤ 3` ✓ → answer `3`
4. Fix the `if __name__ == "main":` guard and re-run — it now prints `3`
5. Complexity: `O(n log n)` sort + `O(n)` window sweep → **O(n log n)** time,
   **O(1)** extra space (the sort is in place)

**Milestone:** solve without hints:
> LC 1838 in under 25 minutes. Then answer: why does sorting make the window
> legal? (A group is always equalised to its *maximum* — raising to anything
> lower wastes operations — and in sorted order that group is contiguous.)

---

### Phase 5: Review & Speed Run (Day 12–14)
1. Re-run `01`, `02`, `03`, and `04` (with its fixed guard) — no peeking
2. Rewrite `01` and `04` from an empty file, timed: 15 min + 25 min
3. Recite the complexities: build `O(n)` + query `O(1)` · LC 1838 `O(n log n)`

**Milestone:** three prompts, one sitting:
> Count letters · count numbers with queries · LC 1838 — all correct, no
> breaks. If that felt routine, this folder is done.

---
## 🧠 Mental Model Cheat Sheet

| Scenario | Technique | Why |
|---|---|---|
| "How often does each letter appear?" | 26-slot array, index = `ord(c) - ord('a')` | The character's code IS the key — direct addressing, no search |
| "Frequency of numbers in a small range `0..W`" | `freq = [0] * (W + 1)`; `freq[v] += 1` | Value-as-index: the slot answers instantly |
| "Q queries after one pass" | Precompute the table once | Build `O(n)`, each query `O(1)` — preprocessing is the entire idea |
| "Keys are huge, negative, or strings" | `dict` / `Counter` / `unordered_map` | Hash tables buy unbounded keys with a little overhead |
| "Values might be out of range" | Guard (`0 <= num < 13`) or fall back to a map | A silent wrong answer is worse than a crash |
| "Largest frequency with k increments" | Sort + sliding window (`04`) | Sorted window is equalisable iff `max × size ≤ sum + k` |
| "Pair that sums to target / duplicates" | Map of what you've seen (`array_medium/01`) | Same table, asked for *complements* instead of *counts* |
| "My queries re-scan the array every time" | Stop. Hash it first. | Re-counting per query is the O(n·Q) trap this folder removes |

---

## 🔑 Pattern Recognition (The Secret to Problem Solving)

### Pattern 1: Direct Addressing (The Frequency Array)
**How to spot it:** "count occurrences" where keys are letters, digits, or
values bounded by a known small maximum.

- allocate `max_key + 1` zeros → one pass of `table[key] += 1` → every
  query is a single index read
- total cost `O(n + Q)` vs the `O(n · Q)` naive loop — this is files
  `01`, `02`, `03`

### Pattern 2: Count with a Map, Look Up the Complement
**How to spot it:** "pair / duplicate / two-sum style" wording with keys
that don't fit inside a small array.

- `freq = collections.Counter(nums)` or `seen = {}` + `target - x` lookup
- this is exactly `array_medium/01_two_sum.py`, plus LC 217 / LC 349
- the map is the SAME idea as Pattern 1 — only the table implementation
  moved from "array slot" to "hashed bucket"

### Pattern 3: Sort + Window for "Make Frequencies Equal" ⭐
**How to spot it:** "largest group that can be levelled with ≤ k
adjustments" — the LC 1838 shape.

- sort, grow `right`, add `nums[right]` to `total`
- shrink while `nums[right] * (right - left + 1) > total + k` — that
  expression IS the increment cost of raising the whole window to
  `nums[right]`
- the window must stay contiguous **in sorted order** because the optimal
  target is always the window's maximum

---
## 📝 30-Day Practice Schedule

| Day | Topic | Problem Set |
|---|---|---|
| 1 | Character hashing | Run `01_character_hashing.py` with `banana` → a:3 n:2 r:0 |
| 2 | The `ord()` trick | Rewrite `01` from memory; explain the 26-slot layout |
| 3 | Number hashing | Run `03_hashing.py` — predict the output BEFORE running |
| 4 | Range guards | Run `02` interactively; feed it a value > 12 |
| 5 | Queries in a loop | GFG: counting frequencies of array elements |
| 6 | Array vs map | Re-code `01`/`02` with `dict.get(k, 0) + 1` |
| 7 | Review week 1 | Rewrite `01` + `03` blind; recite complexities aloud |
| 8 | Complement lookup | LC 1 (Two Sum) with a map · LC 217 (Contains Duplicate) |
| 9 | Set hashing | LC 349 (Intersection of Two Arrays) · LC 128 (Longest Consecutive) |
| 10 | Window intro | Read `04` — trace the shrink loop on paper first |
| 11 | K-shifts ⭐ | Fix the `__main__` guard, then solve LC 1838 timed (≤ 25 min) |
| 12 | Why sorting works | Explain the `max × size ≤ sum + k` inequality out loud |
| 13 | Strings + counting | LC 451 (Sort Characters By Frequency) |
| 14 | Review week 2 | Rewrite `04` from memory; re-run all four files |
| 15 | Prefix sum + map | LC 560 (Subarray Sum Equals K) — counting's next life |
| 16 | Group by key | LC 49 (Group Anagrams) — hash on `tuple(sorted(word))` |
| 17 | Set over sort | LC 128 again — pure set version, no sorting |
| 18 | GFG practice | GFG: frequency of small-ranged values |
| 19 | Speed drill | LC 217 + LC 349 in 15 minutes combined |
| 20 | Review week 3 | Re-solve LC 1838 blind — edge cases first |
| 21 | Backfill: arrays | LC 1 again — hashmap vs sorting debate |
| 22 | Backfill: arrays | LC 560 (count subarrays = k) timed |
| 23 | Weak-spot day | Re-do whichever of `01`–`04` still feels shaky |
| 24 | Teach it | Explain frequency arrays to an empty chair — 5 minutes |
| 25 | GFG practice | GFG: sort elements by frequency |
| 26 | Mixed set | 2 easy + 1 medium hashing problems, no peeking |
| 27 | Timed drill | LC 1838 again — ≤ 20 minutes this time |
| 28 | Mock interview | 45-minute session: 1 hashing + 1 sliding window |
| 29 | Review | Skim this README; tick every checklist box you can |
| 30 | MOCK INTERVIEW DAY | 3 problems — full simulation, camera on |

---

## 💡 Advice From a Mentor

1. **Hashing is preprocessing** — you pay `O(n)` once so every later answer
   is `O(1)`. If you ever re-count inside a query loop, stop and hash
2. **Know your key space** — dense + small + non-negative → array; anything
   else → `dict`. Sizing an array to 10⁹ "just in case" is exactly what
   `02`'s `0..12` guard is teaching you to avoid
3. **Guard out-of-range values** — `02` warns instead of corrupting counts.
   A silent wrong answer is worse than a crash
4. **`ord(c) - ord('a')` should flow from your pen** — it is THE character
   hash; you'll reuse it in strings, graphs, tries, and ciphers
5. **Sort before you window** — `04` is a sliding-window problem wearing a
   hashing costume; the sort is what makes the window contiguous
6. **Know the Python toolbox**: `collections.Counter(nums)`,
   `dict.get(k, 0) + 1`, `defaultdict(int)`, and `set` for "have I seen
   it?" — four tools, one idea
7. **Fix bugs, don't route around them** — `04`'s `"main"` guard is a
   one-string fix; finding it yourself is the exercise (too late now?
   Re-do it from memory anyway)
8. **Patterns > memorization** — frequency table, complement lookup, and
   sort+window are three questions the SAME table keeps answering

---
## 🔗 LeetCode / GFG Problem Links (Copy into browser)

**LeetCode:**
- Frequency of the Most Frequent Element (1838): https://leetcode.com/problems/frequency-of-the-most-frequent-element/
- Two Sum (1): https://leetcode.com/problems/two-sum/
- Contains Duplicate (217): https://leetcode.com/problems/contains-duplicate/
- Intersection of Two Arrays (349): https://leetcode.com/problems/intersection-of-two-arrays/
- Longest Consecutive Sequence (128): https://leetcode.com/problems/longest-consecutive-sequence/
- Sort Characters By Frequency (451): https://leetcode.com/problems/sort-characters-by-frequency/
- Subarray Sum Equals K (560): https://leetcode.com/problems/subarray-sum-equals-k/
- Group Anagrams (49): https://leetcode.com/problems/group-anagrams/

**GeeksforGeeks:**
- Frequency of each element of an array of small ranged values: https://www.geeksforgeeks.org/dsa/frequency-of-each-element-of-an-array-of-small-ranged-values/
- Counting frequencies of array elements: https://www.geeksforgeeks.org/dsa/counting-frequencies-of-array-elements/
- Sort elements by frequency: https://www.geeksforgeeks.org/dsa/sort-elements-by-frequency/

---

## ✅ Final Checklist Before Moving to Binary Search

- [ ] Can define hashing in one sentence ("map a key to a table slot for O(1) access")
- [ ] Can write character-frequency counting from memory using `ord(c) - ord('a')`
- [ ] Can say why `01` crashes on uppercase — and how to fix it (`text.lower()`)
- [ ] Can build a number hash array and state its size formula (`max_value + 1`)
- [ ] Solved a "count frequencies, answer queries" problem with an O(n) build
- [ ] Can explain array vs `dict` — and exactly when each one wins
- [ ] Re-coded `01`/`02` with `dict` in five lines each
- [ ] Found and fixed the `if __name__ == "main":` bug in `04`
- [ ] Solved LC 1838 without help, including the `max × size ≤ sum + k` cost formula
- [ ] Can explain WHY the window must be contiguous after sorting
- [ ] Can name the complexities exactly: build `O(n)` + query `O(1)` · LC 1838 `O(n log n)`
- [ ] Solved at least 10 hashing problems total (this folder + practice links)

> Hashing is the quiet workhorse behind almost every "O(n), but don't be
> dumb about it" interview answer — frequency tables, complement lookups,
> and dedup sets all come from this tiny folder. Next stop:
> **Binary Search** — where you stop scanning the answer and start *halving*
> toward it. Good luck — you've got this! 🚀