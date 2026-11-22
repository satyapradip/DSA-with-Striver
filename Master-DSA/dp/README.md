# 📚 Dynamic Programming (DP) — Master Guide

> A complete, placement-oriented guide to **Dynamic Programming** — the art of solving
> complex problems by breaking them into overlapping subproblems and storing their results.
> DP is one of the most important topics for placements and coding interviews.

---

## 🗺️ DP Patterns Map

| Pattern | Difficulty | Key Problems | Key Idea |
|---|---|---|---|
| **1. 1D DP** | Easy→Medium | Climbing Stairs, House Robber, House Robber II | State depends on previous 1-2 states |
| **2. 2D DP (Grid)** | Medium→Hard | Min Path Sum, Unique Paths, Dungeon Game | State depends on 2D grid position |
| **3. Knapsack** | Medium→Hard | 0/1 Knapsack, Partition Equal Subset, Coin Change | Each item either taken or not |
| **4. LIS (Longest Increasing Subsequence)** | Medium | LIS, Russian Doll Envelopes | Longest increasing subsequence |
| **5. LCS (Longest Common Subsequence)** | Medium | LCS, Edit Distance, Delete Operation for Two Strings | Longest common subsequence |
| **6. DP on Trees** | Medium→Hard | House Robber III, Binary Tree Tilt, Max Path Sum | DP on tree nodes |
| **7. String DP** | Medium→Hard | Word Break, Palindrome Partitioning, Interleaving | String-based DP |

---

## 🧠 The Core Mindset

### Step 1: Identify the Subproblems
- Break the problem into smaller overlapping subproblems
- Define what state you need to remember

### Step 2: Define the State
- `dp[i]` = the answer for subproblem i
- Can be 1D, 2D, or more dimensions

### Step 3: Define the Recurrence Relation
- How to compute `dp[i]` from previous states
- Base cases are critical!

### Step 4: Choose Top-Down (Memoization) or Bottom-Up (Tabulation)
- **Top-Down**: Recursive + memo (cache) — easier to think about
- **Bottom-Up**: Iterative + table — more efficient, no recursion overhead

---

## 📖 Problem Mapping

| # | Pattern | Easy | Medium | Hard |
|---|---|---|---|---|
| **1. 1D DP** | Easy | Climbing Stairs, House Robber | House Robber II, Coin Change | Minimum Cost Climbing Stairs |
| **2. 2D DP (Grid)** | Easy | Min Path Sum | Unique Paths, Dungeon Game | Maximal Square |
| **3. Knapsack** | Easy | Partition Equal Subset | Coin Change 2 | Target Sum |
| **4. LIS** | Easy | LIS | Russian Doll Envelopes | — |
| **5. LCS** | Easy | Longest Common Subsequence | Edit Distance | Shortest Common Supersequence |
| **6. DP on Trees** | Easy | House Robber III | Binary Tree Tilt | — |
| **7. String DP** | Easy | Palindrome Partitioning | Word Break | Interleaving String |

---

## 🚀 Placement Strategy

### Phase 1: DP Basics (Day 1)
- Understand state definition
- Practice 1D DP problems
- Climbing Stairs, House Robber

### Phase 2: 2D DP (Day 2)
- Grid-based DP
- Min Path Sum, Unique Paths

### Phase 3: Knapsack & LIS (Day 3)
- 0/1 Knapsack
- Longest Increasing Subsequence

### Phase 4: LCS & Edit Distance (Day 4)
- Longest Common Subsequence
- Edit Distance

### Phase 5: DP on Trees (Day 5)
- House Robber III
- Tree DP patterns

### Phase 6: Mock Interviews (Day 6)
- Timed practice
- Simulate real interview conditions

---

## 📚 Resources

| Resource | Link |
|---|---|
| LeetCode DP | https://leetcode.com/tag/dynamic-programming/ |
| GFG DP | https://www.geeksforgeeks.org/dynamic-programming/ |
| NeetCode DP | https://neetcode.io/practice/tags?tag=dynamic-programming |
| YouTube (Errichto) | https://www.youtube.com/watch?v=oS_wRS/q3CZ0 |

---

## ✅ Final Checklist

- [ ] Can identify overlapping subproblems
- [ ] Can define dp state clearly
- [ ] Can write recurrence relation from state
- [ ] Can implement top-down (memoization)
- [ ] Can implement bottom-up (tabulation)
- [ ] Can optimize O(n²) to O(n) space where possible
- [ ] Can solve 1D DP problems (Climbing Stairs, House Robber)
- [ ] Can solve 2D DP problems (Min Path Sum, Unique Paths)
- [ ] Can solve 0/1 Knapsack
- [ ] Can solve LIS and LCS
- [ ] Can solve DP on trees
- [ ] Can explain when to use DP vs Greedy
