"""
Theory Explanation: Setting the i-th Bit of a Number

Question: How can we set a specific bit (the i-th bit) of a given number 'n' to 1?

Approach: Bitwise OR with a Mask

To set a particular bit in a number means to ensure that the bit at a specified position becomes 1, regardless of its original value (0 or 1). This is typically achieved using bitwise operations, specifically the bitwise OR operator (`|`).

Properties of Bitwise OR (`|`):
-   `0 | 0 = 0`
-   `0 | 1 = 1`
-   `1 | 0 = 1`
-   `1 | 1 = 1`
    The key property here is that `X | 1` will always result in `1`, and `X | 0` will result in `X`. This means if we OR a bit with 1, it becomes 1. If we OR a bit with 0, it remains unchanged.

Algorithm Steps (to set the i-th bit of 'n'):

1.  **Create a Mask:**
    -   We need a mask that has only the `i`-th bit set to 1, and all other bits set to 0.
    -   This mask is created by left-shifting the integer `1` by `i` positions (`1 << i`).
    -   For example, if `i = 2`: `1` (binary `0001`) shifted left by 2 becomes `0100` (binary, decimal 4). This mask specifically targets the 2nd bit (0-indexed).

2.  **Perform Bitwise OR:**
    -   Perform a bitwise OR operation between the original number `n` and the created mask: `result = n | (1 << i)`.
    -   Because of the properties of OR, the `i`-th bit in `n` will be forced to 1. All other bits in `n` will remain unchanged because they are OR'd with 0s from the mask.

Example:
Let `n = 13` (binary `1101`) and we want to set the `i = 1`-th bit (0-indexed).

1.  **Create Mask (`1 << i`):**
    `1 << 1` = `0010` (binary, decimal 2)

2.  **Perform Bitwise OR (`n | mask`):**
    `n`     = `1101` (original number 13)
    `mask`  = `0010`
    -----------------
    `result`= `1111` (decimal 15)

The original `1`-th bit of `n` was `0`. After the operation, it became `1`. The other bits remained unchanged.

Therefore, `set_ith_bit(13, 1)` should return `15`.
"""

def set_ith_bit(n, i):
  # To set the i-th bit of a number 'n':
  # 1. Create a mask: Left-shift 1 by 'i' positions (1 << i). This generates a number with only the i-th bit set to 1.
  #    Example: To set the 2nd bit (i=2), mask is 1 << 2 = 0100 (binary).
  # 2. Perform bitwise OR: (n | (1 << i)).
  #    - If the i-th bit in 'n' is 0, it becomes 1.
  #    - If the i-th bit in 'n' is 1, it remains 1.
  return (n | (1 << i))

if __name__ == "__main__":
  n_val = 13  # Binary: 1101
  i_val = 1   # Set the 1st bit (0-indexed)
  result = set_ith_bit(n_val, i_val)
  print(f"Original number: {n_val} (binary: {bin(n_val)})")
  print(f"Setting {i_val}-th bit:")
  print(f"Result: {result} (binary: {bin(result)})") # Expected: 15 (binary: 1111)

  n_val = 10  # Binary: 1010
  i_val = 0   # Set the 0th bit
  result = set_ith_bit(n_val, i_val)
  print(f"Original number: {n_val} (binary: {bin(n_val)})")
  print(f"Setting {i_val}-th bit:")
  print(f"Result: {result} (binary: {bin(result)})") # Expected: 11 (binary: 1011)