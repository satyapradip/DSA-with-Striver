"""
================================================================================
Problem: Convert a Decimal Integer to a Binary String
================================================================================

Given a non-negative integer `n`, convert it into its binary string representation.

--------------------------------------------------------------------------------
Theory: Understanding Decimal to Binary Conversion
--------------------------------------------------------------------------------

The conversion from decimal (base-10) to binary (base-2) is fundamentally about
expressing the number as a sum of powers of two. The standard algorithm to
achieve this is through **repeated division by 2**.

The process is as follows:
1.  Take the decimal number and divide it by 2.
2.  Record the **remainder** (which will be either 0 or 1). This remainder is a
    bit in the binary representation.
3.  Use the **quotient** from the division as the new number for the next step.
4.  Repeat this process until the quotient becomes 0.
5.  The binary representation is the sequence of remainders read in **reverse order**
    (from last to first).

Example: Convert 13 to binary
*   `13 / 2 = 6` with a remainder of **`1`** (This is the rightmost bit, or LSB)
*   `6 / 2 = 3` with a remainder of **`0`**
*   `3 / 2 = 1` with a remainder of **`1`**
*   `1 / 2 = 0` with a remainder of **`1`** (This is the leftmost bit, or MSB)

Reading the remainders from bottom to top gives us **`1101`**.

"""

# ==============================================================================
# Approach 1: Iteration with Modulo and Division (The Original Code)
# ==============================================================================
def decimal_to_binary_iterative(n: int) -> str:
    """
    Converts a decimal integer to binary using a while loop with
    modulo and integer division.
    """
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        remainder = n % 2
        # Prepending the remainder string builds the binary string in the correct order
        result = str(remainder) + result
        n = n // 2
    return result


# ==============================================================================
# Approach 2: Using Python's Built-in `bin()` Function (The Pythonic Way)
# ==============================================================================
def decimal_to_binary_builtin(n: int) -> str:
    """
    Converts a decimal integer to its binary string representation
    using the built-in bin() function. This is the simplest and most
    idiomatic approach in Python.
    """
    # bin(n) returns a string like '0b1101'. We slice off the '0b' prefix.
    return bin(n)[2:]


# ==============================================================================
# Approach 3: Using Bitwise Operators (More Efficient Iteration)
# ==============================================================================
def decimal_to_binary_bitwise(n: int) -> str:
    """
    Converts a decimal integer to binary using bitwise operators, which can
    be more efficient than arithmetic operators.
    """
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        # Get the last bit using bitwise AND with 1 (equivalent to n % 2)
        last_bit = n & 1
        result = str(last_bit) + result
        # Right shift the number to process the next bit (equivalent to n // 2)
        n = n >> 1
    return result


# ==============================================================================
# Approach 4: Recursive Approach
# ==============================================================================
def decimal_to_binary_recursive(n: int) -> str:
    """
    Converts a decimal integer to binary using recursion.
    """
    # Base case for the recursion (n is 0 or 1)
    if n <= 1:
        return str(n)
    # Recurse with n divided by 2, then append the current remainder
    return decimal_to_binary_recursive(n // 2) + str(n % 2)


# ==============================================================================
# Main block to test all approaches
# ==============================================================================
if __name__ == "__main__":
    test_cases = [0, 1, 2, 10, 13, 255]

    for num in test_cases:
        print(f"─" * 40)
        print(f"Converting decimal '{num}' to binary:\n")

        res1 = decimal_to_binary_iterative(num)
        print(f"Approach 1 (Iterative):      {res1}")

        res2 = decimal_to_binary_builtin(num)
        print(f"Approach 2 (Built-in `bin()`): {res2}")

        res3 = decimal_to_binary_bitwise(num)
        print(f"Approach 3 (Bitwise):        {res3}")

        res4 = decimal_to_binary_recursive(num)
        print(f"Approach 4 (Recursive):      {res4}")

        # Verification
        if res1 == res2 == res3 == res4:
            print("\n✅ All approaches match.")
        else:
            print("\n❌ Mismatch in results!")
        print(f"─" * 40)