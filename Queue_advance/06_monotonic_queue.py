"""
================================================================================
                    MONOTONIC QUEUE - SLIDING WINDOW ⭐⭐⭐
================================================================================
A monotonic queue maintains elements in either increasing or decreasing order.
It's a DEQUE where we only keep "useful" elements.

💡 KEY INSIGHT: A monotonic queue is the QUEUE version of a monotonic stack!

We maintain a DECREASING deque:
  - When adding new element: remove ALL smaller elements from the back first
  - This keeps the deque sorted (largest at front)
  - The front always has the MAXIMUM in the current window

WHY IT WORKS:
If a bigger element comes after a smaller one, the smaller one becomes
"useless" — it will never be the maximum of any window that includes
the bigger one. So we remove it!
"""

from collections import deque


# ==============================================================================
# PROBLEM 1: SLIDING WINDOW MAXIMUM  (LeetCode 239) ⭐⭐⭐ VERY FAMOUS!
# ==============================================================================
# Given an array and window size K, find the maximum in each sliding window.
#
# Example:
#   arr = [1, 3, -1, -3, 5, 3, 6, 7], K = 3
#   Output: [3, 3, 5, 5, 6, 7]
#
#   Window 1: [1, 3, -1] → max = 3
#   Window 2: [3, -1, -3] → max = 3
#   Window 3: [-1, -3, 5] → max = 5
#   Window 4: [-3, 5, 3] → max = 5
#   Window 5: [5, 3, 6] → max = 6
#   Window 6: [3, 6, 7] → max = 7
#
# NAIVE APPROACH: For each window, scan K elements → O(n*k)
# OPTIMAL: Use monotonic deque → O(n)
# ------------------------------------------------------------------------------

def sliding_window_maximum(nums, k):
    """
    Find maximum in every sliding window of size K.
    
    LOGIC (Monotonic Decreasing Deque):
    1. Store INDICES in a deque, maintaining decreasing order of values
    2. For each new element:
       a. Remove indices outside current window (from front)
       b. Remove indices whose values are <= current value (from back)
          — they can never be the max for any future window!
       c. Add current index to the back
       d. Front of deque = index of maximum for current window
    3. Only start outputting when we have a complete window (i >= k-1)
    
    Time Complexity: O(n) - each index added/removed at most once
    Space Complexity: O(k) - deque size at most k
    """
    n = len(nums)
    result = []
    dq = deque()  # Will store INDICES, maintaining decreasing values
    
    print(f"\n   Array: {nums}")
    print(f"   Window size K = {k}")
    print(f"   ⚡ Using MONOTONIC DEQUE - O(n) solution!")
    print(f"   {'='*60}")
    
    for i in range(n):
        # Step 1: Remove indices outside current window
        # (front indices that are too old)
        while dq and dq[0] <= i - k:
            removed = dq.popleft()
            print(f"   Index {removed} (value {nums[removed]}) left the window → removed")
        
        # Step 2: Remove smaller elements from back
        # (they're useless since current element is larger AND newer)
        while dq and nums[dq[-1]] <= nums[i]:
            removed = dq.pop()
            print(f"   {nums[removed]} ≤ {nums[i]} → {nums[removed]} can never be max → removed")
        
        # Step 3: Add current index
        dq.append(i)
        print(f"   Added index {i} (value {nums[i]}) → Deque values: "
              f"{[nums[idx] for idx in dq]}")
        
        # Step 4: Record max when we have a complete window
        if i >= k - 1:
            result.append(nums[dq[0]])
            print(f"   ✅ Window ending at {i}: {nums[i-k+1:i+1]} → Max = {nums[dq[0]]}")
        
        print()
    
    return result


# ==============================================================================
# PROBLEM 2: SLIDING WINDOW MINIMUM  (Mirror Pattern) ⭐⭐⭐
# ==============================================================================
# Same as sliding window max, but find the MINIMUM in each window.
# Uses a MONOTONIC INCREASING deque (smallest at front).
#
# Example:
#   arr = [1, 3, -1, -3, 5, 3, 6, 7], K = 3
#   Output: [-1, -3, -3, -3, 3, 3]
# ------------------------------------------------------------------------------

def sliding_window_minimum(nums, k):
    """
    Find minimum in every sliding window of size K.
    Uses monotonic INCREASING deque (smallest at front).
    
    Time Complexity: O(n)
    Space Complexity: O(k)
    """
    n = len(nums)
    result = []
    dq = deque()  # Monotonic increasing: front = smallest
    
    print(f"\n   Array: {nums}, Window size K = {k}")
    print(f"   ⚡ Monotonic INCREASING deque (smallest at front)")
    print(f"   {'='*60}")
    
    for i in range(n):
        # Remove indices outside window
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        # Remove LARGER elements (they can never be minimum)
        while dq and nums[dq[-1]] >= nums[i]:
            dq.pop()
        
        dq.append(i)
        
        if i >= k - 1:
            result.append(nums[dq[0]])
            print(f"   Window {nums[i-k+1:i+1]} → Min = {nums[dq[0]]}")
    
    return result


# ==============================================================================
# PATTERN RECOGNITION: THE MONOTONIC DEQUE TEMPLATE 🧠
# ==============================================================================
"""
HOW TO SPOT MONOTONIC DEQUE PROBLEMS:
  • "Maximum/minimum in EVERY window of size K"
  • "Sliding window" + "max/min"
  
THE 4-STEP TEMPLATE:
┌─────────────────────────────────────────────────────────────┐
│  dq = deque()  # stores INDICES                             │
│  for i in range(len(nums)):                                 │
│      # 1. Remove outdated (outside window)                  │
│      while dq and dq[0] <= i - k: dq.popleft()              │
│                                                             │
│      # 2. Remove useless (compare values)                   │
│      while dq and nums[dq[-1]] <= nums[i]: dq.pop()  # max  │
│      while dq and nums[dq[-1]] >= nums[i]: dq.pop()  # min  │
│                                                             │
│      # 3. Add current                                       │
│      dq.append(i)                                           │
│                                                             │
│      # 4. Record result when window complete                │
│      if i >= k - 1: result.append(nums[dq[0]])              │
└─────────────────────────────────────────────────────────────┘

REMEMBER:
  • For MAXIMUM: remove SMALLER elements (<=) — decreasing deque
  • For MINIMUM: remove LARGER elements (>=) — increasing deque
  • Store INDICES not values! (to check if element left window)
"""


# ==============================================================================
# PROBLEM 3: SUM OF MINIMUM & MAXIMUM IN ALL SUBARRAYS OF SIZE K ⭐⭐⭐
# ==============================================================================
# Given an array and K, find the sum of (maximum + minimum) for every
# window of size K. Great exercise combining both patterns!
#
# Example:
#   arr = [2, 5, -1, 7, -3], K = 3
#   Window 1: [2, 5, -1]  → max=5, min=-1  → sum = 4
#   Window 2: [5, -1, 7]  → max=7, min=-1  → sum = 6
#   Window 3: [-1, 7, -3] → max=7, min=-3  → sum = 4
#   Total: 4 + 6 + 4 = 14
# ------------------------------------------------------------------------------

def sum_min_max_in_windows(arr, k):
    """
    Find sum of (max + min) for every window of size K.
    
    Time Complexity: O(n)
    Space Complexity: O(k)
    """
    n = len(arr)
    # Max deque (decreasing) and Min deque (increasing)
    max_dq = deque()
    min_dq = deque()
    total = 0
    
    print(f"\n   Array: {arr}, K = {k}")
    print(f"   {'='*60}")
    
    for i in range(n):
        # 1. Remove outdated for both deques
        while max_dq and max_dq[0] <= i - k:
            max_dq.popleft()
        while min_dq and min_dq[0] <= i - k:
            min_dq.popleft()
        
        # 2. Maintain monotonic deques
        while max_dq and arr[max_dq[-1]] <= arr[i]:
            max_dq.pop()
        while min_dq and arr[min_dq[-1]] >= arr[i]:
            min_dq.pop()
        
        # 3. Add current
        max_dq.append(i)
        min_dq.append(i)
        
        # 4. Record when window is complete
        if i >= k - 1:
            window_max = arr[max_dq[0]]
            window_min = arr[min_dq[0]]
            window_sum = window_max + window_min
            total += window_sum
            print(f"   Window {arr[i-k+1:i+1]} → max={window_max}, "
                  f"min={window_min} → sum={window_sum}")
    
    print(f"\n   ✅ Total sum of (max+min) for all windows: {total}")
    return total


# ==============================================================================
# MAIN FUNCTION
# ==============================================================================

if __name__ == "__main__":
    
    print("\n" + "█" * 60)
    print("██  MONOTONIC QUEUE - SLIDING WINDOW PROBLEMS")
    print("█" * 60)
    
    # ──────────────────────────────────────────────────────────────────────────
    # PROBLEM 1: Sliding Window Maximum ⭐ STAR OF THE SHOW
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 PROBLEM 1: SLIDING WINDOW MAXIMUM")
    print("=" * 60)
    print()
    print("   ⭐ THIS IS THE MOST IMPORTANT QUEUE INTERVIEW PROBLEM! ⭐")
    print("   It introduces the MONOTONIC DEQUE pattern (Striver's favorite!)")
    
    swm = sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3)
    print(f"\n   ✅ Sliding Window Maximum: {swm}\n")
    
    # ──────────────────────────────────────────────────────────────────────────
    # PROBLEM 2: Sliding Window Minimum
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 PROBLEM 2: SLIDING WINDOW MINIMUM (Mirror Pattern)")
    print("=" * 60)
    print()
    print("   Same template, just flip the comparison sign!")
    print("   For MINIMUM: remove LARGER elements instead of smaller ones")
    
    swm_min = sliding_window_minimum([1, 3, -1, -3, 5, 3, 6, 7], 3)
    print(f"\n   ✅ Result: {swm_min}\n")
    
    # ──────────────────────────────────────────────────────────────────────────
    # PATTERN TEMPLATE
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 THE 4-STEP MONOTONIC DEQUE TEMPLATE")
    print("=" * 60)
    print("""
   dq = deque()  # stores INDICES
   for i in range(len(nums)):
       # 1. Remove outdated (outside window)
       while dq and dq[0] <= i - k: dq.popleft()
       
       # 2. Remove useless (compare values)
       while dq and nums[dq[-1]] <= nums[i]: dq.pop()  # max
       while dq and nums[dq[-1]] >= nums[i]: dq.pop()  # min
       
       # 3. Add current
       dq.append(i)
       
       # 4. Record result when window complete
       if i >= k - 1: result.append(nums[dq[0]])
    """)
    
    # ──────────────────────────────────────────────────────────────────────────
    # PROBLEM 3: Sum of Min & Max
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 PROBLEM 3: SUM OF MIN & MAX IN ALL WINDOWS")
    print("=" * 60)
    print()
    print("   Combines BOTH patterns: run max-deque AND min-deque together!")
    
    total_sum = sum_min_max_in_windows([2, 5, -1, 7, -3], 3)
    print(f"\n   Final total: {total_sum}\n")
    
    print("🚀 NEXT: Run 07_bfs_rotten_oranges.py to learn the OTHER")
    print("   superpower of queues - BFS (Breadth First Search)!")