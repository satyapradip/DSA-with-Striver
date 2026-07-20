"""
================================================================================
⭐ RECURSION ON SUBSEQUENCES - COMPLETE BEGINNER'S GUIDE ⭐
================================================================================

📌 WHAT IS A SUBSEQUENCE?
   A subsequence is a sequence that can be derived from an array by selecting
   ZERO or MORE elements WITHOUT changing the order of the remaining elements.

   ✅ Key Point: Order MUST be maintained
   ✅ Key Point: Elements do NOT need to be contiguous (unlike subarrays)

   Example: arr = [3, 1, 2]
   Subsequences: [], [3], [1], [2], [3,1], [3,2], [1,2], [3,1,2]
   (Total = 2^n = 2^3 = 8 subsequences)

   🚫 NOT a subsequence: [2, 1] — because 2 comes AFTER 1 in the original array
   🚫 NOT a subsequence: [1, 3] — because 1 comes AFTER 3 in the original array

📌 SUBSEQUENCE vs SUBARRAY (Common Confusion!)
   ┌──────────────────────────────┬────────────────────────────────┐
   │        SUBSEQUENCE          │           SUBARRAY             │
   ├──────────────────────────────┼────────────────────────────────┤
   │ Can skip elements           │ Must be CONTIGUOUS             │
   │ [3, 2] from [3, 1, 2] ✅    │ [3, 2] from [3, 1, 2] ❌      │
   │ Order maintained            │ Order maintained               │
   └──────────────────────────────┴────────────────────────────────┘

📌 THE CORE IDEA: TAKE / NOT-TAKE PATTERN (Pick or Don't Pick)

   This is the MOST IMPORTANT pattern in recursion for subsequences!

   For EVERY element in the array, we have EXACTLY 2 choices:
    1️⃣ TAKE it (include in subsequence)
    2️⃣ NOT TAKE it (skip it)

   This creates a RECURSION TREE where each level represents one element,
   and each branch represents a choice.

📌 VISUAL RECURSION TREE for arr = [3, 1, 2]

                     ROOT (index=0, empty subsequence)
                    |                              |
            TAKE 3                                  NOT TAKE 3
              |                                      |
          [3] (idx=1)                              [] (idx=1)
         |        |                               |        |
    TAKE 1    NOT TAKE 1                     TAKE 1    NOT TAKE 1
      |            |                          |            |
  [3,1](idx=2)   [3](idx=2)              [1](idx=2)     [](idx=2)
   |    |        |    |                 |    |          |    |
 T 2  NT 2    T 2  NT 2             T 2  NT 2      T 2  NT 2
  |    |       |    |                |    |         |    |
[3,1,2] [3,1] [3,2] [3]           [1,2] [1]      [2]  []

  📍 LEAF NODES (where index == n) are the subsequences!
  [] [3] [1] [3,1] [2] [3,2] [1,2] [3,1,2]

================================================================================
"""

# ==============================================================================
# METHOD 1: PRINT ALL SUBSEQUENCES USING RECURSION (OPTIMAL APPROACH)
# ==============================================================================
# ⏱ Time Complexity:  O(2^n * n)  → 2^n subsequences, O(n) to print each one
# 💾 Space Complexity: O(n)        → recursion stack depth + temp list
#
# This is the MOST OPTIMAL solution for printing all subsequences.
# We cannot do better than O(2^n * n) because there are 2^n subsequences
# that each need to be printed.
# ==============================================================================

def print_subsequences(arr: list) -> None:
    """
    Prints ALL subsequences of the given array.

    Parameters:
        arr (list): The input array

    Example:
        >>> print_subsequences([3, 1, 2])
        [3, 1, 2]
        [3, 1]
        [3, 2]
        [3]
        [1, 2]
        [1]
        [2]
        []
    """

    n = len(arr)
    temp = []  # temporary list to store current subsequence being built

    def solve(index: int) -> None:
        """
        Recursive helper function.
        
        At each call, we are at 'index' in the array and we need to decide
        whether to 'take' or 'not take' arr[index] into our subsequence.

        Parameters:
            index (int): Current position in the array we're processing
        """

        # 🛑 BASE CASE: If we've processed ALL elements (index == n)
        #    This means we've made a decision (take/not-take) for EVERY element.
        #    Whatever is in 'temp' right now IS one complete subsequence!
        if index == n:
            print(temp)  # Print the subsequence
            return

        # ======================================================================
        # 🔄 RECURSIVE CASE: TWO CHOICES for every element
        # ======================================================================

        # ──────────────────────────────────────────────────────────────────────
        # CHOICE 1️⃣ : "TAKE" the current element
        # ──────────────────────────────────────────────────────────────────────
        temp.append(arr[index])   # 1. Add the element to our subsequence
        solve(index + 1)          # 2. Recurse for the next element
        temp.pop()                # 3. BACKTRACK: remove it for the next branch
        #    🧠 Why pop()? After we return from the "take" branch, we need to
        #       remove this element so that when we explore the "not-take"
        #       branch, 'temp' doesn't have this element anymore!

        # ──────────────────────────────────────────────────────────────────────
        # CHOICE 2️⃣ : "NOT TAKE" the current element
        # ──────────────────────────────────────────────────────────────────────
        solve(index + 1)          # Just recurse for the next element WITHOUT
                                  # adding arr[index] to 'temp'

        # ✅ That's it! These two lines (append + solve + pop, then solve again)
        #    are the ENTIRE magic of subsequence recursion!

    # Start the recursion from index 0
    solve(0)


# ==============================================================================
# 🧪 DRY RUN with arr = [3, 1, 2]
# ==============================================================================
#
# Let's trace through solve(0) step-by-step:
#
# ┌────────┬──────────────────────┬─────────────────────────────┐
# │ INDEX  │      ACTION          │      temp (after action)   │
# ├────────┼──────────────────────┼─────────────────────────────┤
# │   0    │ solve(0) called      │            []               │
# │   0    │ TAKE 3 → append(3)   │            [3]              │
# │   1    │ solve(1) called      │            [3]              │
# │   1    │ TAKE 1 → append(1)   │           [3, 1]            │
# │   2    │ solve(2) called      │           [3, 1]            │
# │   2    │ TAKE 2 → append(2)   │          [3, 1, 2]          │
# │   3    │ solve(3) INDEX==n 🛑 │          [3, 1, 2]          │
# │   3    │ 📍 PRINT [3, 1, 2]   │          [3, 1, 2]          │
# │   3    │ return → pop(2)      │           [3, 1]            │
# │   2    │ NOT TAKE 2 → solve(3)│           [3, 1]            │
# │   3    │ 📍 PRINT [3, 1]      │           [3, 1]            │
# │   3    │ return               │           [3, 1]            │
# │   2    │ return → pop(1)      │            [3]              │
# │   1    │ NOT TAKE 1 → solve(2)│            [3]              │
# │   2    │ TAKE 2 → append(2)   │            [3, 2]           │
# │   3    │ 📍 PRINT [3, 2]      │            [3, 2]           │
# │   3    │ return → pop(2)      │            [3]              │
# │   2    │ NOT TAKE 2 → solve(3)│            [3]              │
# │   3    │ 📍 PRINT [3]         │            [3]              │
# │   3    │ return               │            [3]              │
# │   2    │ return → pop(3)      │            []               │
# │   0    │ NOT TAKE 3 → solve(1)│            []               │
# │   1    │ TAKE 1 → append(1)   │            [1]              │
# │   2    │ TAKE 2 → append(2)   │            [1, 2]           │
# │   3    │ 📍 PRINT [1, 2]      │            [1, 2]           │
# │   3    │ return → pop(2)      │            [1]              │
# │   2    │ NOT TAKE 2 → solve(3)│            [1]              │
# │   3    │ 📍 PRINT [1]         │            [1]              │
# │   3    │ return → pop(1)      │            []               │
# │   1    │ NOT TAKE 1 → solve(2)│            []               │
# │   2    │ TAKE 2 → append(2)   │            [2]              │
# │   3    │ 📍 PRINT [2]         │            [2]              │
# │   3    │ return → pop(2)      │            []               │
# │   2    │ NOT TAKE 2 → solve(3)│            []               │
# │   3    │ 📍 PRINT []          │            []               │
# │   3    │ return               │            []               │
# └────────┴──────────────────────┴─────────────────────────────┘
#
# OUTPUT:
#   [3, 1, 2]
#   [3, 1]
#   [3, 2]
#   [3]
#   [1, 2]
#   [1]
#   [2]
#   []

# ==============================================================================
# 🎯 KEY TAKEAWAYS
# ==============================================================================
#
# 1️⃣ The PATTERN to remember:
#       temp.append(arr[index])
#       solve(index + 1)        # Take branch
#       temp.pop()
#       solve(index + 1)        # Not-take branch
#
# 2️⃣ Total subsequences = 2^n (each element has 2 choices)
#
# 3️⃣ Time Complexity: O(2^n * n)
#    - 2^n subsequences are generated
#    - Each subsequence takes O(n) time to print
#
# 4️⃣ Space Complexity: O(n)
#    - Recursion stack goes n levels deep
#    - 'temp' list holds at most n elements
#
# 5️⃣ This is the OPTIMAL solution — we cannot do better because we MUST
#    generate all 2^n subsequences and print each one!

# ==============================================================================
# 🔗 RELATED PROBLEMS (Building on this concept)
# ==============================================================================
# Once you master this "take/not-take" pattern, you can solve:
#   • Subsets (LeetCode 78)     → same as subsequences!
#   • Subset Sum (GFG)          → sum of each subsequence
#   • Subset Sum II (LeetCode 90) → unique subsets with duplicates
#   • Combination Sum (LeetCode 39) → subsequences with specific sum
#   • Permutations (LeetCode 46)   → same pattern but reordering allowed

# ==============================================================================
# 🏃‍♂️ RUN THE CODE
# ==============================================================================
if __name__ == "__main__":
    print("=" * 60)
    print("PRINTING ALL SUBSEQUENCES OF [3, 1, 2]")
    print("=" * 60)
    print_subsequences([3, 1, 2])
    print("=" * 60)
    print(f"Total: 2^3 = {2**3} subsequences ✅")
    print()

    print("=" * 60)
    print("PRINTING ALL SUBSEQUENCES OF [1, 2]")
    print("=" * 60)
    print_subsequences([1, 2])
    print("=" * 60)
    print(f"Total: 2^2 = {2**2} subsequences ✅")
    print()

    print("=" * 60)
    print("PRINTING ALL SUBSEQUENCES OF ['a', 'b', 'c']")
    print("=" * 60)
    print_subsequences(['a', 'b', 'c'])
    print("=" * 60)
    print(f"Total: 2^3 = {2**3} subsequences ✅")