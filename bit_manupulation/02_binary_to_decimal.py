"""
================================================================================
Problem: Convert a Binary String to a Decimal Integer
================================================================================

Given a string representing a binary number (e.g., "1101"), convert it into
its equivalent decimal (base-10) integer.

--------------------------------------------------------------------------------
Theory: Understanding Binary to Decimal Conversion
--------------------------------------------------------------------------------

At its core, converting a binary (base-2) number to a decimal (base-10) number
is all about understanding **positional notation**. Each digit in a number has a
value based on its position, and that value is a power of the base.

In the decimal system (base-10), a number like `345` is really:
  (3 * 10^2) + (4 * 10^1) + (5 * 10^0) = 300 + 40 + 5 = 345

The binary system works the same way, but with a base of 2. For a binary
number like `1101`:
  (1 * 2^3) + (1 * 2^2) + (0 * 2^1) + (1 * 2^0) = 8 + 4 + 0 + 1 = 13

The goal of any conversion algorithm is to correctly calculate this sum.

"""

# ==============================================================================
# Approach 1: Manual Iteration with Powers (The Original Code)
# ==============================================================================
def convert_manual_iteration(binary_str: str) -> int:
  """
  Converts a binary string to decimal by manually implementing the
  positional notation formula. It iterates from right to left.
  """
  decimal_num = 0
  power = 0
  index = len(binary_str) - 1
  while index >= 0:
    # Get the numeric value of the bit (0 or 1)
    bit_val = int(binary_str[index])
    # Multiply it by the correct power of 2 and add to the total
    decimal_num += bit_val * (2**power)
    # Move to the next position (leftwards)
    index -= 1
    power += 1
  return decimal_num


# ==============================================================================
# Approach 2: Using Python's Built-in `int()` Function (The Pythonic Way)
# ==============================================================================
def convert_with_builtin(binary_str: str) -> int:
    """
    Converts a binary string using Python's built-in int() constructor.
    This is the most efficient and recommended approach in Python.
    """
    # The second argument '2' tells int() to interpret the string as base-2
    return int(binary_str, 2)


# ==============================================================================
# Approach 3: Using Bit Manipulation (Horner's Method)
# ==============================================================================
def convert_with_bit_manipulation(binary_str: str) -> int:
    """
    Converts a binary string using bit manipulation (left shift).
    This is an implementation of Horner's method, iterating from left to right.
    """
    decimal_num = 0
    for bit in binary_str:
        # Left shift the current result (multiply by 2)
        # and then add the new bit (0 or 1) using bitwise OR
        decimal_num = (decimal_num << 1) | int(bit)
    return decimal_num


# ==============================================================================
# Main block to test all approaches
# ==============================================================================
if __name__ == "__main__":
  binary_input = "110101" # Represents 32 + 16 + 4 + 1 = 53

  print(f"Converting binary string '{binary_input}' to decimal:\n")

  res1 = convert_manual_iteration(binary_input)
  print(f"Approach 1 (Manual Iteration): {res1}")

  res2 = convert_with_builtin(binary_input)
  print(f"Approach 2 (Built-in `int()`): {res2}")

  res3 = convert_with_bit_manipulation(binary_input)
  print(f"Approach 3 (Bit Manipulation): {res3}")