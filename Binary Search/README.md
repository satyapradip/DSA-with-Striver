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
<!-- CONTINUE -->