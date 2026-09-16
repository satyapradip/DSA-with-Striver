"""
================================================================================
                     MONOTONIC STACK - THE INTERVIEW GOLD ⭐⭐⭐
================================================================================
A monotonic stack maintains elements in either increasing or decreasing order.
It's the STACK version of the monotonic queue!

💡 KEY INSIGHT: A monotonic stack is the STACK version of a monotonic deque!

When do we use it?
  • "Next greater/smaller element"
  • "Previous greater/smaller element"
  • "Number of days until price goes up"
  • Any problem about finding the nearest element bigger/smaller than me

We maintain a DECREASING stack (for "next GREATER" problems):
  - When a NEW bigger element arrives: pop all smaller elements from the top
  - The new element is the "next greater" for all those popped elements!
  - What's left in the stack: elements waiting for a bigger element

WHY IT WORKS:
If a bigger element comes AFTER a smaller one, the bigger element is the
"next greater" answer for the smaller one. Stack stores elements WAITING
for their greater element, and the new big element satisfies them all.
"""
# ==============================================================================
# PROBLEM 1: NEXT GREATER ELEMENT  (LeetCode 496) ⭐⭐⭐ VERY FAMOUS!
# ==============================================================================
# Given an array, find the next greater element for each element.
# The next greater element is the FIRST GREATER element to the right.
# If no greater element exists, return -1.
#
# Example:
#   arr = [4, 5, 2, 25]
#   Output: [5, 25, 25, -1]
#
#   - Next greater for 4  (index 0) = 5
#   - Next greater for 5  (index 1) = 25
#   - Next greater for 2  (index 2) = 25
#   - Next greater for 25 (index 3) = -1 (nothing greater to the right)
#
# NAIVE: For each element scan to the right → O(n²)
# OPTIMAL: Monotonic stack → O(n)
# ------------------------------------------------------------------------------

def next_greater_element(arr):
    """
    Find next greater element for each element using a stack.

    LOGIC (Monotonic Decreasing Stack):
    1. Iterate left → right
    2. While current element > element at stack's top:
       - Pop that index from stack
       - Current element is the "next greater" for the popped index!
    3. Push current index onto the stack
    4. Elements still in stack at the end have no greater element → -1

    Time Complexity: O(n) - each element pushed/popped at most once
    Space Complexity: O(n)
    """
    n = len(arr)
    result = [-1] * n
    stack = []  # Stores indices of elements WAITING for their next greater

    print(f"\n   Array: {arr}")
    print(f"   ⚡ Using MONOTONIC STACK - O(n) solution!")
    print(f"   {'='*60}")

    for i in range(n):
        print(f"\n   Processing arr[{i}] = {arr[i]}")

        # Pop all smaller elements — current is their next greater!
        while stack and arr[i] > arr[stack[-1]]:
            popped_idx = stack.pop()
            result[popped_idx] = arr[i]
            print(f"   → {arr[popped_idx]}'s next greater = {arr[i]} ✅")

        stack.append(i)
        print(f"   Stack (waiting indices): {stack} → "
              f"waiting values: {[arr[idx] for idx in stack]}")

    # Elements left in stack: no next greater → already -1
    for idx in stack:
        print(f"   → {arr[idx]} has no next greater → -1")

    print(f"\n   ✅ Result: {result}")
    return result
# ==============================================================================
# PROBLEM 2: NEXT GREATER ELEMENT II - CIRCULAR  (LeetCode 503) ⭐⭐⭐
# ==============================================================================
# Same as NGE but the array is CIRCULAR: after the last element comes
# the first element again.
#
# Example:
#   arr = [1, 2, 1]
#   Output: [2, -1, 2]
#   - Next greater for arr[0] = 1 is 2
#   - Next greater for arr[1] = 2 is -1 (nothing greater anywhere)
#   - Next greater for arr[2] = 1 is 2 (wraps around to index 0!)
#
# TRICK 🎯: Simulate circularity by processing the array TWICE
#   (loop i from 0 to 2n-1, use index i % n).
#   The FIRST n elements give the answers; the second pass lets
#   elements find greater ones that "wrap around".
# ------------------------------------------------------------------------------

def next_greater_element_circular(arr):
    """
    Find next greater element in a circular array.

    Time Complexity: O(n) - each index pushed/popped at most twice
    Space Complexity: O(n)
    """
    n = len(arr)
    result = [-1] * n
    stack = []

    print(f"\n   Circular Array: {arr}")
    print(f"   ⚡ Process the array TWICE to simulate wrapping!")
    print(f"   {'='*60}")

    # Process 2n elements using modulo (twice around the circle)
    for i in range(2 * n):
        idx = i % n
        print(f"\n   Pass element arr[{idx}] = {arr[idx]} (iteration {i})")

        while stack and arr[idx] > arr[stack[-1]]:
            popped_idx = stack.pop()
            if result[popped_idx] == -1:  # only set once!
                result[popped_idx] = arr[idx]
                print(f"   → arr[{popped_idx}] = {arr[popped_idx]}'s "
                      f"next greater = {arr[idx]} ✅")

        # Only push indices during the FIRST pass (avoid duplicates)
        if i < n:
            stack.append(idx)
            print(f"   Pushed index {idx} → Stack: {stack}")

    print(f"\n   ✅ Result: {result}")
    return result
# ==============================================================================
# PROBLEM 3: STOCK SPAN PROBLEM  (LeetCode 901) ⭐⭐⭐
# ==============================================================================
# The stock span of a day = number of consecutive days BEFORE today
# (including today) where the price was LESS THAN OR EQUAL to today's price.
#
# Example:
#   prices = [100, 80, 60, 70, 60, 75, 85]
#   spans  = [  1,  1,  1,  2,  1,  4,  6]
#
#   Explanation:
#   - Day 0 (100): No previous days → span = 1
#   - Day 1 (80):  Previous 100 > 80 → span = 1
#   - Day 2 (60):  Previous 80 > 60  → span = 1
#   - Day 3 (70):  60 ≤ 70 → span = 2 (days 2 & 3)
#   - Day 4 (60):  70 > 60 → span = 1
#   - Day 5 (75):  60, 70 ≤ 75 → span = 4 (days 2, 3, 4, 5)
#   - Day 6 (85):  all previous ≤ 85 until 100 → span = 6
#
# LOGIC (monotonic DECREASING stack of indices):
#   Span[i] = i - index_of_nearest_greater_price_on_the_left
#   If no greater price on the left → span = i + 1
# ------------------------------------------------------------------------------

def stock_span(prices):
    """
    Calculate stock span for each day using a monotonic stack.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    n = len(prices)
    span = [0] * n
    stack = []  # Stores indices of decreasing prices

    print(f"\n   Prices: {prices}")
    print(f"   {'='*60}")

    for i in range(n):
        # Pop all days with price <= current price
        # (They are "covered" by today's price)
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()

        # Nearest greater day to the left (or start of array)
        if not stack:
            span[i] = i + 1
        else:
            span[i] = i - stack[-1]

        stack.append(i)
        print(f"   Day {i} (Price: {prices[i]}) → Span: {span[i]}")
        print(f"   Stack of decreasing prices (indices): {stack}")
        print()

    return span
# ==============================================================================
# THE UNIVERSAL MONOTONIC STACK TEMPLATE 🧠 (Memorize this!)
# ==============================================================================
"""
HOW TO SPOT MONOTONIC STACK PROBLEMS:
  • "Next greater/smaller element for each item"
  • "Previous greater/smaller element"
  • "Consecutive days/prices smaller than today"
  • "Nearest bigger/smaller to the left/right"

THE 2-STEP TEMPLATE:
┌──────────────────────────────────────────────────────────────────┐
│  stack = []  # stores INDICES of elements "waiting"              │
│                                                                  │
│  for i in range(n):                                              │
│      # 1. RESOLVE: while current "beats" what's on the stack...  │
│      while (stack and arr[i] > arr[stack[-1]]):   # for GREATER  │
│      while (stack and arr[i] < arr[stack[-1]]):   # for SMALLER  │
│          top = stack.pop()                                       │
│          result[top] = arr[i]   # current is top's answer        │
│                                                                  │
│      # 2. PUSH: current waits for ITS answer                     │
│      stack.append(i)                                             │
│                                                                  │
│  # leftovers in the stack have no answer (→ -1, or a default)    │
└──────────────────────────────────────────────────────────────────┘

REMEMBER:
  • For "next/previous GREATER": keep a DECREASING stack
  • For "next/previous SMALLER": keep an INCREASING stack
  • Store INDICES not values (you get the value via arr[index])
  • Each index is pushed & popped AT MOST once → O(n) total!
"""


# ==============================================================================
# MAIN FUNCTION
# ==============================================================================

if __name__ == "__main__":

    print("\n" + "█" * 60)
    print("██  MONOTONIC STACK - The Interview Gold")
    print("█" * 60)

    # ──────────────────────────────────────────────────────────────────────────
    # PROBLEM 1: Next Greater Element
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 PROBLEM 1: NEXT GREATER ELEMENT (LeetCode 496)")
    print("=" * 60)
    print()
    print("   ⭐ THE problem that introduces the MONOTONIC STACK pattern!")
    print("   🧠 MENTAL MODEL:")
    print("   • The stack holds elements still waiting for their 'bigger one'")
    print("   • A new BIG element satisfies everyone smaller above it")

    nge = next_greater_element([4, 5, 2, 25])
    print(f"\n   ✅ Result: {nge}\n")

    # ──────────────────────────────────────────────────────────────────────────
    # PROBLEM 2: NGE II - Circular
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 PROBLEM 2: NEXT GREATER ELEMENT II - CIRCULAR (LeetCode 503)")
    print("=" * 60)
    print()
    print("   🧠 TRICK: Process the array TWICE (2n iterations,")
    print("   index = i % n) → elements can 'wrap around' the circle!")

    nge2 = next_greater_element_circular([1, 2, 1])
    print(f"\n   ✅ Result: {nge2}\n")

    # ──────────────────────────────────────────────────────────────────────────
    # THE TEMPLATE
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 THE UNIVERSAL MONOTONIC STACK TEMPLATE")
    print("=" * 60)
    print("""
   stack = []  # stores indices of "waiting" elements

   for i in range(n):
       # 1. RESOLVE: current beats waiting elements
       while stack and arr[i] > arr[stack[-1]]:  # for GREATER
           top = stack.pop()
           result[top] = arr[i]

       # 2. PUSH: current starts waiting
       stack.append(i)
    """)

    # ──────────────────────────────────────────────────────────────────────────
    # PROBLEM 3: Stock Span
    # ──────────────────────────────────────────────────────────────────────────
    print("=" * 60)
    print("📖 PROBLEM 3: STOCK SPAN (LeetCode 901)")
    print("=" * 60)
    print()
    print("   🧠 KEY INSIGHT:")
    print("   • 'Span' = distance to the nearest GREATER price on the left")
    print("   • Pop while previous price <= today → they're all covered!")

    spans = stock_span([100, 80, 60, 70, 60, 75, 85])
    print(f"   ✅ Spans: {spans}\n")

    print("🚀 NEXT: Run 06_expression_evaluation.py to see how compilers")
    print("   use stacks (Infix → Postfix → EVALUATE)!")