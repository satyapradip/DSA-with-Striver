"""
Question: Check if a Number is a Power of Two

Given an integer n, determine whether it is a power of two.
A number is a power of two if it can be expressed as 2^k for some integer k >= 0.
For example: 1 (2^0), 2 (2^1), 4 (2^2), 8 (2^3), 16 (2^4), etc.

Approach: Bit Manipulation (The n & (n-1) Trick)

Key insight from binary representation:
- Every power of two has exactly one bit set in its binary form:
    1 = 1
    2 = 10
    4 = 100
    8 = 1000
    16 = 10000

- The property of n & (n-1):
    When you subtract 1 from a power of two, all bits after (and including)
    the only set bit become 1, and the set bit itself becomes 0.
    Example: n = 8 = 1000, n-1 = 7 = 0111, n & (n-1) = 1000 & 0111 = 0000

- So for any power of two, n & (n-1) == 0.
- For any non-power of two, this expression is non-zero.

- Edge case: n = 0 is not a power of two, but 0 & (-1) = 0,
  so we need the n > 0 check.

Time Complexity: O(1) — constant time bitwise operation
Space Complexity: O(1) — no extra space used
"""


def check_if_num_is_power_of_2(n):
    # n > 0 rejects 0 and negative numbers
    # (n & (n-1)) == 0 verifies exactly one bit is set
    return n > 0 and (n & (n-1)) == 0


if __name__ == "__main__":
    print(check_if_num_is_power_of_2(16))  # Expected: True (16 = 2^4)