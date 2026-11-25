# 📚 Greedy Algorithms — Master Guide

> A complete, placement-oriented guide to **Greedy Algorithms** — making locally optimal choices at each step
> with the hope of finding a global optimum. Greedy is one of the most important topics for placements.

---

## 🗺️ Greedy Patterns Map

| Pattern | Difficulty | Key Problems | Key Idea |
|---|---|---|---|
| **1. Activity Selection** | Easy→Medium | Assign Cookies, Non-overlapping Intervals | Sort by end time, pick greedily |
| **2. Fractional Knapsack** | Easy→Medium | Lemonade Change, Partition Labels | Sort by value/weight ratio |
| **3. Interval Merging** | Easy→Medium | Merge Intervals, Insert Interval | Sort by start time, merge overlapping |
| **4. Huffman Coding** | Medium | Task Scheduler | Priority queue for optimal scheduling |
| **5. Minimum Spanning Tree** | Hard | Meeting Rooms II | Prim's/Kruskal's algorithm |
| **6. Shortest Path** | Hard | Jump Game II | Greedy reach forward |
| **7. Coin Change** | Hard | Candy | Two-pass greedy |

---

## 🧠 The Core Mindset

### Greedy Choice Property
- Make the best choice at each step without considering future consequences
- Once a choice is made, never reconsider it

### Optimal Substructure
- The optimal solution contains optimal solutions to subproblems

### Greedy vs DP vs Divide & Conquer
| Approach | Key Idea | When to Use |
|---|---|---|
| **Greedy** | Local optimal choice → global optimal | Problems with greedy choice property |
| **DP** | Overlapping subproblems → memoize/tabulate | Problems needing exploration of all options |
| **Divide & Conquer** | Break into independent subproblems | Problems decomposable into smaller parts |

---

## 📖 Problem Mapping

| # | Pattern | Easy | Medium | Hard |
|---|---|---|---|---|
| **1. Activity Selection** | Easy | Assign Cookies, Lemonade Change | Non-overlapping Intervals, Partition Labels | — |
| **2. Interval Merging** | Easy | Monotonic Array | Merge Intervals, Insert Interval | — |
| **3. Priority Queue** | Easy | Majority Element | Task Scheduler | Meeting Rooms II |
| **4. Forward Greedy** | Medium | — | — | Jump Game II, Gas Station |
| **5. Two-Pass Greedy** | Medium | — | — | Candy |
| **6. Huffman Coding** | Medium | — | Task Scheduler | — |
| **7. MST/Shortest Path** | Hard | — | — | Meeting Rooms II |

---

## 🚀 Placement Strategy

### Phase 1: Greedy Basics (Day 1)
- Understand greedy choice property
- Practice Activity Selection problems
- Assign Cookies, Lemonade Change

### Phase 2: Interval Problems (Day 2)
- Sort intervals by start/end time
- Merge Intervals, Non-overlapping Intervals

### Phase 3: Priority Queue Greedy (Day 3)
- Task Scheduler, Majority Element
- Meeting Rooms II

### Phase 4: Forward Greedy (Day 4)
- Jump Game II, Gas Station
- Understand reach forward strategy

### Phase 5: Two-Pass Greedy (Day 5)
- Candy, Two-pass left-to-right then right-to-left

### Phase 6: Mock Interviews (Day 6)
- Timed practice
- Simulate real interview conditions

---

## 📚 Resources

| Resource | Link |
|---|---|
| LeetCode Greedy | https://leetcode.com/tag/greedy/ |
| GFG Greedy | https://www.geeksforgeeks.org/greedy-algorithms/ |
| NeetCode Greedy | https://neetcode.io/practice/tags?tag=greedy |
| YouTube (Aditi) | https://www.youtube.com/watch?v=xe_M-tbXK6c |

---

## ✅ Final Checklist

- [ ] Can identify when greedy works vs when DP is needed
- [ ] Can sort intervals by start/end time correctly
- [ ] Can implement Activity Selection greedy
- [ ] Can use priority queue for greedy scheduling
- [ ] Can implement Jump Game II forward greedy
- [ ] Can solve Candy two-pass greedy
- [ ] Can explain why greedy works for specific problems
- [ ] Can prove greedy choice property (when needed)
