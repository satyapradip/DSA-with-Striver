"""
================================================================================
                    BASIC QUEUE PROBLEMS ⭐
================================================================================
Three classic beginner problems to build your queue intuition:

1. Generate Binary Numbers from 1 to N
2. First Negative Integer in Every Window of Size K
3. Reverse First K Elements of Queue

Each problem demonstrates a DIFFERENT queue technique:
  1. Queue as a "generator" (breadth-first growth)
  2. Queue to track "relevant" elements in a window
  3. Queue + Stack combo (reverse using stack)
"""

from collections import deque


# ==============================================================================
# PROBLEM 1: GENERATE BINARY NUMBERS FROM 1 TO N  ⭐
# ==============================================================================
# Given a number N, generate binary numbers from 1 to N using a queue.
#
# Example:
#   N = 5 → ["1", "10", "11", "100", "101"]
#
# LOGIC:
#   1. Start with "1" in the queue
#   2. Dequeue front, output it
#   3. Append "0" and "1" to create children: front + "0", front + "1"
#   4. Enqueue both children
#   5. Repeat N times
#
# Visual:
#   Queue: ["1"]
#   Dequeue "1" → output "1", enqueue "10", "11"
#   Queue: ["10", "11"]
#   Dequeue "10" → output "10", enqueue "100", "101"
#   Queue: ["11", "100", "101"]
#   ...
# ------------------------------------------------------------------------------

def generate_binary_numbers(n):
    """
    Generate binary numbers from 1 to N using a queue.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    result = []
    q = deque(["1"])
    
    print(f"\n   Generating binary numbers 1 to {n}:")
    print(f"   {'-'*50}")
    
    for _ in range(n):
        # Dequeue the front
        current = q.popleft()
        result.append(current)
        print(f"   Dequeued '{current}' → Output: {result}")
        
        # Enqueue children (append 0 and 1)
        q.append(current + "0")
        q.append(current + "1")
        print(f"   Enqueued '{current}0', '{current}1' → Queue: {list(q)}")
    
    return result


# ==============================================================================
# PROBLEM 2: FIRST NEGATIVE INTEGER IN EVERY WINDOW OF SIZE K  ⭐⭐
# ==============================================================================
# Given an array and window size K, find the first negative number in each
# window. If no negative exists, output 0.
#
# Example:
#   arr = [12, -1, -7, 8, -15, 30, 16, 28]
#   K = 3
#
#   Window 1: [12, -1, -7]  → first negative = -1
#   Window 2: [-1, -7, 8]   → first negative = -1
#   Window 3: [-7, 8, -15]  → first negative = -7
#   Window 4: [8, -15, 30]  → first negative = -15
#   Window 5: [-15, 30, 16] → first negative = -15
#   Window 6: [30, 16, 28]  → no negative → 0
#
# LOGIC: Use a queue to store INDICES of negative numbers. For each window,
# remove indices outside the window, then the front is the answer.
# ------------------------------------------------------------------------------

def first_negative_in_window(arr, k):
    """
    Find first negative integer in every window of size K.
    
    Time Complexity: O(n) - each element processed once
    Space Complexity: O(k) - queue stores at most k indices
    """
    n = len(arr)
    result = []
    q = deque()  # Queue to store indices of negative numbers
    
    print(f"\n   Array: {arr}")
    print(f"   Window size K = {k}")
    print(f"   {'='*60}")
    
    # Process first window separately
    for i in range(min(k, n)):
        if arr[i] < 0:
            q.append(i)
    
    # Process sliding windows
    for i in range(k, n + 1):
        # Front of queue is the first negative in current window (if exists)
        if q:
            result.append(arr[q[0]])
        else:
            result.append(0)  # No negative in window
        
        # Print current window
        window = arr[max(0, i-k):i] if i <= n else arr[max(0, i-k):n]
        print(f"   Window {list(window)} → First negative: {result[-1]}")
        
        # Remove elements that are out of the next window
        while q and q[0] <= i - k:
            q.popleft()
        
        # Add new element (if within bounds) to queue
        if i < n and arr[i] < 0:
            q.append(i)
    
    return result


# ==============================================================================
# PROBLEM 3: REVERSE FIRST K ELEMENTS OF QUEUE  ⭐⭐
# ==============================================================================
# Given a queue and number K, reverse the order of the first K elements.
#
# Example:
#   Queue: [1, 2, 3, 4, 5], K = 3
#   Result: [3, 2, 1, 4, 5]
#
# LOGIC:
#   1. Pop first K elements into a stack (this reverses them)
#   2. Pop from stack back into queue (now reversed at front)
#   3. Rotate remaining (n - k) elements to the back
# ------------------------------------------------------------------------------

def reverse_first_k(queue, k):
    """
    Reverse first K elements of a queue.
    
    Time Complexity: O(n)
    Space Complexity: O(k) for the stack
    """
    q = deque(queue)
    stack = []
    
    print(f"\n   Original Queue: {list(q)}, K = {k}")
    print(f"   {'-'*50}")
    
    # Step 1: Move first K elements to stack (reverses them)
    for _ in range(k):
        item = q.popleft()
        stack.append(item)
        print(f"   Dequeued {item} → Pushed to stack: {stack}")
    
    # Step 2: Move them back from stack to front of queue
    while stack:
        q.append(stack.pop())
    print(f"   After re-inserting: {list(q)}")
    
    # Step 3: Rotate remaining (n - k) elements to the back
    for _ in range(len(q) - k):
        q.append(q.popleft())
    
    print(f"   ✅ Final Queue: {list(q)}")
    return list(q)


# ==============================================================================
# MAIN FUNCTION
# ==============================================================================

if __name__ == "__main__":
    
    print("\n" + "█" * 60)
    print("██  BASIC QUEUE PROBLEMS")
    print("█" * 60)
    
    # ──────────────────────────────────────────────────────────────────────────
    # PROBLEM 1: Generate Binary Numbers
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 PROBLEM 1: GENERATE BINARY NUMBERS")
    print("=" * 60)
    
    binaries = generate_binary_numbers(5)
    print(f"\n   ✅ Binary numbers: {binaries}\n")
    
    # ──────────────────────────────────────────────────────────────────────────
    # PROBLEM 2: First Negative in Window
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 PROBLEM 2: FIRST NEGATIVE IN WINDOW")
    print("=" * 60)
    
    fnw = first_negative_in_window([12, -1, -7, 8, -15, 30, 16, 28], 3)
    print(f"\n   ✅ Result: {fnw}\n")
    
    # ──────────────────────────────────────────────────────────────────────────
    # PROBLEM 3: Reverse First K Elements
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 PROBLEM 3: REVERSE FIRST K ELEMENTS")
    print("=" * 60)
    
    reversed_q = reverse_first_k([1, 2, 3, 4, 5], 3)
    print(f"\n   ✅ Reversed queue: {reversed_q}\n")
    
    print("🚀 NEXT: Run 06_monotonic_queue.py to learn the interview gold!")
    print("   (Sliding Window Maximum - MONOTONIC DEQUE!)")