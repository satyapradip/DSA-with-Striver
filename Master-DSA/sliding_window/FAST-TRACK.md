# ⚡ Sliding Window — Placement FAST-TRACK (1-Page Cheat Sheet)

> **Revise this in 15 minutes. Print it. Use it before every mock interview.**

---

## 🧩 The Master Template (Memorise This)

```python
def sliding_window(nums, target):
    n = len(nums)
    left = 0
    window_sum = 0
    max_len = 0           # or min_len = float('inf')

    for right in range(n):
        window_sum += nums[right]          # ① expand window

        while window_sum > target:         # ② shrink while invalid
            window_sum -= nums[left]
            left += 1

        update_answer(left, right)         # ③ record best result

    return max_len   # or result
```

---

## 🔑 The 3-Step Mindset

| Step | Question to Ask | Action |
|---|---|---|
| **① Expand** | `right += 1` adds `nums[right]` to window | Always do it first |
| **② Shrink** | Does the window violate the condition? | `while` → subtract `left`, `left += 1` |
| **③ Update** | Have I found a better solution? | `max_len = max(max_len, right-left+1)` or similar |

---

## 🆚 Sliding Window vs Alternatives (Quick Recall)

| Signal | Use |
|---|---|
| "Longest/shortest subarray" with **non-negative numbers** | Sliding Window (O(n)) |
| "Count subarrays with sum = K" with **negatives** | Prefix sum + hashmap (O(n)) |
| Fixed window of size K | Sliding window |
| Longest substring without repeating | Sliding window + `set` or `dict` |

---

## 🎯 Placement Checklist

| ✅ I can… | Day |
|---|---|
| Trace a fixed-size window by hand | Day 1 |
| Write `02_max_subarray_sum_fixed_size.py` from memory | Day 2 |
| Identify *sliding window* vs *hashmap* within 10 seconds | Day 3 |
| Solve all 4 EASY problems in ≤ 60 min | Day 4 |
| Solve all 5 MEDIUM problems in ≤ 90 min | Day 5 |
| Solve MEDIUM problems blind (no editor) | Day 6 |
| Solve all 4 HARD problems in ≤ 120 min | Day 7 |

---

## 📊 Time Targets

| Problem Grade | Target Time | Notes |
|---|---|---|
| Easy | 10–15 min | Focus on getting the pattern right |
| Medium | 20–40 min | Use the template; don't overthink |
| Hard | 30–60 min | Dedicate full session; review after |

---

## 🔁 Spaced Repetition (Memory Retention)

| When | Action |
|---|---|
| Now | Skim this sheet |
| 1 day later | Re-solve `04_longest_substring_without_repeating_chars.py` |
| 3 days later | Re-solve `05_min_size_subarray_sum.py` |
| 7 days later | Re-solve `06_minimum_window_substring.py` |
| On exam day | Only skim this sheet + master template |

---

## 🚨 Common Pitfalls & Fixes

| Pitfall | Fix |
|---|---|
| Window sum recalculated from scratch each iteration | Maintain `window_sum` incrementally |
| `left` pointer reset to 0 every time | **Never reset** `left` — it only moves forward |
| Integer overflow (Python doesn't have this, but in C++: `int` overflow) | Use `long long` in C++/Java |
| Forgetting to update answer **before** moving `right++` | Always update inside the loop, before increment |
| Negative numbers break the window condition | Switch to prefix sum + hashmap |

---

## 🏁 Final Reminder

> *"Sliding Window is not a topic — it's a lens. Once you see the window, you see every array problem differently."*

**You've got this! 🚀**
