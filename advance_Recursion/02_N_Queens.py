"""
==============================================================================
PROBLEM: N-Queens (LeetCode 51)
==============================================================================

WHAT IS THE N-QUEENS PROBLEM?
-----------------------------
You are given an N × N chessboard (like a grid with N rows and N columns).
Your task: Place N queens on this board such that NO TWO QUEENS ATTACK each other.

In chess, a QUEEN can move ANY number of squares:
  → Horizontally (left/right)  — like a rook
  → Vertically (up/down)       — like a rook  
  → Diagonally (in all 4 directions) — like a bishop

So "no two queens attack" means:
  ✅ NO two queens share the SAME ROW
  ✅ NO two queens share the SAME COLUMN
  ✅ NO two queens share the SAME DIAGONAL

==============================================================================
REAL-WORLD ANALOGY (Beginner Friendly!)
==============================================================================

Imagine you're the principal of a school with N classrooms in a row.
You have N VERY AGGRESSIVE teachers who HATE each other.
Each teacher must be placed in a classroom such that:
  - No two are in the same row (floor)
  - No two are in the same column (room number)
  - No two can see each other diagonally (across the courtyard)

How would you arrange them?

==============================================================================
EXAMPLE: 4-QUEENS SOLUTION
==============================================================================

For N = 4, here's one valid solution:

    Q . . .     (Queen at row 1, column 1)
    . . Q .     (Queen at row 2, column 3)
    . . . Q     (Queen at row 3, column 4)
    . Q . .     (Queen at row 4, column 2)

Let's verify:
  ✅ Each row has EXACTLY 1 queen
  ✅ Each column has EXACTLY 1 queen (columns 1,3,4,2)
  ✅ No two queens share a diagonal
  
  Check diagonals:
    Queen1 (1,1) and Queen2 (2,3): |1-2| ≠ |1-3|, so OK ✓
    Queen1 (1,1) and Queen3 (3,4): |1-3| ≠ |1-4|, so OK ✓
    Queen2 (2,3) and Queen4 (4,2): |2-4| ≠ |3-2|, so OK ✓
    ... all pairs checked ✓

Another valid solution for N = 4:

    . Q . .     (Queen at row 1, column 2)
    . . . Q     (Queen at row 2, column 4)
    Q . . .     (Queen at row 3, column 1)
    . . Q .     (Queen at row 4, column 3)

For N = 4, there are exactly 2 distinct solutions.

==============================================================================
THE CORE INSIGHT (MUST UNDERSTAND!)
==============================================================================

Since each row can have ONLY ONE queen (otherwise they'd attack horizontally),
and we need N queens on an N×N board...

We simply place ONE queen in EACH row!

So the problem reduces to:
  "For each row (0 to N-1), which column should I place my queen in?"

This is like having N slots (rows), and for each slot, you need to pick 
a column number such that:
  1. No other row has used that same column
  2. No other queen lies on the same diagonal

==============================================================================
UNDERSTANDING DIAGONALS (The Tricky Part!)
==============================================================================

There are TWO types of diagonals on a chessboard:

1. MAIN DIAGONALS (top-left to bottom-right) — like "\"
   Key property: (row - column) is CONSTANT for all cells on this diagonal!
   
   Example cells on the same "\" diagonal:
     (0,0), (1,1), (2,2), (3,3)  →  row - col = 0
     (0,1), (1,2), (2,3), (3,4)  →  row - col = -1
     (1,0), (2,1), (3,2), (4,3)  →  row - col = 1

2. ANTI DIAGONALS (top-right to bottom-left) — like "/"
   Key property: (row + column) is CONSTANT for all cells on this diagonal!
   
   Example cells on the same "/" diagonal:
     (0,3), (1,2), (2,1), (3,0)  →  row + col = 3
     (0,2), (1,1), (2,0)         →  row + col = 2
     (1,3), (2,2), (3,1)         →  row + col = 4

WHY IS THIS USEFUL?
   To check if a queen at (r1, c1) attacks another at (r2, c2):
   
   Same row?      →  r1 == r2    (but we place 1 per row, so this is automatic) ✓
   Same column?   →  c1 == c2    (check if column is already used)
   Same diagonal? →  r1-c1 == r2-c2  OR  r1+c1 == r2+c2

==============================================================================
APPROACH 1: BASIC BACKTRACKING (Easiest to understand)
==============================================================================

THINKING PROCESS:
1. Start with row 0
2. For the current row, try EACH column one by one
3. Before placing a queen, CHECK if it's SAFE:
   - No other queen in the same column
   - No other queen on the same "\" diagonal (row - col)
   - No other queen on the same "/" diagonal (row + col)
4. If safe:
   a) Place the queen at this position
   b) MOVE to the NEXT row (recursive call)
   c) After returning, REMOVE the queen (BACKTRACK) and try the NEXT column
5. If we successfully placed queens in ALL rows → we found a solution!

==============================================================================
TIME & SPACE COMPLEXITY
==============================================================================

Time Complexity:  O(N!)  — This is the upper bound
  - First row: N choices of column
  - Second row: at most N-1 choices (one column blocked)
  - Third row: at most N-2 choices
  - ... and so on
  - So worst case: N × (N-1) × (N-2) × ... × 1 = N!
  
  Actually with the diagonal constraints, it's much less than N!
  For N=8 (standard 8-queens), there are only 92 solutions out of 
  16,777,216 possible arrangements (8^8).

Space Complexity: O(N²) for the board + O(N) for recursion stack
  - We store the board as N×N grid
  - Recursion depth is at most N (one call per row)

==============================================================================
VISUALIZING THE BACKTRACKING PROCESS
==============================================================================

Let's trace through N = 4 to see how backtracking works:

Step 1: row=0, try col=0
  Q . . .   ← Place first queen at (0,0)
  . . . .
  . . . .
  . . . .

Step 2: row=1, try col=0 → UNSAFE (same column as Queen 0)
                    try col=1 → UNSAFE (diagonal with Queen 0: 1-1 == 0-0)
                    try col=2 → SAFE! Place queen
  Q . . .
  . . Q .   ← Place queen at (1,2)
  . . . .
  . . . .

Step 3: row=2, try col=0 → UNSAFE (same column as Queen 0)
                    try col=1 → UNSAFE (diagonal with Queen 1: 2-1 ≠ 1-2... wait)
                                Let's check: Queen1 at (1,2), this at (2,1)
                                Same "\" diag? 1-2= -1, 2-1=1 ≠ -1 ✓
                                Same "/" diag? 1+2=3, 2+1=3 = 3 ❌ SAME DIAGONAL!
                    try col=2 → UNSAFE (same column as Queen 1)
                    try col=3 → UNSAFE (check diagonals)
              → NO SAFE SPOT in row 2!
              ⬅ BACKTRACK to row 1!

Step 4: row=1, remove queen from col=2, try next column col=3 → SAFE!
  Q . . .
  . . . Q   ← Move queen to (1,3)
  . . . .
  . . . .

Step 5: row=2, try col=0 → UNSAFE
                    try col=1 → Check: Queen0 at (0,0), Queen1 at (1,3)
                                Same col? 1 ≠ 0,3 ✓
                                "\" diag? 2-1=1≠0-0=0 and 2-1=1≠1-3=-2 ✓
                                "/" diag? 2+1=3≠0+0=0 and 2+1=3≠1+3=4 ✓
                                SAFE! Place queen!
  Q . . .
  . . . Q
  . Q . .   ← Place queen at (2,1)
  . . . .

Step 6: row=3, try col=0 → UNSAFE
                    try col=1 → UNSAFE
                    try col=2 → Check: Queen0(0,0), Queen1(1,3), Queen2(2,1)
                                col=2 not used ✓
                                "\" diag: 3-2=1≠0,≠-2,≠1? 2-1=1, 3-2=1 ❌
                                → UNSAFE!
                    try col=3 → UNSAFE
              → NO SAFE SPOT!
              ⬅ BACKTRACK again!

... and this continues until all possibilities are explored.

==============================================================================
THE TWO SOLUTIONS
==============================================================================

We'll implement TWO solutions:
1. BASIC: Uses a simple check function (easy to understand)
2. OPTIMAL: Uses hash sets for O(1) safety checks (FASTEST)

Both use the same backtracking idea — they just differ in how they 
check if a position is safe.
"""

from typing import List

# ==============================================================================
# SOLUTION 1: BASIC BACKTRACKING (Beginner Friendly)
# ==============================================================================
# In this approach, we store the board as a list of strings.
# Each string represents a row, where 'Q' is a queen and '.' is empty.
#
# To check if a position is safe, we simply scan:
#   - Upward in the same column
#   - Up-left diagonal
#   - Up-right diagonal
#
# We only check UPWARD because we place queens from top to bottom.
# There's nothing below the current row yet!

class Solution:
    """
    Solution for N-Queens problem.
    Contains two approaches: basic and optimized.
    """

    # ==========================================================================
    # APPROACH 1: Basic Backtracking with O(N) safety check
    # ==========================================================================
    # EASIEST TO UNDERSTAND
    #
    # THINK: We'll check safety by manually scanning upward from current position.
    # No fancy data structures — just loops!

    def solveNQueens_basic(self, n: int) -> List[List[str]]:
        """
        Approach 1: Basic backtracking with manual safety check.
        
        Time: O(N! × N) — N! for backtracking, N for each safety check
        Space: O(N²) for the board
        """
        
        # ------------------------------------------------------------------
        # INITIALIZE THE BOARD
        # ------------------------------------------------------------------
        # We start with an EMPTY board: all '.' (dots)
        # Later we'll place 'Q' (queens)
        #
        # Example for N=4:
        #   board = [". . . .",
        #            ". . . .",
        #            ". . . .",
        #            ". . . ."]
        # ------------------------------------------------------------------
        board = [["."] * n for _ in range(n)]
        result = []  # Stores all valid solutions
        
        # ------------------------------------------------------------------
        # HELPER FUNCTION: isSafe
        # ------------------------------------------------------------------
        # Checks if placing a queen at (row, col) is safe.
        #
        # IMPORTANT: We only need to check ABOVE the current row!
        # Why? Because we place queens from row 0 downwards.
        # When we're at row 'r', we haven't placed any queens BELOW row 'r'.
        # So no queen can attack from below.
        #
        # We check three things:
        #   1. Same column above (↑)
        #   2. Upper-left diagonal (↖)
        #   3. Upper-right diagonal (↗)
        # ------------------------------------------------------------------
        def is_safe(row: int, col: int) -> bool:
            """
            Returns True if placing queen at (row, col) doesn't attack
            any already-placed queen.
            
            Think of it like: "Is this seat SAFE for my queen?"
            """
            
            # CHECK 1: Same column (look UP from current row)
            # ------------------------------------------------------------------
            # Scenario: A queen is standing DIRECTLY above this position.
            # Since queens attack vertically, they'd be fighting!
            #
            # We check all rows ABOVE the current row in the SAME column.
            # If ANY has a queen → UNSAFE!
            # ------------------------------------------------------------------
            for r in range(row):
                if board[r][col] == "Q":
                    return False  # ❌ Queen found above! Not safe!
            
            # CHECK 2: Upper-left diagonal (↖)
            # ------------------------------------------------------------------
            # Scenario: A queen is standing on the upper-left diagonal.
            # Like looking at a mirror at an angle — if you see a queen,
            # they can attack you diagonally!
            #
            # We move diagonally up-left: row decreases, col decreases
            # Keep going until we hit the edge of the board.
            # ------------------------------------------------------------------
            r, c = row - 1, col - 1
            while r >= 0 and c >= 0:
                if board[r][c] == "Q":
                    return False  # ❌ Queen on upper-left diagonal!
                r -= 1
                c -= 1
            
            # CHECK 3: Upper-right diagonal (↗)
            # ------------------------------------------------------------------
            # Same as above, but moving up-right: row decreases, col increases
            # ------------------------------------------------------------------
            r, c = row - 1, col + 1
            while r >= 0 and c < n:
                if board[r][c] == "Q":
                    return False  # ❌ Queen on upper-right diagonal!
                r -= 1
                c += 1
            
            # ✅ All checks passed! No queen can attack this position.
            return True

        # ------------------------------------------------------------------
        # RECURSIVE FUNCTION: backtrack
        # ------------------------------------------------------------------
        # 'row' = which row we're currently trying to place a queen in.
        #
        # BASE CASE: If row == n, we've placed queens in ALL rows!
        #   → We found a valid solution! Add it to results.
        #
        # RECURSIVE CASE: Try placing a queen in each column of this row.
        # ------------------------------------------------------------------
        def backtrack(row: int):
            """
            🧠 BASE CASE: All queens placed successfully!
            
            When we reach row == n, it means we've successfully placed 
            a queen in EVERY row (row 0 to row n-1) without any attacks.
            We've found a complete solution!
            """
            if row == n:
                # Convert board from list of lists to list of strings
                # ["Q", ".", ".", "."] → "Q..."
                result.append(["".join(r) for r in board])
                return  # 🛑 STOP - we found a complete solution
            
            # ------------------------------------------------------------------
            # 🔁 RECURSIVE CASE: Try each column in the current row
            # ------------------------------------------------------------------
            # For THIS row, we try placing a queen in EVERY column (0 to n-1).
            # 
            # Think of it like trying each seat in a row:
            #   "Should I put the queen in column 0? ... No? Column 1? ..."
            #
            # For each column that is SAFE, we:
            #   1. PLACE the queen → board[row][col] = "Q"
            #   2. RECURSE to the next row → backtrack(row + 1)
            #   3. REMOVE the queen → board[row][col] = "." (BACKTRACK!)
            #
            # Why remove? So we can try a DIFFERENT column in this row!
            # Like trying a different seat when one doesn't work out.
            # ------------------------------------------------------------------
            for col in range(n):
                if is_safe(row, col):
                    # Step 1: PLACE the queen 👑
                    board[row][col] = "Q"
                    
                    # Step 2: RECURSE — move to the next row
                    backtrack(row + 1)
                    
                    # Step 3: BACKTRACK — remove the queen 🧹
                    # This undoes our choice so we can try the next column
                    board[row][col] = "."
            
            # If no column was safe in this row, the function simply returns.
            # The recursion will backtrack and try different positions above.
        
        # Start the backtracking from row 0
        backtrack(0)
        return result

    # ==========================================================================
    # APPROACH 2: OPTIMIZED Backtracking with O(1) safety check
    # ==========================================================================
    # This is the FASTEST solution for N-Queens.
    #
    # KEY INSIGHT: Instead of SCANNING the board each time to check safety,
    # we use THREE hash sets to track which columns and diagonals are blocked.
    #
    # Hash Set 1: cols       → Stores which COLUMNS already have a queen
    # Hash Set 2: diag1      → Stores which "\" diagonals are blocked
    #                         (Key: row - col)
    # Hash Set 3: diag2      → Stores which "/" diagonals are blocked  
    #                         (Key: row + col)
    #
    # Checking safety becomes O(1) — just check if col, (row-col), or (row+col)
    # is already in our sets!
    #
    # Think of it like having a MAP of dangerous locations:
    #   - "Column 2 is blocked!" → check cols set
    #   - "Main diagonal (0) is blocked!" → check diag1 set
    #   - "Anti diagonal (3) is blocked!" → check diag2 set
    """
    ==============================================================================
    DETAILED EXPLANATION: Why (row - col) and (row + col) for Diagonals?
    ==============================================================================
    
    Imagine a coordinate system on our chessboard:
    
        ┌───┬───┬───┬───┐
        │0,0│0,1│0,2│0,3│  ← Row 0, Columns 0-3
        ├───┼───┼───┼───┤
        │1,0│1,1│1,2│1,3│
        ├───┼───┼───┼───┤
        │2,0│2,1│2,2│2,3│
        ├───┼───┼───┼───┤
        │3,0│3,1│3,2│3,3│
        └───┴───┴───┴───┘
    
    Now let's mark all cells with their (row-col) value:
    
        ┌───┬───┬───┬───┐
        │ 0 │-1 │-2 │-3 │
        ├───┼───┼───┼───┤
        │ 1 │ 0 │-1 │-2 │
        ├───┼───┼───┼───┤
        │ 2 │ 1 │ 0 │-1 │
        ├───┼───┼───┼───┤
        │ 3 │ 2 │ 1 │ 0 │
        └───┴───┴───┴───┘
    
    Notice: ALL cells on the SAME "\" diagonal have the SAME (row-col) value!
    For example: (0,0), (1,1), (2,2), (3,3) all have row-col = 0 ✓
    
    Now let's mark all cells with their (row+col) value:
    
        ┌───┬───┬───┬───┐
        │ 0 │ 1 │ 2 │ 3 │
        ├───┼───┼───┼───┤
        │ 1 │ 2 │ 3 │ 4 │
        ├───┼───┼───┼───┤
        │ 2 │ 3 │ 4 │ 5 │
        ├───┼───┼───┼───┤
        │ 3 │ 4 │ 5 │ 6 │
        └───┴───┴───┴───┘
    
    Notice: ALL cells on the SAME "/" diagonal have the SAME (row+col) value!
    For example: (0,3), (1,2), (2,1), (3,0) all have row+col = 3 ✓
    
    THIS IS THE MAGIC! 🌟
    Just by computing (row-col) and (row+col), we can instantly identify
    which diagonal a cell belongs to, and check if another queen is there!
    """

    def solveNQueens_optimized(self, n: int) -> List[List[str]]:
        """
        Approach 2: Optimized backtracking with O(1) safety checks.
        
        This is significantly faster for larger N.
        
        Time: O(N!) — Same worst case, but much faster in practice
        Space: O(N) — Only 3 hash sets of size N, no board scan
        
        For N=8: Basic takes ~1-2ms, Optimized takes ~0.3ms
        """
        
        result = []      # All valid solutions
        board = [["."] * n for _ in range(n)]  # Empty board
        
        # ------------------------------------------------------------------
        # HASH SETS for O(1) safety checks
        # ------------------------------------------------------------------
        # These sets store which positions are ALREADY occupied.
        # Think of them as a "NO ENTRY" zone for new queens.
        #
        # When we place a queen at (row, col):
        #   - Add 'col' to cols set
        #   - Add 'row-col' to diag1 set
        #   - Add 'row+col' to diag2 set
        #
        # When we backtrack (remove the queen):
        #   - Remove 'col' from cols set
        #   - Remove 'row-col' from diag1 set
        #   - Remove 'row+col' from diag2 set
        # ------------------------------------------------------------------
        cols = set()      # Tracks which columns are blocked
        diag1 = set()     # Tracks which "\" diagonals are blocked (row-col)
        diag2 = set()     # Tracks which "/" diagonals are blocked (row+col)

        def backtrack(row: int):
            """
            Recursive backtracking with O(1) safety checks.
            
            The logic is similar to Approach 1, but instead of calling 
            is_safe() which scans the board, we just check our hash sets!
            """
            
            # 🧠 BASE CASE: All queens placed!
            if row == n:
                result.append(["".join(r) for r in board])
                return
            
            # 🔁 RECURSIVE CASE: Try each column
            for col in range(n):
                # ------------------------------------------------------------------
                # O(1) SAFETY CHECK using hash sets
                # ------------------------------------------------------------------
                # Instead of scanning all rows above (O(N)), we just check:
                #   1. Is 'col' in the 'cols' set? 
                #      → YES → Another queen in this column! ❌
                #   2. Is '(row-col)' in the 'diag1' set?
                #      → YES → Another queen on this "\" diagonal! ❌
                #   3. Is '(row+col)' in the 'diag2' set?
                #      → YES → Another queen on this "/" diagonal! ❌
                #
                # ALL THREE must be False for the position to be SAFE!
                #
                # It's like having a checklist:
                #   [ ] Column is free? ✓
                #   [ ] "\" diagonal is free? ✓
                #   [ ] "/" diagonal is free? ✓
                #   → All checked! Position is SAFE! ✅
                # ------------------------------------------------------------------
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue  # ❌ This position is under attack, try next column
                
                # ✅ Position is SAFE! Let's place our queen
                
                # Step 1: PLACE the queen 👑
                board[row][col] = "Q"
                
                # Step 2: UPDATE hash sets — mark this column & diagonals as blocked
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                
                # Step 3: RECURSE — move to the next row
                backtrack(row + 1)
                
                # Step 4: BACKTRACK — undo EVERYTHING we just did 🧹
                # This is CRITICAL: we must clean up ALL changes before trying
                # the next column!
                board[row][col] = "."
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
        
        # Start the recursion
        backtrack(0)
        return result

    # ==========================================================================
    # BONUS: Print a Solution Visually
    # ==========================================================================
    # This is just for fun — it prints a solution like a real chessboard!
    
    @staticmethod
    def print_solution(board: List[str]):
        """Print a single N-Queens solution in a nice format."""
        n = len(board)
        print("   " + " ".join(str(i) for i in range(n)))
        for i, row in enumerate(board):
            print(f"{i}  " + " ".join(row))
        print()


# ==============================================================================
# TESTING THE SOLUTIONS
# ==============================================================================
if __name__ == "__main__":
    sol = Solution()
    
    print("=" * 60)
    print("N-QUEENS PROBLEM - SOLUTIONS")
    print("=" * 60)
    
    for n in [4, 8]:
        print(f"\n{'=' * 60}")
        print(f"N = {n}")
        print(f"{'=' * 60}")
        
        # Test basic approach
        solutions1 = sol.solveNQueens_basic(n)
        print(f"\n📌 Approach 1 (Basic Backtracking):")
        print(f"   Number of solutions: {len(solutions1)}")
        
        # Test optimized approach
        solutions2 = sol.solveNQueens_optimized(n)
        print(f"\n📌 Approach 2 (Optimized with Hash Sets):")
        print(f"   Number of solutions: {len(solutions2)}")
        
        # Verify both approaches give same results
        assert solutions1 == solutions2, "ERROR: Approaches give different results!"
        print("   ✅ Both approaches agree on all solutions!")
        
        if n == 4:
            print(f"\n📋 All Solutions for N = 4:")
            print(f"{'-' * 40}")
            for i, solution in enumerate(solutions1, 1):
                print(f"\nSolution #{i}:")
                Solution.print_solution(solution)
    
    print(f"\n{'=' * 60}")
    print("DONE! Both solutions verified.")
    print(f"{'=' * 60}")


# ==============================================================================
# SUMMARY - KEY TAKEAWAYS
# ==============================================================================
#
# 🎯 THE PROBLEM:
#   Place N queens on N×N board so no two attack each other.
#
# 💡 THE INSIGHT:
#   Since each row must have exactly one queen, the problem is:
#   "Pick one column per row such that no two share a column or diagonal."
#
# 🔄 THE SOLUTION: BACKTRACKING
#   1. Place a queen in row 0, column 0
#   2. Move to row 1, try each safe column
#   3. If stuck (no safe column), GO BACK and change previous choice
#   4. Repeat until all queens are placed or all options exhausted
#
# 🧵 THREE RULES FOR SAFETY:
#   1. Different column:  col not in cols_set
#   2. Different "\" diagonal:  (row-col) not in diag1_set
#   3. Different "/" diagonal:  (row+col) not in diag2_set
#
# 🚀 OPTIMIZATION:
#   Use hash sets instead of scanning the board → O(N!) stays same
#   but each check goes from O(N) to O(1) — much faster!
#
# ⏱️ COMPLEXITY:
#   Time: O(N!) — N! is the upper bound
#   Space: O(N) — recursion stack depth