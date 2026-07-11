"""
Count the number of set bits (1s) in the binary representation of a number.

Example:
    Input: 13  (binary: 1101)
    Output: 3   (three 1s)

    Input: 7   (binary: 111)
    Output: 3

    Input: 0   (binary: 0)
    Output: 0
"""


def count_set_bits_brute_force(n):
    """
    Approach 1: Brute Force (dividing by 2)
    Time Complexity: O(log n) - number of bits in n
    Space Complexity: O(1)

    Continuously divide n by 2 and check if the remainder is 1.
    """
    count = 0
    while n > 0:
        if n % 2 == 1:  # Check if the last bit is set
            count += 1
        n //= 2  # Integer division (remove the last bit)
    return count


def count_set_bits_bitwise(n):
    """
    Approach 2: Using Bitwise AND with 1
    Time Complexity: O(log n) - number of bits in n
    Space Complexity: O(1)

    Use (n & 1) to check if the last bit is set, then right shift n by 1.
    """
    count = 0
    while n > 0:
        count += n & 1  # Add 1 if last bit is set, else 0
        n >>= 1         # Right shift by 1 (same as n //= 2)
    return count


def count_set_bits_kernighan(n):
    """
    Approach 3: Brian Kernighan's Algorithm (Most Efficient)
    Time Complexity: O(number of set bits) - only iterates over set bits
    Space Complexity: O(1)

    Key Insight: n & (n - 1) removes the rightmost set bit.
    Example: n = 13 (1101)
        n-1 = 12 (1100)
        n & (n-1) = 1100 (removed the rightmost 1)
    We count how many times we can do this until n becomes 0.
    """
    count = 0
    while n > 0:
        n = n & (n - 1)  # Remove the rightmost set bit
        count += 1
    return count


def count_set_bits_builtin(n):
    """
    Approach 4: Using Python's built-in bin() function
    Time Complexity: O(log n)
    Space Complexity: O(log n) - for the binary string

    Convert to binary string and count '1' characters.
    """
    return bin(n).count('1')


def count_set_bits_bit_length(n):
    """
    Approach 5: Using bit_length and bit manipulation
    Time Complexity: O(log n)
    Space Complexity: O(1)

    Iterate through each bit position using bit_length.
    """
    count = 0
    for i in range(n.bit_length()):
        if n & (1 << i):  # Check if the i-th bit is set
            count += 1
    return count


if __name__ == "__main__":
    test_cases = [13, 7, 0, 1, 15, 8, 255, 1024, 63, 100]

    print("Testing count_set_bits implementations:\n")

    for num in test_cases:
        r1 = count_set_bits_brute_force(num)
        r2 = count_set_bits_bitwise(num)
        r3 = count_set_bits_kernighan(num)
        r4 = count_set_bits_builtin(num)
        r5 = count_set_bits_bit_length(num)

        print(f"n = {num:4}  (binary: {bin(num):10})  ->  "
              f"Brute: {r1}, Bitwise: {r2}, Kernighan: {r3}, "
              f"Built-in: {r4}, BitLength: {r5}  "
              f"{'✓' if r1 == r2 == r3 == r4 == r5 else '✗'}")