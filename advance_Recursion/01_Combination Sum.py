"""
================================================================================
PROBLEM: Combination Sum (LeetCode 39)
================================================================================

QUESTION:
Given an array of DISTINCT integers called 'candidates' and a 'target' integer,
find ALL UNIQUE combinations of candidates where the chosen numbers sum to target.

IMPORTANT RULES:
1. You may use the same number from candidates an UNLIMITED number of times.
2. The answer must NOT contain duplicate combinations (even if order is different).
3. All numbers (including target) are positive integers.

Example 1:
    candidates = [2, 3, 6, 7], target = 7
    Output: [[2, 2, 3], [7]]
    Explanation: 2+2+3 = 7, and 7 = 7

Example 2:
    candidates = [2, 3, 5], target = 8
    Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

================================================================================
UNDERSTANDING THE PROBLEM (Think Like This):
================================================================================

Imagine you have a basket of numbers: [2, 3, 6, 7]
You need to pick numbers that add up to 7.
You can pick the SAME number multiple times (unlimited supply!).

Think of it like this:
- You're at a vending machine with unlimited stock of each item.
- Each item has a price (the number).
- You need to spend EXACTLY 'target' amount of money.
- You can buy multiple quantities of the same item.
- Find ALL possible combinations of items you can buy.

================================================================================
RECURSION APPROACH - THE "PICK/NOT PICK" PATTERN
================================================================================

The key insight: At EVERY step, for each number, we have TWO choices:
    1. PICK the number (add it to our current combination)
    2. NOT PICK the number (skip it and move to the next number)

But wait! Since we can use a number unlimited times:
    - If we PICK it, we DON'T move to the next index (we can pick it AGAIN!)
    - If we DON'T pick it, we MOVE to the next index (we're done with this number)

This creates a TREE-like structure in our recursion.

Let's trace through with candidates = [2, 3, 6, 7], target = 7:

                    Start: idx=0, sum=0, combo[]
                   /              \\
          PICK 2                  DON'T PICK 2
          idx=0, sum=2,           idx=1, sum=0,
          combo=[2]               combo=[]
         /         \\              /          \\
  PICK 2        DON'T 2      PICK 3       DON'T 3
  sum=4,        idx=1,       sum=3,        idx=2,
  [2,2]         [2]          [3]           []
    /  \\         /  \\         /  \\          /  \\
 PICK   DNT   PICK  DNT   PICK  DNT     PICK   DNT
 2      2      3     3     3     3       6      6

... and so on until we either reach target sum (valid) or exceed it (invalid).

================================================================================
VISUALIZING THE RECURSION TREE (Full Example)
================================================================================

candidates = [2, 3, 5], target = 8

Let's trace ONLY the valid paths that sum to 8:

                         f(0, 0, [])
                        /         \
                  PICK 2          DON'T PICK 2
                  /                   \
            f(0, 2, [2])            f(1, 0, [])
             /        \               /        \
        PICK 2     DON'T 2        PICK 3     DON'T 3
          /            \            /             \
    f(0,4,[2,2])   f(1,2,[2])  f(1,3,[3])    f(2,0,[])
      /    \         /    \       /    \         /     \
    ...   ...    PICK  DON'T  PICK  DON'T    PICK   DON'T
                  3      3     3      3       5       5
                  |      |      |      |      |        |
                f(1,  f(2,  f(1,  f(2,  f(2,  f(3,
                5,    2,    6,    3,    5,    0,
                [2,3])[2]) [3,3])[3]) [5])  [])

                Exactly!                Sum=5+3?    Sum=5+5?   Sum=5+6?
                Sum=8!   Sum=2+3!=8             No            No          No
                [2,3,3]  so continue           (exceeds)
                is valid!  ...

The valid combinations we find: [2,2,2,2], [2,3,3], [3,5]

================================================================================
TIME & SPACE COMPLEXITY
================================================================================

Time Complexity: O(2^(target/min(candidate))) - In the worst case, the tree 
    can be very deep because we can pick the smallest element many times.
Space Complexity: O(target/min(candidate)) - For the recursion stack depth.
"""

from typing import List

class Solution:
    """
    Solution class for Combination Sum problem.
    We'll implement two approaches to help you understand recursion better.
    """

    # ==========================================================================
    # APPROACH 1: Basic Recursion (Pick/Not Pick) - EASIEST TO UNDERSTAND
    # ==========================================================================
    # THINKING PROCESS:
    # 1. We go through each candidate one by one (using index 'idx')
    # 2. At each candidate, we have two choices:
    #    a) PICK it: Add to our combo, DON'T move index (can pick again)
    #    b) NOT PICK it: Don't add, MOVE to next index
    # 3. Base case: When we've gone through all candidates OR sum exceeds target
    # 4. If sum == target, we found a valid combination!

    def combinationSum_approach1(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Approach 1: For loop + recursion (most intuitive)
        """

        result = []      # This will store ALL our valid combinations
        current = []     # This stores the combination we're BUILDING right now
        n = len(candidates)

        # ------------------------------------------------------------------
        # RECURSIVE FUNCTION
        # ------------------------------------------------------------------
        # 'idx' = which candidate we are considering right now
        # 'current' = the combination we have built so far
        # 'current_sum' = sum of numbers in 'current'
        # ------------------------------------------------------------------
        def solve(idx: int, current: List[int], current_sum: int):
            """
            🧠 BASE CASES (When does the recursion STOP?):
            
            Think of base cases like the emergency brakes of a roller coaster.
            They stop the ride (recursion) when something goes wrong or 
            when we've completed our goal.
            """
            
            # CASE 1: We FOUND a valid combination!
            # If current_sum equals target, our current combo is CORRECT.
            # We add a COPY of it to result (not the actual list, because 
            # we'll modify 'current' later).
            if current_sum == target:
                # IMPORTANT: We use current[:] or list(current) to make a COPY
                # If we just appended 'current', it would change later!
                result.append(current[:])  
                return  # 🛑 STOP recursing - we found what we needed
            
            # CASE 2: We EXCEEDED the target or ran out of candidates!
            # If sum > target, adding more numbers will only make it worse.
            # If idx >= n, we've checked all candidates.
            # In both cases, there's no point continuing. 🛑 STOP!
            if current_sum > target or idx >= n:
                return
            
            # ------------------------------------------------------------------
            # RECURSIVE CASE (The interesting part!)
            # ------------------------------------------------------------------
            # 
            # 🔁 RECURSIVE CALL 1: PICK the current candidate
            #
            # What happens when we PICK a number?
            # 1. We ADD it to our current combination (current.append(candidates[idx]))
            # 2. We ADD its value to current_sum
            # 3. We do NOT increase idx (because we can PICK it again!)
            # 4. We call solve() again with these updated values
            #
            # Think of it like: "I'll take this number, and now let's see 
            # what happens next..."
            
            # Step 1: Add the candidate to our current combo
            current.append(candidates[idx])
            
            # Step 2: Recursively explore with this number picked
            # Notice: idx stays the SAME because we can pick this number again!
            solve(idx, current, current_sum + candidates[idx])
            
            # ⚠️ IMPORTANT BACKTRACKING STEP!
            # After we come back from the recursive call, we REMOVE the number
            # we just added. This is called BACKTRACKING.
            # 
            # Why? Because 'current' is a list we're reusing. When we return
            # from recursion, we need to UNDO the change we made so that
            # 'current' is back to how it was before we picked this number.
            # This allows us to try the NOT PICK option cleanly.
            current.pop()  # 🧹 Backtrack: Remove the last added element
            
            # ------------------------------------------------------------------
            # 🔁 RECURSIVE CALL 2: NOT PICK the current candidate (skip it)
            #
            # If we decide NOT to pick this number:
            # 1. We DON'T add it to current
            # 2. We DON'T change the sum
            # 3. We INCREASE idx by 1 (move to next candidate)
            # 4. We call solve() with next index
            #
            # Think of it like: "I don't want this number, let me check the next one."
            # ------------------------------------------------------------------
            solve(idx + 1, current, current_sum)

        # Start the recursion from index 0, empty combo, sum = 0
        solve(0, [], 0)
        return result


    # ==========================================================================
    # APPROACH 2: For Loop inside Recursion (More Optimized)
    # ==========================================================================
    # THINKING PROCESS:
    # Instead of pick/not-pick for EACH element, we think:
    # "At each position in our combination, which candidate should I place?"
    # We use a FOR LOOP to try placing EACH candidate starting from current index.
    #
    # This is more efficient because it naturally avoids exploring unnecessary paths.
    
    def combinationSum_approach2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Approach 2: For-loop recursion (more efficient, common pattern)
        """
        result = []
        current = []
        n = len(candidates)
        
        # Sort candidates (helps with optimization, not required for correctness)
        candidates.sort()
        
        def solve(start_idx: int, current: List[int], remaining: int):
            """
            APPROACH 2 EXPLANATION:
            Instead of asking "pick or not pick?" we ask:
            "Which candidate should I put at this position in my combination?"
            
            'start_idx' = the index from which we can start picking candidates
            'remaining' = how much more we need to reach target
                          (instead of current_sum, we use remaining = target - current_sum)
            
            This is like: "I have 'remaining' amount left to spend. 
                          Which items can I buy?"
            """
            
            # 🧠 BASE CASE: We reached the target exactly!
            if remaining == 0:
                result.append(current[:])  # Add COPY of current combo
                return
            
            # 🧠 BASE CASE: We overshot (remaining < 0)
            # No point continuing
            if remaining < 0:
                return
            
            # ------------------------------------------------------------------
            # RECURSIVE CASE: Try each possible candidate
            # ------------------------------------------------------------------
            # For each position in our combination, we try placing EACH candidate
            # that is >= the last candidate we used.
            #
            # Why start from start_idx? To maintain ORDER and avoid duplicates!
            # If we used candidates[0] already, we don't want to later pick 
            # candidates[0] again at a DIFFERENT position (would create duplicates).
            # ------------------------------------------------------------------
            for i in range(start_idx, n):
                # Optimization: If this candidate is > remaining, no need to check
                # further because array is sorted and later elements are even larger!
                if candidates[i] > remaining:
                    break  # 🛑 Stop the loop, remaining candidates are too big
                
                # Pick this candidate
                current.append(candidates[i])
                
                # 🔁 RECURSIVE CALL
                # We pass 'i' (not i+1) because we can reuse the SAME element
                # multiple times (unlimited supply!)
                solve(i, current, remaining - candidates[i])
                
                # 🧹 BACKTRACK: Remove the candidate we just tried
                # This allows us to try the NEXT candidate in the next loop iteration
                current.pop()
        
        solve(0, [], target)
        return result


# ==============================================================================
# EASIEST WAY TO REMEMBER - MENTAL MODEL
# ==============================================================================
#
# 🎯 RECURSION MENTAL MODEL:
# Imagine you're at a buffet with unlimited food items.
# You have a plate (current combo) and a target amount of appetite (target).
#
# At each food item, you ask:
#   "Should I take this (PICK) or skip it (NOT PICK)?"
#
# If you take it:
#   - You put it on your plate
#   - Your remaining appetite decreases
#   - You can take MORE of the same item (stay at same index)
#
# If you skip it:
#   - You leave it behind
#   - Your appetite stays the same
#   - You move to the next item (increase index)
#
# When your appetite reaches EXACTLY 0 → You found a valid meal! 🎉
# When your appetite goes negative → Too much food! Skip this path. ❌
# When you've seen all items → No more options. Stop. 🛑
#
# ⚙️ BACKTRACKING MENTAL MODEL:
# When you try an item and it doesn't work out,
# you REMOVE it from your plate before trying something else.
# Like undoing a move in chess - you take back your last move
# to try a different strategy.
#
# ==============================================================================
# Let's TRACE through an example with Approach 1:
# ==============================================================================
# candidates = [2, 3], target = 5
#
# Call stack (showing pick/not-pick decisions):
#
# solve(0, [], 0)
# ├── PICK 2 → solve(0, [2], 2)
# │   ├── PICK 2 → solve(0, [2,2], 4)
# │   │   ├── PICK 2 → solve(0, [2,2,2], 6) → sum>target ❌ return
# │   │   └── NOT PICK → solve(1, [2,2], 4)
# │   │       ├── PICK 3 → solve(1, [2,2,3], 7) → sum>target ❌ return
# │   │       └── NOT PICK → solve(2, [2,2], 4) → idx>=n ❌ return
# │   └── NOT PICK → solve(1, [2], 2)
# │       ├── PICK 3 → solve(1, [2,3], 5) → sum==target ✅ FOUND! [2,3]
# │       └── NOT PICK → solve(2, [2], 2) → idx>=n ❌ return
# └── NOT PICK → solve(1, [], 0)
#     ├── PICK 3 → solve(1, [3], 3)
#     │   ├── PICK 3 → solve(1, [3,3], 6) → sum>target ❌ return
#     │   └── NOT PICK → solve(2, [3], 3) → idx>=n ❌ return
#     └── NOT PICK → solve(2, [], 0) → idx>=n ❌ return
#
# Result: [[2, 3]]
# ==============================================================================


# ==============================================================================
# TESTING THE SOLUTION
# ==============================================================================
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    candidates1 = [2, 3, 6, 7]
    target1 = 7
    result1 = sol.combinationSum_approach1(candidates1, target1)
    print(f"Approach 1 - candidates={candidates1}, target={target1}")
    print(f"Result: {result1}")
    print(f"Expected: [[2, 2, 3], [7]]")
    print()
    
    # Test Case 2
    candidates2 = [2, 3, 5]
    target2 = 8
    result2 = sol.combinationSum_approach1(candidates2, target2)
    print(f"Approach 1 - candidates={candidates2}, target={target2}")
    print(f"Result: {result2}")
    print(f"Expected: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]")
    print()
    
    # Test with Approach 2
    result3 = sol.combinationSum_approach2(candidates1, target1)
    print(f"Approach 2 - candidates={candidates1}, target={target1}")
    print(f"Result: {result3}")
    print(f"Expected: [[2, 2, 3], [7]]")
    print()
    
    # Test Case 3: Edge case
    candidates3 = [1]
    target3 = 2
    result4 = sol.combinationSum_approach1(candidates3, target3)
    print(f"Approach 1 - candidates={candidates3}, target={target3}")
    print(f"Result: {result4}")
    print(f"Expected: [[1, 1]]")