"""
================================================================================
🎯 PRINT ALL SUBSEQUENCES WITH SUM = K - COMPLETE BEGINNER'S GUIDE 🎯
================================================================================

📌 QUICK RECAP: What are Subsequences?
   From the previous file, we learned:
   - A subsequence is formed by selecting ZERO or MORE elements
   - Order MUST be maintained
   - Each element has 2 choices: TAKE or NOT TAKE
   - Total subsequences = 2^n

📌 WHAT'S NEW IN THIS PROBLEM?
   Instead of printing ALL subsequences, we only print those
   whose elements ADD UP to a given target sum K.

   Example: arr = [1, 2, 1], K = 2
   
   All subsequences:            Valid (sum == 2)?
   []          sum=0 ❌
   [1]         sum=1 ❌
   [2]         sum=2 ✅  ← PRINT THIS
   [1]         sum=1 ❌
   [1, 2]      sum=3 ❌
   [1, 1]      sum=2 ✅  ← PRINT THIS
   [2, 1]      sum=3 ❌
   [1, 2, 1]   sum=4 ❌

   Output: [2], [1, 1]

📌 HOW IS THIS DIFFERENT FROM THE PREVIOUS PROBLEM?
   
   ┌────────────────────────────────────┬────────────────────────────────────┐
   │   PRINT ALL SUBSEQUENCES           │   PRINT SUBSEQUENCES WITH SUM K   │
   ├────────────────────────────────────┼────────────────────────────────────┤
   │   Print EVERYTHING                 │   Print ONLY when sum == K        │
   │   No extra check needed            │   Need to track running sum       │
   │   Just print at base case          │   Print at base case IF sum == K  │
   └────────────────────────────────────┴────────────────────────────────────┘

📌 THE CORE IDEA
   We use the EXACT SAME "take/not-take" recursion pattern.
   The ONLY addition is:
    1️⃣ Pass a `current_sum` parameter to the recursive function
    2️⃣ When we TAKE an element → add it to current_sum
    3️⃣ When we NOT TAKE → current_sum stays the same
    4️⃣ At base case (index == n), check if current_sum == K

📌 VISUAL RECURSION TREE for arr = [1, 2, 1], K = 2

                    ROOT (index=0, sum=0, temp=[])
                   |                              |
           TAKE 1 (sum=1)                    NOT TAKE 1 (sum=0)
              |                                      |
           [1] (idx=1, sum=1)                    [] (idx=1, sum=0)
          |            |                        |            |
    TAKE 2         NOT TAKE 2              TAKE 2         NOT TAKE 2
    sum=3          sum=1                   sum=2          sum=0
      |              |                      |              |
   [1,2](idx=2)   [1](idx=2)            [2](idx=2)     [](idx=2)
   |    |         |    |                |    |          |    |
  T 1 NT 1      T 1 NT 1             T 1 NT 1       T 1 NT 1
  s4  s3       s2  s1               s3  s2         s1  s0
   |    |       |    |               |    |          |    |
[1,2,1][1,2] [1,1][1]            [2,1][2]       [1]  []
 sum=4 sum=3 sum=2 sum=1        sum=3 sum=2     sum=1 sum=0
  ❌   ❌   ✅🎯  ❌            ❌   ✅🎯       ❌   ❌

  🎯 Output: [1, 1] and [2]

================================================================================
"""

# ==============================================================================
# METHOD: PRINT ALL SUBSEQUENCES WITH SUM = K (OPTIMAL APPROACH)
# ==============================================================================
# ⏱ Time Complexity:  O(2^n)     → We visit 2^n nodes in recursion tree
# 💾 Space Complexity: O(n)       → Recursion stack depth + temp list
#
# Why is this OPTIMAL? We still need to explore all 2^n possibilities
# because any subsequence COULD sum to K. There's no shortcut.
# ==============================================================================

def print_subsequences_with_sum_k(arr: list, K: int) -> None:
    """
    Prints all subsequences whose elements sum up to K.

    Parameters:
        arr (list): The input array
        K (int): The target sum

    Example:
        >>> print_subsequences_with_sum_k([1, 2, 1], 2)
        [1, 1]
        [2]
    """

    n = len(arr)
    temp = []       # temporary list to store the current subsequence being built

    def solve(index: int, current_sum: int) -> None:
        """
        Recursive helper function.
        
        At each call, we're at position 'index' in the array and we've
        already built up 'current_sum' from elements we've taken so far.

        Parameters:
            index (int): Current position in the array
            current_sum (int): Sum of elements we have taken so far
        """

        # 🛑 BASE CASE: If we've processed ALL elements
        if index == n:
            # 🎯 ONLY PRINT if the sum of this subsequence equals K!
            if current_sum == K:
                print(temp)
            return

        # ======================================================================
        # 🔄 RECURSIVE CASE: TWO CHOICES for every element
        # ======================================================================

        # ──────────────────────────────────────────────────────────────────────
        # CHOICE 1️⃣ : "TAKE" the current element
        # ──────────────────────────────────────────────────────────────────────
        temp.append(arr[index])         # 1. Add element to subsequence
        solve(index + 1, current_sum + arr[index])  # 2. Recurse with UPDATED sum
        temp.pop()                      # 3. BACKTRACK: remove element

        # ──────────────────────────────────────────────────────────────────────
        # CHOICE 2️⃣ : "NOT TAKE" the current element
        # ──────────────────────────────────────────────────────────────────────
        solve(index + 1, current_sum)   # Recurse WITHOUT adding element
        #    🧠 Notice: current_sum stays the SAME here because we didn't
        #       take the element!

    # Start from index 0 with sum = 0 (empty subsequence)
    solve(0, 0)


# ==============================================================================
# 🧪 DRY RUN with arr = [1, 2, 1], K = 2
# ==============================================================================
#
# Let's trace solve(0, 0) step-by-step:
#
# ┌───────┬────────────────────────────┬──────────┬────────────┬──────────┐
# │ INDEX │          ACTION            │  temp    │ current_sum│  PRINT?  │
# ├───────┼────────────────────────────┼──────────┼────────────┼──────────┤
# │   0   │ solve(0, 0) called        │   []     │     0      │          │
# │   0   │ TAKE 1 → append, recurse   │  [1]     │     1      │          │
# │   1   │ solve(1, 1) called        │  [1]     │     1      │          │
# │   1   │ TAKE 2 → append, recurse   │ [1,2]    │     3      │          │
# │   2   │ solve(2, 3) called        │ [1,2]    │     3      │          │
# │   2   │ TAKE 1 → append, recurse   │[1,2,1]   │     4      │          │
# │   3   │ BASE CASE! sum(4) != 2    │[1,2,1]   │     4      │   ❌     │
# │   3   │ return → pop              │ [1,2]    │     3      │          │
# │   2   │ NOT TAKE 1 → recurse      │ [1,2]    │     3      │          │
# │   3   │ BASE CASE! sum(3) != 2    │ [1,2]    │     3      │   ❌     │
# │   3   │ return                    │ [1,2]    │     3      │          │
# │   2   │ return → pop              │  [1]     │     1      │          │
# │   1   │ NOT TAKE 2 → recurse      │  [1]     │     1      │          │
# │   2   │ solve(2, 1) called        │  [1]     │     1      │          │
# │   2   │ TAKE 1 → append, recurse   │ [1,1]    │     2      │          │
# │   3   │ BASE CASE! sum(2) == 2 🎯 │ [1,1]    │     2      │ ✅ PRINT │
# │   3   │ return → pop              │  [1]     │     1      │          │
# │   2   │ NOT TAKE 1 → recurse      │  [1]     │     1      │          │
# │   3   │ BASE CASE! sum(1) != 2    │  [1]     │     1      │   ❌     │
# │   3   │ return                    │  [1]     │     1      │          │
# │   2   │ return → pop              │   []     │     0      │          │
# │   0   │ NOT TAKE 1 → recurse      │   []     │     0      │          │
# │   1   │ solve(1, 0) called        │   []     │     0      │          │
# │   1   │ TAKE 2 → append, recurse   │  [2]     │     2      │          │
# │   2   │ solve(2, 2) called        │  [2]     │     2      │          │
# │   2   │ TAKE 1 → append, recurse   │ [2,1]    │     3      │          │
# │   3   │ BASE CASE! sum(3) != 2    │ [2,1]    │     3      │   ❌     │
# │   3   │ return → pop              │  [2]     │     2      │          │
# │   2   │ NOT TAKE 1 → recurse      │  [2]     │     2      │          │
# │   3   │ BASE CASE! sum(2) == 2 🎯 │  [2]     │     2      │ ✅ PRINT │
# │   3   │ return                    │  [2]     │     2      │          │
# │   2   │ return → pop              │   []     │     0      │          │
# │   1   │ NOT TAKE 2 → recurse      │   []     │     0      │          │
# │   2   │ solve(2, 0) called        │   []     │     0      │          │
# │   2   │ TAKE 1 → append, recurse   │  [1]     │     1      │          │
# │   3   │ BASE CASE! sum(1) != 2    │  [1]     │     1      │   ❌     │
# │   3   │ return → pop              │   []     │     0      │          │
# │   2   │ NOT TAKE 1 → recurse      │   []     │     0      │          │
# │   3   │ BASE CASE! sum(0) != 2    │   []     │     0      │   ❌     │
# │   3   │ return                    │   []     │     0      │          │
# └───────┴────────────────────────────┴──────────┴────────────┴──────────┘
#
# OUTPUT:
#   [1, 1]
#   [2]


# ==============================================================================
# ✨ VISUAL COMPARISON: Before vs After (for sum K)
# ==============================================================================
#
# The ONLY difference from printing ALL subsequences is:
#
#   # BEFORE (print all subsequences):
#   if index == n:
#       print(temp)               ← prints EVERYTHING
#
#   # AFTER (print subsequences with sum K):
#   if index == n:
#       if current_sum == K:      ← ADD THIS CHECK!
#           print(temp)
#
# That's it! Just one extra if-condition. 🎉


# ==============================================================================
# 📊 TIME & SPACE COMPLEXITY DEEP DIVE
# ==============================================================================
#
# ⏱ TIME COMPLEXITY: O(2^n)
#   - Each of the n elements has 2 choices (take/not-take)
#   - Total recursive calls = 2^(n+1) - 1 ≈ 2^n
#   - This is OPTIMAL because we MUST check every subsequence
#     (any of them could sum to K - we can't skip any)
#
# 💾 SPACE COMPLEXITY: O(n)
#   - Recursion stack: goes n levels deep → O(n)
#   - temp list: stores at most n elements → O(n)
#   - No extra space used otherwise
#
# ❓ Why can't we optimize this further?
#   - Unlike "is there ANY subsequence with sum K?" (which can be optimized),
#     this problem asks to PRINT ALL of them
#   - There could be up to 2^n subsequences with sum K in worst case
#   - So we MUST explore all possibilities


# ==============================================================================
# 💡 COMMON BEGINNER MISTAKES & HOW TO AVOID THEM
# ==============================================================================
#
# MISTAKE 1️⃣: Changing current_sum globally (like a mutable variable)
#    ❌ WRONG:
#       current_sum += arr[index]   # This changes current_sum permanently!
#       solve(index + 1, current_sum)
#       solve(index + 1, current_sum)  # BUG! current_sum still has the value!
#
#    ✅ CORRECT:
#       solve(index + 1, current_sum + arr[index])  # Pass NEW value, DON'T modify
#       solve(index + 1, current_sum)               # Original value unchanged!
#
#    🧠 Python passes integers by value. So current_sum + arr[index] creates
#       a NEW number. The original current_sum is NOT affected. This is why
#       we can safely call solve() twice without needing to "backtrack" the sum!
#
# MISTAKE 2️⃣: Forgetting to backtrack temp
#    ❌ WRONG:
#       temp.append(arr[index])
#       solve(index + 1, current_sum + arr[index])
#       # forgot temp.pop() !
#       solve(index + 1, current_sum)  # temp still has arr[index]! ❌
#
#    ✅ CORRECT:
#       temp.append(arr[index])
#       solve(index + 1, current_sum + arr[index])
#       temp.pop()                    # MUST remove before not-take branch
#       solve(index + 1, current_sum)
#
# MISTAKE 3️⃣: Confusing "sum K" condition placement
#    ❌ WRONG: (checking in middle of recursion)
#       if current_sum == K:
#           print(temp)    # This prints PARTIAL subsequences too early!
#
#    ✅ CORRECT: (check only at base case)
#       if index == n:                    # Only when FULLY decided
#           if current_sum == K:          # Check if complete subsequence sums to K
#               print(temp)


# ==============================================================================
# 🏋️ PRACTICE YOURSELF: TRACE THESE EXAMPLES
# ==============================================================================
#
# Try tracing the recursion tree for these inputs:
#
# Example 1: arr = [1, 2, 3], K = 3
#   Expected output: [1, 2], [3]
#
# Example 2: arr = [1, 1, 1], K = 2
#   Expected output: [1, 1], [1, 1], [1, 1]
#   (three different ways to pick two 1's!)
#
# Example 3: arr = [5], K = 10
#   Expected output: (nothing)
#   Because 5 != 10, and [] sums to 0 != 10


# ==============================================================================
# 🎯 KEY TAKEAWAYS
# ==============================================================================
#
# 1️⃣ This is a DIRECT extension of the "print all subsequences" problem
#     → Same take/not-take pattern
#     → Same backtracking with pop()
#     → Just added: track sum + check at base case
#
# 2️⃣ The CLEVER pattern to remember:
#       temp.append(arr[index])
#       solve(index + 1, current_sum + arr[index])  # Take: update sum
#       temp.pop()
#       solve(index + 1, current_sum)               # Not-take: sum unchanged
#
# 3️⃣ Why we DON'T need to "backtrack" the sum:
#     → sum is passed by VALUE (integer is immutable in Python)
#     → Each recursive call gets its OWN copy
#     → Unlike temp (list) which is passed by REFERENCE and needs pop()
#
# 4️⃣ Problems you can now solve with this pattern:
#     → Subset Sum (GFG) - check if ANY subset has sum K
#     → Combination Sum (LeetCode 39) - same but can reuse elements
#     → Subset Sum II (LeetCode 90) - unique subsets with duplicates
#     → Partition Equal Subset Sum (LeetCode 416) - can we split into 2 halves?
#     → Target Sum (LeetCode 494) - assign + or - to reach target

# ==============================================================================
# 🏃‍♂️ RUN THE CODE
# ==============================================================================
if __name__ == "__main__":
    print("=" * 60)
    print("PRINT SUBSEQUENCES WITH SUM K = 2")
    print("arr = [1, 2, 1], K = 2")
    print("=" * 60)
    print_subsequences_with_sum_k([1, 2, 1], 2)
    print("=" * 60)
    print()

    print("=" * 60)
    print("PRINT SUBSEQUENCES WITH SUM K = 3")
    print("arr = [1, 2, 3], K = 3")
    print("=" * 60)
    print_subsequences_with_sum_k([1, 2, 3], 3)
    print("=" * 60)
    print()

    print("=" * 60)
    print("PRINT SUBSEQUENCES WITH SUM K = 0")
    print("arr = [1, 2], K = 0")
    print("=" * 60)
    print_subsequences_with_sum_k([1, 2], 0)
    print("=" * 60)
    print("(Only empty subsequence [] sums to 0)")