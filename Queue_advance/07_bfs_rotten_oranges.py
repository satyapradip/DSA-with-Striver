"""
================================================================================
                    BFS - BREADTH FIRST SEARCH WITH QUEUE ⭐⭐⭐
================================================================================
BFS is the SUPERPOWER of queues! It explores level-by-level, exactly like
a queue processes elements in order.

🧠 MENTAL MODEL:
  • Queue processes elements in "waves" (levels)
  • Level 0: starting points
  • Level 1: one step away from start
  • Level 2: two steps away from start
  • ...and so on

WHY QUEUE? Because we need to process elements in the ORDER they were found.
The first element discovered is processed first (FIFO) — this guarantees
we explore level-by-level!

KEY PATTERN: MULTI-SOURCE BFS
  • Sometimes there are MULTIPLE starting points (e.g., multiple rotten oranges)
  • Push ALL starting points into the queue FIRST
  • Then BFS processes them all simultaneously, wave by wave
"""

from collections import deque


# ==============================================================================
# PROBLEM: ROTTEN ORANGES  (LeetCode 994) ⭐⭐⭐ Striver Classic!
# ==============================================================================
# In a grid, 0 = empty cell, 1 = fresh orange, 2 = rotten orange.
# Every minute, any fresh orange adjacent (4-directionally) to a rotten orange
# becomes rotten. Return the minimum minutes until all oranges rot,
# or -1 if impossible.
#
# Example:
#   grid = [[2,1,1],
#           [1,1,0],
#           [0,1,1]]
#   Output: 4
#
# LOGIC (Multi-source BFS):
#   1. Find ALL initially rotten oranges → push into queue (multi-source!)
#   2. BFS level by level, tracking time
#   3. Each neighbor that is fresh becomes rotten and joins queue
#   4. After BFS, check if any fresh orange remains → -1
# ------------------------------------------------------------------------------

def rotten_oranges(grid):
    """
    Find minimum time for all oranges to rot using BFS.
    
    Time Complexity: O(m*n) - visit each cell once
    Space Complexity: O(m*n) - queue size
    """
    rows, cols = len(grid), len(grid[0])
    q = deque()
    fresh_count = 0
    time = 0
    
    print(f"\n   Grid: {grid}")
    print(f"   {'='*60}")
    
    # Step 1: Find all rotten oranges (multi-source) and count fresh
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.append((r, c, 0))  # (row, col, time_rotten)
            elif grid[r][c] == 1:
                fresh_count += 1
    
    print(f"   Initial rotten sources: {list(q)}")
    print(f"   Fresh oranges: {fresh_count}")
    
    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Step 2: BFS
    while q:
        r, c, t = q.popleft()
        time = max(time, t)
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            # If neighbor is fresh, it becomes rotten
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh_count -= 1
                q.append((nr, nc, t + 1))
                print(f"   Minute {t+1}: Orange at ({nr}, {nc}) became rotten!")
    
    # Step 3: Check if any fresh oranges remain
    if fresh_count > 0:
        print(f"   ✗ {fresh_count} fresh orange(s) unreachable → Return -1")
        return -1
    
    print(f"   ✅ All oranges rotten in {time} minutes!")
    return time


# ==============================================================================
# BFS TEMPLATE FOR GRIDS 🧠 (Memorize this!)
# ==============================================================================
"""
THE UNIVERSAL BFS GRID TEMPLATE:
┌─────────────────────────────────────────────────────────────┐
│  def bfs(grid, starts):                                     │
│      rows, cols = len(grid), len(grid[0])                   │
│      q = deque(starts)      # Push ALL starting points      │
│      visited = set(starts)  # Track visited cells           │
│      steps = 0                                              │
│                                                             │
│      while q:                                               │
│          for _ in range(len(q)):  # Process level by level  │
│              r, c = q.popleft()                             │
│              # ... process current cell ...                 │
│                                                             │
│              # Check 4 neighbors                            │
│              for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:     │
│                  nr, nc = r + dr, c + dc                    │
│                  if (0 <= nr < rows and 0 <= nc < cols      │
│                      and (nr,nc) not in visited             │
│                      and grid[nr][nc] is valid):            │
│                      visited.add((nr, nc))                  │
│                      q.append((nr, nc))                     │
│          steps += 1                                         │
│      return steps                                           │
└─────────────────────────────────────────────────────────────┘

KEY POINTS:
  1. Multi-source? Push ALL sources first!
  2. Level-by-level? Use `for _ in range(len(q))` inner loop
  3. 4-directional? Use directions array
  4. Avoid revisiting? Use visited set
  5. Shortest path? BFS guarantees it (first time you reach = shortest)
"""


# ==============================================================================
# PRACTICE PROBLEM: 01 MATRIX  (LeetCode 542) ⭐⭐⭐
# ==============================================================================
# Given a binary matrix, find the distance of the nearest 0 for each cell.
#
# Example:
#   grid = [[0,0,0],
#           [0,1,0],
#           [1,1,1]]
#   Output: [[0,0,0],
#            [0,1,0],
#            [1,2,1]]
#
# LOGIC (Multi-source BFS from ALL zeros!):
#   1. Push ALL cells with 0 into queue (distance 0)
#   2. BFS outward — each fresh cell gets distance = parent + 1
#   3. This guarantees SHORTEST distance (BFS property!)
# ------------------------------------------------------------------------------

def update_matrix(grid):
    """
    Find distance of nearest 0 for each cell using multi-source BFS.
    
    Time Complexity: O(m*n)
    Space Complexity: O(m*n)
    """
    rows, cols = len(grid), len(grid[0])
    q = deque()
    # Result matrix: -1 means unvisited
    dist = [[-1] * cols for _ in range(rows)]
    
    # Step 1: Push ALL zeros as sources (distance 0)
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                dist[r][c] = 0
                q.append((r, c))
    
    print(f"\n   Grid: {grid}")
    print(f"   Initial sources (all zeros): {list(q)}")
    print(f"   {'='*60}")
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Step 2: BFS
    while q:
        r, c = q.popleft()
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            # If neighbor is unvisited, its distance = current + 1
            if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))
                print(f"   Cell ({nr},{nc}) → distance {dist[nr][nc]}")
    
    print(f"\n   ✅ Distance matrix: {dist}")
    return dist


# ==============================================================================
# MAIN FUNCTION
# ==============================================================================

if __name__ == "__main__":
    
    print("\n" + "█" * 60)
    print("██  BFS - BREADTH FIRST SEARCH WITH QUEUE")
    print("█" * 60)
    
    # ──────────────────────────────────────────────────────────────────────────
    # PROBLEM 1: Rotten Oranges
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 PROBLEM 1: ROTTEN ORANGES (BFS)")
    print("=" * 60)
    print()
    print("   🧠 MENTAL MODEL:")
    print("   • Multiple oranges rot at the SAME TIME (multi-source BFS)")
    print("   • Queue processes oranges in waves: minute 0, 1, 2...")
    print("   • This is EXACTLY how BFS works on grids!")
    
    orange_grid = [[2,1,1],[1,1,0],[0,1,1]]
    time_needed = rotten_oranges(orange_grid)
    print(f"\n   ✅ Minimum time: {time_needed} minutes\n")
    
    # ──────────────────────────────────────────────────────────────────────────
    # BFS TEMPLATE
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 THE UNIVERSAL BFS GRID TEMPLATE")
    print("=" * 60)
    print("""
   def bfs(grid, starts):
       rows, cols = len(grid), len(grid[0])
       q = deque(starts)      # Push ALL starting points
       visited = set(starts)  # Track visited cells
       steps = 0
       
       while q:
           for _ in range(len(q)):  # Process level by level
               r, c = q.popleft()
               # ... process current cell ...
               
               for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                   nr, nc = r + dr, c + dc
                   if (0 <= nr < rows and 0 <= nc < cols
                       and (nr,nc) not in visited
                       and grid[nr][nc] is valid):
                       visited.add((nr, nc))
                       q.append((nr, nc))
           steps += 1
       return steps
    """)
    
    # ──────────────────────────────────────────────────────────────────────────
    # PROBLEM 2: 01 Matrix
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 PROBLEM 2: 01 MATRIX (Distance to Nearest 0)")
    print("=" * 60)
    print()
    print("   🧠 KEY INSIGHT:")
    print("   • Push ALL zeros as sources (multi-source BFS)")
    print("   • BFS guarantees SHORTEST distance!")
    
    matrix = [[0,0,0],[0,1,0],[1,1,1]]
    result = update_matrix(matrix)
    print(f"\n   ✅ Result: {result}\n")
    
    print("🚀 NEXT: Run 08_task_scheduler.py to learn a greedy + queue")
    print("   approach to a HOT interview problem!")