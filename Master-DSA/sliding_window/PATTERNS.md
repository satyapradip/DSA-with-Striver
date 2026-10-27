# 🔎 Array Patterns — How to Recognise "Sliding Window"

> Copy-paste friendly reference. Use this to **spot** sliding window problems in seconds.

---

## 🧠 The Sliding Window Recognition Checklist

Ask **these 4 questions** in order:

| Q | Question | Signal | Verdict |
|---|---|---|---|
| 1 | Is it about a **contiguous** segment? | Subarray, substring, substring | ✅ Likely window |
| 2 | Is it asking for **longest/shortest/max/min/count** over a condition? | "longest", "shortest", "number of subarrays", "max sum" | ✅ Likely window |
| 3 | Is the condition **sum/prod/avg/unique count** based? | Sum = K, product < K, max vowels, max unique chars | ✅ Likely window |
| 4 | Are the numbers **non-negative**? | Yes → window works. No → slide to prefix sum | ⚠️ Check negatives |

**Only YES to all four → Sliding Window ✅**

---

## 📐 Pattern vs Technique Map

| Pattern | What it actually is | When to use | Time |
|---|---|---|---|
| **Fixed-Size Sliding Window** | Slide a window of constant `K` | "Max/Min sum of size K", "max avg of K", "count windows with sum K" | O(n) |
| **Variable-Size Sliding Window** | Window shrinks when condition breaks | "Longest substring w/o repeating", "min subarray sum ≥ target" | O(n) |
| **Prefix Sum + Hashmap** | Replaces re-computation with stored cumulative values | "Number of subarrays with sum = K" *(negatives)*, "count pairs with difference" | O(n) |
| **Two Pointers (Sorted)** | Two separate indices moving based on sortedness | "Pair sum", "count triplets", "3sum" | O(n) |

---

## 🚫 When NOT to Use Sliding Window

| Situation | Why window fails | Use instead |
|---|---|---|
| **Negatives in array** | Subtracting `nums[left]` can increase `current_sum`, breaking the `while` condition | Prefix sum + hashmap (O(n)) |
| **Non-contiguous elements** | "Subsequence" not "subarray" | DP / greedy / sorting + pointers |
| **Tree/Graph adjacency** | Windows assume linear index | BFS/DFS / adjacency list |
| **K-th smallest/median** | Order statistics need different data structures | Heap / quick-select |

---

## 📈 Complexity Cheat Sheet

| Approach | Time | Space |
|---|---|---|
| Brute force (nested loops) | O(n²) | O(1) |
| **Fixed window** | **O(n)** | **O(1)** |
| **Variable window** | **O(n)** | **O(1)** or O(K) for hashmap |
| Prefix sum + hashmap | O(n) | O(n) |

---

## 🔑 Key Insight: The "Running Sum" Trick

**The core of sliding window** is:
```
window_sum = sum(arr[left..right])
```
But we DON'T recompute. We maintain:
```
window_sum += nums[right]     # expand
window_sum -= nums[left]      # shrink
```
This turns **O(n²) → O(n)**.

---

## 🧪 10 Quick Recognition Examples

| Problem | Recognised as |
|---|---|
| Max consecutive 1s | Fixed window (count 1s in window of size = window length) |
| Longest substring w/o repeating | Variable window |
| Subarray sum = K | Prefix sum + hashmap (check negatives first) |
| Max sum of size K | Fixed window |
| Min window substring | Variable window + 2`need`/`have` maps |
| Maximum product subarray | DP (cannot use simple window) |
| Longest increasing subarray | Variable window + increasing check |
| Count subarrays with sum 0 | Prefix sum map |
| Sorted & rotated | Two pointers (not window) |
| Find pair sum | Two pointers (sorted) or hashmap (unsorted) |

---

## 🎯 Memory Aid

```
"Window" → "Contiguous" + "Condition" + "Non-negative"
If any is NO → pick the alternative.
```

---

## 📚 References (Before Exam / Interview)

| Resource | Link |
|---|---|
| LeetCode — Sliding Window | https://leetcode.com/tag/sliding-window/ |
| GFG — Sliding Window | https://www.geeksforgeeks.org/sliding-window-maximum-in-an-array/ |
| Striver's Slide Pattern | (Search "striver sliding window pattern") |
| NeetCode — Sliding Window | https://neetcode.io/patterns/sliding-window |

> **Keep this file open while practicing. Over ~5 days, recognition becomes instant.**
