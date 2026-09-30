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
>   try: string `banana` with queries `a n r` (→ 3, 2, 1), and array
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
<!-- CONTINUE -->