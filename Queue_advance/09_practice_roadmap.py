"""
================================================================================
                    QUEUE PRACTICE ROADMAP 📚
================================================================================
Your complete learning path from beginner to advanced!

HOW TO USE THIS FILE:
  1. Work through each level IN ORDER
  2. Check off items as you complete them
  3. Revisit Level 1-2 periodically (spaced repetition)
  4. Move to the next level only when comfortable
"""

# ==============================================================================
# QUEUE PRACTICE ROADMAP (Beginner → Advanced)
# ==============================================================================

print("""
================================================================================
📋 QUEUE MASTERY CHECKLIST
================================================================================

🟢 LEVEL 1: BASIC (Master the fundamentals)
   ☐ Queue = FIFO (First In First Out)
   ☐ enqueue at REAR, dequeue from FRONT
   ☐ Implement queue using list (01_queue_basics.py ✅)
   ☐ Implement circular queue (02_circular_queue.py ✅)
   ☐ Understand collections.deque (03_deque.py ✅)
   ☐ Queue using two stacks (04_queue_stack_conversions.py ✅)
   ☐ Stack using two queues (04_queue_stack_conversions.py ✅)
   ☐ Generate binary numbers (05_basic_problems.py ✅)
   ☐ Reverse first K elements of queue (05_basic_problems.py ✅)
   ☐ Implement queue using linked list (YOUR TURN!)
   ☐ Design a deque using circular array (YOUR TURN!)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🟡 LEVEL 2: INTERMEDIATE (Build patterns)
   ☐ First negative in every window (05_basic_problems.py ✅)
   ☐ Sliding Window Maximum - MONOTONIC DEQUE! (06_monotonic_queue.py ✅)
   ☐ Sliding Window Minimum (06_monotonic_queue.py ✅)
   ☐ Sum of min & max in all windows (06_monotonic_queue.py ✅)
   ☐ Rotten Oranges - BFS (07_bfs_rotten_oranges.py ✅)
   ☐ 01 Matrix - multi-source BFS (07_bfs_rotten_oranges.py ✅)
   ☐ Task Scheduler - greedy (08_task_scheduler.py ✅)
   ☐ Reversing a queue using recursion (YOUR TURN!)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔴 LEVEL 3: ADVANCED (Interview-ready)
   ☐ Longest valid parentheses
   ☐ Shortest path in binary matrix (BFS)
   ☐ Design Snake Game (deque usage)
   ☐ Reveal cards in increasing order (deque simulation)
   ☐ Longest Continuous Subarray with Diff ≤ Limit
   ☐ Perfect Squares (BFS on numbers)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚫ LEVEL 4: CHALLENGING (For the brave!)
   ☐ Shortest bridge (multi-source BFS)
   ☐ Minimum knight moves (BFS on chessboard)
   ☐ Word Ladder (famous BFS problem!)
   ☐ Open the Lock (BFS with states)
   ☐ Moving Average from Data Stream

================================================================================
🧠 MEMORIZE THESE PATTERNS
================================================================================

PATTERN 1: BFS ON GRIDS
  "Shortest path steps" / "Minimum moves" / "spread level by level"
  
  Template:
    q = deque(starts)      # Push ALL starting points
    visited = set(starts)
    steps = 0
    while q:
        for _ in range(len(q)):  # Level by level
            r, c = q.popleft()
            # check 4 neighbors, push unvisited valid ones
        steps += 1

PATTERN 2: MONOTONIC DEQUE
  "Window of size K" / "max/min in every window"
  
  Template:
    dq = deque()  # stores INDICES
    for i in range(len(nums)):
        while dq and dq[0] <= i - k: dq.popleft()     # outdated
        while dq and nums[dq[-1]] <= nums[i]: dq.pop() # useless (max)
        dq.append(i)
        if i >= k - 1: result.append(nums[dq[0]])

PATTERN 3: QUEUE FOR SEQUENTIAL PROCESSING
  "Process in order" / "simulation" / "first come first serve"

================================================================================
💪 MENTOR TIPS
================================================================================

1. ALWAYS draw the queue on paper - front and rear arrows!
2. Queue = BFS. "Shortest path" → think queue
3. Sliding window problems → think DEQUE (monotonic queue)
4. Multi-source BFS → push ALL starting points into queue first!
5. BFS is level-by-level - the level = distance from source
6. Practice Sliding Window Maximum at least 5 times!
7. Compare with Stack: everything has a mirror
8. Don't just read - WRITE every implementation by hand

================================================================================
🎯 30-DAY PRACTICE SCHEDULE
================================================================================

Day 1-2:   Queue basics, run 01 & 02
Day 3-4:   deque, run 03, implement CircularQueue from scratch
Day 5-6:   Queue ↔ Stack conversions, run 04
Day 7-10:  BFS, run 07, solve Rotten Oranges & 01 Matrix
Day 11-14: Monotonic deque, run 06, solve Sliding Window Maximum 3x!
Day 15+:   Task Scheduler, run 08, then Level 3-4 problems
Day 21:    Review everything - re-run all files
Day 30:    MOCK INTERVIEW - solve 3 problems in 45 min!

================================================================================
✅ FINAL CHECKLIST BEFORE MOVING TO TREES
================================================================================

   ☐ Can implement CircularQueue from memory (all O(1) ops)
   ☐ Can explain FIFO vs LIFO to a 5-year-old
   ☐ Solved Sliding Window Maximum 3 times independently
   ☐ Solved Rotten Oranges without help
   ☐ Can code BFS template for grids from memory
   ☐ Can code Queue using 2 stacks from memory
   ☐ Built intuition for: "When do I reach for a queue?"
   ☐ Solved at least 15 queue/BFS problems total

   When you finish, Trees & Graphs will come MUCH easier
   because they both build on BFS. You've got this! 🚀
""")


# ==============================================================================
# LEETCODE PROBLEM LINKS FOR REFERENCE
# ==============================================================================

LEETCODE_PROBLEMS = {
    "Sliding Window Maximum": "https://leetcode.com/problems/sliding-window-maximum/",
    "Rotten Oranges": "https://leetcode.com/problems/rotting-oranges/",
    "01 Matrix": "https://leetcode.com/problems/01-matrix/",
    "Number of Islands": "https://leetcode.com/problems/number-of-islands/",
    "Task Scheduler": "https://leetcode.com/problems/task-scheduler/",
    "Word Ladder": "https://leetcode.com/problems/word-ladder/",
    "Open the Lock": "https://leetcode.com/problems/open-the-lock/",
    "Shortest Bridge": "https://leetcode.com/problems/shortest-bridge/",
    "Queue using Stacks": "https://leetcode.com/problems/implement-queue-using-stacks/",
    "Stack using Queues": "https://leetcode.com/problems/implement-stack-using-queues/",
    "Design Hit Counter": "https://leetcode.com/problems/design-hit-counter/",
    "Moving Average": "https://leetcode.com/problems/moving-average-from-data-stream/",
    "Design Snake Game": "https://leetcode.com/problems/design-snake-game/",
    "Perfect Squares": "https://leetcode.com/problems/perfect-squares/",
    "Minimum Knight Moves": "https://leetcode.com/problems/minimum-knight-moves/",
}


if __name__ == "__main__":
    print("\n" + "█" * 60)
    print("██  QUEUE PRACTICE ROADMAP")
    print("█" * 60)
    
    # The big checklist is printed above
    
    print("\n📌 LEETCODE PROBLEM LINKS:")
    print("-" * 60)
    for name, url in LEETCODE_PROBLEMS.items():
        print(f"   • {name}: {url}")
    
    print()
    print("🔥 REMEMBER: Consistency beats intensity!")
    print("   Practice 30 minutes EVERY day, not 4 hours once a week!")