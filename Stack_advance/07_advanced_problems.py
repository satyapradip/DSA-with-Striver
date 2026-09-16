"""
================================================================================
                 ADVANCED PROBLEMS - HARD MONOTONIC STACK ⭐⭐⭐⭐
================================================================================
Two of the HARDEST stack problems — both solved beautifully with the
monotonic stack pattern from file 05:

1. Largest Rectangle in Histogram (LeetCode 84) — THE classic hard one
2. Trapping Rain Water (LeetCode 42) — the "walls" problem

These problems frequently appear in:
  • FAANG interviews (Google, Meta, Amazon, Apple, Netflix)
  • Coding rounds for companies like Goldman Sachs, Uber, Adobe

Both use the same golden idea:
  "When a SMALLER element arrives, the previous bars' rectangles/water
   finalize — stack makes this O(n) instead of O(n²)!"
"""

# ==============================================================================
# PROBLEM 1: LARGEST RECTANGLE IN HISTOGRAM  (LeetCode 84) ⭐⭐⭐⭐
# ==============================================================================
# Given an array of non-negative integers representing bar heights in a
# histogram, find the area of the largest rectangle that can be formed.
#
# Example:
#   heights = [2, 1, 5, 6, 2, 3]
#   Output: 10 (area 5 × 2 using bars at index 2 and 3)
#
#   Visual:
#        ▓
#      ▓ ▓
#      ▓ ▓   ▓
#      ▓ ▓ ▓ ▓
#    ▓ ▓ ▓ ▓ ▓
#    ▓ ▓ ▓ ▓ ▓ ▓
#
# LOGIC (Monotonic INCREASING stack):
#   1. Process each bar left → right
#   2. While current height < height at stack top:
#      - Pop that height → it can extend right no further!
#      - Its rectangle width = current_index - stack_top - 1
#      - Area = height × width
#   3. Add a sentinel (height 0) at the end to flush the remaining bars
#
# Time Complexity: O(n) - each bar pushed/popped at most once
# Space Complexity: O(n)
# ------------------------------------------------------------------------------

def largest_rectangle_in_histogram(heights):
    """
    Find the largest rectangle area in a histogram using a stack.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    max_area = 0
    stack = []  # Stack of indices (increasing heights)
    n = len(heights)

    print(f"\n   Heights: {heights}")
    print(f"   ⚡ Monotonic INCREASING stack + sentinel trick!")
    print(f"   {'='*55}")

    # Loop n+1 times: the sentinel (height 0) flushes remaining bars
    for i in range(n + 1):
        current_height = heights[i] if i < n else 0
        print(f"\n   Bar {i}: height = "
              f"{'∞ (sentinel)' if i == n else current_height}")

        # While current bar is shorter, previous bar can't extend further right
        while stack and current_height < heights[stack[-1]]:
            height = heights[stack.pop()]

            # Width = how far this bar stretched between two shorter bars
            left_boundary = stack[-1] if stack else -1
            width = i - left_boundary - 1

            area = height * width
            print(f"   → Rect height={height}, width={width}, area={area}")
            max_area = max(max_area, area)

        stack.append(i)
        print(f"   Stack (indices): {stack} → heights: "
              f"{[heights[idx] for idx in stack if idx < n]}")

    print(f"\n   ✅ Largest Rectangle Area: {max_area}")
    return max_area
# ==============================================================================
# PROBLEM 2: TRAPPING RAIN WATER  (LeetCode 42) ⭐⭐⭐⭐
# ==============================================================================
# Given elevation heights, compute how much water can be trapped after rain.
#
# Example:
#   height = [0,1,0,2,1,0,1,3,2,1,2,1]
#   Output: 6 units of water 💧
#
#   Visual:
#                              ▓
#              ▓              ▓▓
#      ▓       ▓▓       ▓     ▓▓▓
#   ▓  ▓▓  💧  ▓▓💧  💧  ▓▓💧  ▓▓▓💧
#   ▓▓  ▓▓💧  ▓▓▓💧  ▓▓💧  ▓▓▓  ▓▓▓
#
# LOGIC (Monotonic DECREASING stack):
#   1. Push indices of bars DEEPER than or equal to the ones before them
#      (i.e., keep a decreasing stack of heights)
#   2. When a HIGHER bar arrives → pop the shorter "valley" bar
#      • height = the popped bar (the bottom of the water)
#      • left wall = new stack top, right wall = current bar
#      • water width = current - left_wall - 1
#      • water level = min(left_wall, right_wall) - bottom
#   3. Sum all trapped water
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# ------------------------------------------------------------------------------

def trapping_rain_water(height):
    """
    Compute trapped rain water using a monotonic stack.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    stack = []
    water = 0
    n = len(height)

    print(f"\n   Heights: {height}")
    print(f"   ⚡ Monotonic DECREASING stack - each bar popped once!")
    print(f"   {'='*55}")

    for i in range(n):
        print(f"\n   Bar {i}: height = {height[i]}")

        # While current bar is TALLER than the stack top...
        while stack and height[i] > height[stack[-1]]:
            bottom = stack.pop()  # the bar that holds water on top of it

            if not stack:
                print(f"   → {height[bottom]} at idx {bottom}: no left wall "
                      f"→ water escapes")
                break

            left_wall = stack[-1]
            width = i - left_wall - 1
            water_height = min(height[left_wall], height[i]) - height[bottom]

            if water_height > 0:
                trapped = width * water_height
                water += trapped
                print(f"   → Valley {height[bottom]} at idx {bottom}: "
                      f"walls {height[left_wall]} (idx {left_wall}) & "
                      f"{height[i]} (idx {i}) → {'💧' * trapped} +{trapped}")
            else:
                print(f"   → Valley {height[bottom]} at idx {bottom}: "
                      f"no water (flat)")

        stack.append(i)
        print(f"   Stack: {stack} → heights: {[height[idx] for idx in stack]}")

    print(f"\n   ✅ Total water trapped: {water} 💧")
    return water
# ==============================================================================
# VISUAL EXPLANATION 🧠
# ==============================================================================
"""
WHY DOES THE STACK WORK FOR HISTOGRAM & RAIN WATER?
====================================================

💰 LARGEST RECTANGLE IN HISTOGRAM:
   Each bar can be the HEIGHT of a rectangle. Its WIDTH stretches until it
   meets a shorter bar on the left and on the right.
   • When a shorter bar arrives → the previous bar's rectangle ENDS there.
   • area = height × (right_shorter - left_shorter - 1)

💧 TRAPPING RAIN WATER:
   Water collects ONLY between a left wall and a right wall with a
   valley (bottom) between them.
   • When a taller bar arrives, the valley on the stack top is filled:
     water = (min(left_wall, right_wall) - bottom) × width

⚠️ SAME FAMILY, DIFFERENT FLAVOR:
   ┌──────────────────────────┬────────────────────────────────────────┐
   │ Histogram                │ Rain Water                            │
   ├──────────────────────────┼────────────────────────────────────────┤
   │ Stack order              │ INCREASING (deeper→taller at top)     │
   │ Trigger to pop           │ Current < top (shorter arrives)       │
   │ Popped bar               │ Is the RECTANGLE HEIGHT               │
   │ Width formula            │ i - stack_top - 1                     │
   │ Area = height × width    │ Water = depth × width                 │
   └──────────────────────────┴────────────────────────────────────────┘
   │ Rain Water               │                                       │
   │ Stack order              │ DECREASING (taller→deeper at top)     │
   │ Trigger to pop           │ Current > top (taller arrives)        │
   │ Popped bar               │ Is the WATER BOTTOM (valley)          │
   │ Width formula            │ i - stack_top - 1                     │
   │ Water = min walls - bot  │ × width                               │
   └──────────────────────────┴────────────────────────────────────────┘
"""


# ==============================================================================
# MAIN FUNCTION
# ==============================================================================

if __name__ == "__main__":

    print("\n" + "█" * 60)
    print("██  ADVANCED PROBLEMS - Hard Monotonic Stack")
    print("█" * 60)

    # ──────────────────────────────────────────────────────────────────────────
    # PROBLEM 1: Largest Rectangle in Histogram
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 PROBLEM 1: LARGEST RECTANGLE IN HISTOGRAM (LeetCode 84)")
    print("=" * 60)
    print()
    print("   🧠 MENTAL MODEL:")
    print("   • Each bar can be a rectangle's height")
    print("   • Its width = distance between two SHORTER bars around it")
    print("   • Sentinel (0) at the end flushes all remaining rectangles!")

    max_rect = largest_rectangle_in_histogram([2, 1, 5, 6, 2, 3])
    print(f"\n   ✅ Max Rectangle Area: {max_rect}\n")

    # ──────────────────────────────────────────────────────────────────────────
    # PROBLEM 2: Trapping Rain Water
    # ──────────────────────────────────────────────────────────────────────────
    print("=" * 60)
    print("📖 PROBLEM 2: TRAPPING RAIN WATER (LeetCode 42)")
    print("=" * 60)
    print()
    print("   🧠 MENTAL MODEL:")
    print("   • Water needs 3 things: left wall + right wall + valley")
    print("   • A new TALLER bar fills the valley under it")
    print("   • Water escapes if there's NO left wall!")

    trapped = trapping_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    print(f"\n   ✅ Total water: {trapped} 💧\n")

    # ──────────────────────────────────────────────────────────────────────────
    # MORE TEST CASES
    # ──────────────────────────────────────────────────────────────────────────
    print("=" * 60)
    print("📖 MORE TEST CASES")
    print("=" * 60)

    largest_rectangle_in_histogram([1, 2, 3, 4, 5])
    trapping_rain_water([4, 2, 0, 3, 2, 5])

    print("\n🚀 NEXT: Run 08_practice_roadmap.py to see your full")
    print("   learning path and practice checklist!")