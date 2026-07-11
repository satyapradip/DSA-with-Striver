"""
Question: Minimum Bit Flips to Convert Number
==============================================

Problem Statement:
Given two integers `start` and `goal`, return the minimum number of bit flips
required to convert `start` to `goal`. A bit flip changes a single bit from
0 to 1 or 1 to 0.

Example:
    start = 10  -> binary: 1010
    goal  = 7   -> binary: 0111
    Bits differ at positions 3, 2, 0 -> 3 positions differ
    Output: 3

How to Run / Test Commands:
----------------------------
1. Run with sample test cases:
   python -c "
   from bit_manupulation.10_Minimum_Bit_Flips_to_Convert_Number import Solution
   s = Solution()
   print(s.minBitFlips(10, 7))    # Expected: 3
   print(s.minBitFlips(3, 4))     # Expected: 3 (011 ^ 100 = 111 -> 3 set bits)
   print(s.minBitFlips(0, 0))     # Expected: 0
   print(s.minBitFlips(1, 1))     # Expected: 0
   print(s.minBitFlips(8, 0))     # Expected: 1 (1000 ^ 0000 = 1000 -> 1 set bit)
   "

2. Run with random tests:
   python -c "
   import random
   from bit_manupulation.10_Minimum_Bit_Flips_to_Convert_Number import Solution
   s = Solution()
   for _ in range(5):
       a, b = random.randint(0, 255), random.randint(0, 255)
       flips = s.minBitFlips(a, b)
       print(f'minBitFlips({a}, {b}) = {flips}  (binary: {a:08b} -> {b:08b})')
   "

3. Run module directly (if __name__ == '__main__' block is present):
   python -m bit_manupulation.10_Minimum_Bit_Flips_to_Convert_Number

================================================================================
DETAILED CODE EXPLANATION
================================================================================

    def minBitFlips(self, start: int, goal: int) -> int:
        # Step 1: XOR to find bits that differ
        ans = start ^ goal
        count = 0

        # Step 2: Count set bits using Brian Kernighan's algorithm
        # ans & (ans - 1) removes the rightmost set bit
        while ans > 0:
            ans = ans & (ans - 1)  # Remove the rightmost set bit
            count += 1

        return count

LINE-BY-LINE WALKTHROUGH:
---------------------------

Line 1:  ans = start ^ goal
    - XOR (^) compares each bit of start and goal
    - Output bit = 1 when bits differ, 0 when bits match
    - Example: start=10 (1010), goal=7 (0111)
      1010
    ^ 0111
    ------
      1101   <- ans = 13 (decimal)
    - Now ans has set bits only at positions needing a flip

Line 2:  count = 0
    - Initialize counter for number of flips needed

Lines 5-7:  while ans > 0:  /  ans = ans & (ans - 1)  /  count += 1
    - This is Brian Kernighan's algorithm to count set bits
    - Key trick: ans & (ans - 1) removes the rightmost set bit

    WHY DOES ans & (ans - 1) WORK?
    - Subtracting 1 from a binary number flips all trailing 0s to 1s
      and flips the rightmost 1 to 0
    - Example: ans = 1101 (13)
      - ans - 1 = 1100 (12)
      - 1101 & 1100 = 1100  -> rightmost set bit removed
    - Example: ans = 1100 (12)
      - ans - 1 = 1011 (11)
      - 1100 & 1011 = 1000  -> rightmost set bit removed

    ITERATION WALKTHROUGH (start=10, goal=7):
    Iter | ans (before) | ans - 1 | ans & (ans-1) | count
    --------------------------------------------------------
    1    | 13 = 1101    | 12 = 1100 | 12 = 1100   | 1
    2    | 12 = 1100    | 11 = 1011 | 8  = 1000   | 2
    3    | 8  = 1000    | 7  = 0111 | 0  = 0000   | 3
    Loop ends because ans = 0

Line 8:  return count
    - Returns 3, which is the minimum number of bit flips needed

================================================================================
THREE APPROACHES TO SOLVE THIS PROBLEM
================================================================================

APPROACH 1: Brian Kernighan's Algorithm [OPTIMAL - Used in Code]
----------------------------------------------------------------
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = start ^ goal
        count = 0
        while ans > 0:
            ans = ans & (ans - 1)
            count += 1
        return count

    How it works:
    - XOR to isolate differing bits
    - ans & (ans - 1) repeatedly removes the rightmost set bit
    - Each removal = 1 bit flip counted
    - Loop runs only for set bits, not all bits

    Time: O(number of set bits in start ^ goal)
    Space: O(1)

    Example: start=10, goal=7
    ans = 13 (1101) -> 3 iterations -> 3 flips

APPROACH 2: Brute Force - Bit by Bit Comparison
----------------------------------------------------------------
    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0
        while start > 0 or goal > 0:
            # Check if LSBs differ
            if (start & 1) != (goal & 1):
                count += 1
            start >>= 1  # Right shift to check next bit
            goal >>= 1
        return count

    How it works:
    - Extract LSB of both numbers using & 1
    - If they differ, increment count
    - Right shift both numbers to examine the next bit
    - Continue until both numbers become 0

    Time: O(log n) = O(number of bits in larger number)
    Space: O(1)

    Example: start=10 (1010), goal=7 (0111)
    Iter | start LSB | goal LSB | Differ? | count | start>>1 | goal>>1
    ----------------------------------------------------------------
    1    | 0         | 1        | Yes     | 1     | 101      | 011
    2    | 1         | 1        | No      | 1     | 10       | 01
    3    | 0         | 0        | No      | 1     | 1        | 0
    4    | 1         | 0        | Yes     | 2     | 0        | 0
    5    | end       | end      | -       | 2?    | Wait, this is wrong!

    ACTUAL walkthrough:
    start=10 (1010), goal=7 (0111)
    Iter 1: start&1=0, goal&1=1 -> differ -> count=1, start=5(101), goal=3(011)
    Iter 2: start&1=1, goal&1=1 -> same  -> count=1, start=2(010), goal=1(001)
    Iter 3: start&1=0, goal&1=1 -> differ -> count=2, start=1(001), goal=0(000)
    Iter 4: start&1=1, goal&1=0 -> differ -> count=3, start=0, goal=0 -> exit
    Result: 3 flips ✓

APPROACH 3: Python Built-in bit_count() [SIMPLEST]
----------------------------------------------------------------
    def minBitFlips(self, start: int, goal: int) -> int:
        return (start ^ goal).bit_count()

    How it works:
    - XOR to find differing bits (same as Approach 1)
    - Python's int.bit_count() counts set bits natively
    - Implemented in C, highly optimized
    - Available from Python 3.8+

    Time: O(1) in practice (native C implementation)
    Space: O(1)

    Example: start=10, goal=7
    (10 ^ 7).bit_count() = 13.bit_count() = 3

================================================================================
COMPARISON SUMMARY
================================================================================
    Approach            | Time Complexity  | Code  | When to Use
    --------------------+------------------+-------+---------------------------
    Brian Kernighan     | O(set bits)      | 4 ln  | Optimal for sparse bits
    Brute Force         | O(log n)         | 6 ln  | Simple, easy to understand
    bit_count()         | O(1) native      | 1 ln  | Shortest, production-ready
"""


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # Step 1: XOR to find bits that differ
        ans = start ^ goal
        count = 0

        # Step 2: Count set bits using Brian Kernighan's algorithm
        # ans & (ans - 1) removes the rightmost set bit
        while ans > 0:
            ans = ans & (ans - 1)  # Remove the rightmost set bit
            count += 1

        return count


# --- Test the solution when run directly ---
if __name__ == "__main__":
    s = Solution()

    # Test case 1
    result = s.minBitFlips(10, 7)
    print(f"minBitFlips(10, 7)  = {result}  (binary: 1010 -> 0111)  Expected: 3")

    # Test case 2
    result = s.minBitFlips(3, 4)
    print(f"minBitFlips(3, 4)   = {result}  (binary: 0011 -> 0100)  Expected: 3")

    # Test case 3
    result = s.minBitFlips(0, 0)
    print(f"minBitFlips(0, 0)   = {result}  (binary: 0000 -> 0000)  Expected: 0")

    # Test case 4
    result = s.minBitFlips(8, 0)
    print(f"minBitFlips(8, 0)   = {result}  (binary: 1000 -> 0000)  Expected: 1")

    # Test case 5
    result = s.minBitFlips(0, 15)
    print(f"minBitFlips(0, 15)  = {result}  (binary: 0000 -> 1111)  Expected: 4")