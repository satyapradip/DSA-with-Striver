# 📚 Queue Learning Path — Basic to Advanced

Welcome! This is your complete guide to mastering **Queues** from scratch to
interview-level problem solving. Follow this path in order.

---

## 🗺️ The Roadmap

### Phase 1: Foundations (Day 1–2)
1. Understand FIFO (First In First Out) — opposite of Stack's LIFO
2. Run `basics.py` Module 1 — see the simple queue demo
3. Understand WHY the simple list queue is inefficient (O(n) dequeue)

**Milestone:** Answer this without looking:
> What's the difference between `push/pop` (stack) vs `enqueue/dequeue` (queue)?
> Where does each operation happen in a queue?

---

### Phase 2: Efficient Implementation (Day 3–4)
1. Study the **Circular Queue** implementation
2. Understand the magic of `% capacity` (modulo wrapping)
3. Learn `collections.deque` — Python's built-in super queue
4. Implement a circular queue YOURSELF from scratch (no peeking!)

**Milestone:** Code a CircularQueue class from memory:
- `enqueue`, `dequeue`, `peek`, `is_empty`, `is_full`
- All operations must be **O(1)**

---

### Phase 3: Queue ↔ Stack Conversions (Day 5–6)
1. **Queue using Two Stacks** — understand the "transfer" trick
2. **Stack using Two Queues** — understand the "rotate" trick
3. Analyze time complexity of each operation (amortized analysis!)

**Milestone:** Explain to yourself:
> Why is dequeue in QueueUsingStacks "amortized O(1)"?
> Why is push in StackUsingQueues O(n)?

---

### Phase 4: BFS — The Superpower of Queues (Day 7–10)
This is where queues become **powerful**. BFS = Breadth First Search.

1. Study **Rotten Oranges** — multi-source BFS on a grid
2. Understand the queue's role: level-by-level processing
3. Try these BFS classics:
   - 01 Matrix (distance to nearest 0)
   - Number of Islands (could also use DFS)
   - Shortest Path in Binary Matrix
   - Word Ladder (BFS on words!)

**Milestone:** Solve "01 Matrix" on LeetCode WITHOUT hints.

---

### Phase 5: Monotonic Queue / Sliding Window (Day 11–14)
⭐ **THE INTERVIEW GOLD**

1. Study **Sliding Window Maximum** very carefully
2. Understand WHY we remove smaller elements (they're "useless")
3. Try the mirror problem: **Sliding Window Minimum**
4. Practice:
   - Sum of Subarray Minimums / Maximums
   - Longest Continuous Subarray with Absolute Diff ≤ Limit

**Milestone:** Solve "Sliding Window Maximum" on LeetCode 3 times:
- Once following the code
- Once with the explanation closed
- Once from complete memory

---

### Phase 6: Advanced Applications (Day 15+)
1. **Task Scheduler** — greedy + queue reasoning
2. **Design Problems:**
   - Design Hit Counter
   - Moving Average from Data Stream
   - Design Snake Game
   - LRU Cache (uses a doubly linked list + hashmap, but queue intuition helps)
3. **Hard BFS:**
   - Shortest Bridge
   - Open the Lock
   - Minimum Knight Moves

---

## 🧠 Mental Model Cheat Sheet

| Scenario | Data Structure | Why |
|---|---|---|
| "Process in arrival order" | Queue | FIFO natural fit |
| "Level by level / shortest path" | Queue (BFS) | BFS explores level-by-level |
| "Sliding window max/min" | Deque (monotonic) | Remove useless elements |
| "First come first served" | Queue | Task scheduling |
| "Most recent first" | Stack | LIFO natural fit |
| "Last K elements" | Deque | Both ends O(1) |

---

## 🔑 Pattern Recognition (The Secret to Problem Solving)

### Pattern 1: BFS on Grids
**How to spot it:** "Shortest path steps", "Minimum moves/turns",
"spread/rot/infect level by level"

**Template:**
```python
def bfs(grid, starts):
    q = deque(starts)  # Push ALL starting points
    visited = set(starts)
    steps = 0
    while q:
        for _ in range(len(q)):  # Process level by level
            r, c = q.popleft()
            # ... check neighbors, push unvisited ones
        steps += 1
    return steps
```

### Pattern 2: Monotonic Deque
**How to spot it:** "window of size K", "maximum/minimum in every window"

**Template:**
```python
def sliding_window(nums, k):
    dq = deque()  # Stores INDICES
    result = []
    for i in range(len(nums)):
        # 1. Remove outdated (outside window)
        while dq and dq[0] <= i - k:
            dq.popleft()
        # 2. Remove useless (for max: smaller elements)
        while dq and nums[dq[-1]] <= nums[i]:  # >= for min
            dq.pop()
        # 3. Add current
        dq.append(i)
        # 4. Record result
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result
```

### Pattern 3: Queue for Sequential Processing
**How to spot it:** "process in order", "simulation", "repeat until"

---

## 📝 30-Day Practice Schedule

| Day | Topic | Problem Set |
|---|---|---|
| 1 | Queue basics | Run `basics.py` sections 1–2 |
| 2 | Circular Queue | Implement from scratch |
| 3 | deque usage | Play with all deque methods |
| 4 | Queue using 2 stacks | LeetCode 232 |
| 5 | Stack using 2 queues | LeetCode 225 |
| 6 | Review both conversions | Explain out loud |
| 7 | BFS intro | Rotten Oranges (994) |
| 8 | BFS on grid | 01 Matrix (542) |
| 9 | BFS on grid | Number of Islands (200) |
| 10 | BFS on grid | Shortest Path in Binary Matrix (1091) |
| 11 | Monotonic deque | Sliding Window Maximum (239) ⭐ |
| 12 | Monotonic deque | Sliding Window Minimum |
| 13 | Monotonic deque | Longest Subarray with Diff ≤ Limit (1438) |
| 14 | Review monotonic deque | Solve 239 from memory |
| 15 | Greedy + queue | Task Scheduler (621) |
| 16 | Design | Design Hit Counter (362) |
| 17 | Design | Moving Average from Data Stream (346) |
| 18 | BFS on words | Word Ladder (127) |
| 19 | BFS on numbers | Open the Lock (752) |
| 20 | BFS multi-source | Shortest Bridge (934) |
| 21 | Review week 1–3 | Re-solve all Level 1 problems |
| 22–23 | Mock interviews | Pick random problems, 30 min each |
| 24 | Design | Design Snake Game (353) |
| 25 | BFS hard | Perfect Squares (279) |
| 26 | BFS hard | Minimum Knight Moves (1197) |
| 27 | Deque hard | Reveal Cards In Increasing Order (950) |
| 28 | Review week 4 | Re-solve all Level 2 problems |
| 29 | Mock interview | 45-min session, 2 problems |
| 30 | MOCK INTERVIEW DAY | 3 problems — full simulation |

---

## 💡 Advice From a Mentor

1. **Don't just read** — write every implementation by hand
2. **Draw diagrams** — front/rear arrows, wrap-around visualization
3. **Explain out loud** — the "rubber duck" method works!
4. **Spaced repetition** — redo problems at Day 7, 14, 21, 30
5. **Patterns > Memorization** — learn to RECOGNIZE queue patterns
6. **BFS is your new best friend** — it's everywhere in interviews!
7. **Compare with Stack** — everything you learned in Stack has a Queue mirror
8. **Time = O(n), Space = O(k)** for most queue problems — internalize this

---

## 🔗 LeetCode Problem Links (Copy into browser)

- Sliding Window Maximum: https://leetcode.com/problems/sliding-window-maximum/
- Rotten Oranges: https://leetcode.com/problems/rotting-oranges/
- 01 Matrix: https://leetcode.com/problems/01-matrix/
- Number of Islands: https://leetcode.com/problems/number-of-islands/
- Task Scheduler: https://leetcode.com/problems/task-scheduler/
- Word Ladder: https://leetcode.com/problems/word-ladder/
- Open the Lock: https://leetcode.com/problems/open-the-lock/
- Shortest Bridge: https://leetcode.com/problems/shortest-bridge/
- Queue using Stacks: https://leetcode.com/problems/implement-queue-using-stacks/
- Stack using Queues: https://leetcode.com/problems/implement-stack-using-queues/
- Design Hit Counter: https://leetcode.com/problems/design-hit-counter/
- Moving Average: https://leetcode.com/problems/moving-average-from-data-stream/
- Design Snake Game: https://leetcode.com/problems/design-snake-game/

---

## ✅ Final Checklist Before Moving to Trees

- [ ] Can implement CircularQueue from memory (all O(1) ops)
- [ ] Can explain FIFO vs LIFO to a 5-year-old
- [ ] Solved Sliding Window Maximum 3 times independently
- [ ] Solved Rotten Oranges without help
- [ ] Can code BFS template for grids from memory
- [ ] Can code Queue using 2 stacks from memory
- [ ] Built intuition for: "When do I reach for a queue?"
- [ ] Solved at least 15 queue/BFS problems total

> When you finish this roadmap, Trees and Graphs will come MUCH easier
> because they both build on BFS. Good luck — you've got this! 🚀