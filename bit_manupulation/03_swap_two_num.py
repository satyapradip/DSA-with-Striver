"""
Theory Explanation: Swapping Two Numbers Using XOR (Bit Manipulation)

Question: How can two numbers be swapped without using a temporary variable?

Approach: XOR Swap Algorithm

The XOR swap algorithm is a bitwise operation technique that allows two distinct variables to exchange their values without the need for a third temporary variable. This method leverages the properties of the XOR (exclusive OR) bitwise operator.

Properties of XOR:
1.  `x ^ x = 0` (XORing a number with itself results in 0)
2.  `x ^ 0 = x` (XORing a number with 0 results in the number itself)
3.  `x ^ y = y ^ x` (Commutative property)
4.  `(x ^ y) ^ z = x ^ (y ^ z)` (Associative property)

Algorithm Steps (to swap 'a' and 'b'):

1.  `a = a ^ b`
    -   'a' now holds the XOR sum of the original values of 'a' and 'b'.
    -   It essentially stores the "difference" between 'a' and 'b' in terms of bits that are set differently.

2.  `b = a ^ b`
    -   Substitute the new 'a' from step 1: `b = (original_a ^ original_b) ^ original_b`
    -   Using associative and commutative properties: `b = original_a ^ (original_b ^ original_b)`
    -   Since `original_b ^ original_b = 0`: `b = original_a ^ 0`
    -   Therefore: `b = original_a`.
    -   At this point, 'b' has successfully received the original value of 'a'.

3.  `a = a ^ b`
    -   Substitute the new 'a' from step 1 and the new 'b' from step 2: `a = (original_a ^ original_b) ^ original_a`
    -   Using associative and commutative properties: `a = (original_a ^ original_a) ^ original_b`
    -   Since `original_a ^ original_a = 0`: `a = 0 ^ original_b`
    -   Therefore: `a = original_b`.
    -   At this point, 'a' has successfully received the original value of 'b'.

Advantages:
-   **No Temporary Variable:** Eliminates the need for an extra memory space for a temporary variable.
-   **Atomic Operation (in some contexts):** Can be more efficient or even atomic in certain low-level programming scenarios, though modern compilers often optimize standard swaps.
-   **Handles Integer Overflow:** Unlike arithmetic swap (e.g., `a = a + b; b = a - b; a = a - b`), XOR swap does not suffer from potential overflow issues with fixed-size integers, as it operates on bits directly.

Example:
Let `a = 10` (binary `00001010`) and `b = 100` (binary `01100100`)

1.  `a = a ^ b`
    `a = 00001010 ^ 01100100 = 01101110` (decimal 110)

2.  `b = a ^ b`
    `b = 01101110 ^ 01100100 = 00001010` (decimal 10)  <- `b` now has `original_a`

3.  `a = a ^ b`
    `a = 01101110 ^ 00001010 = 01100100` (decimal 100) <- `a` now has `original_b`

Result: `a = 100`, `b = 10` - The numbers are successfully swapped.
"""

def swap_two_numbers(a, b):
  a = a ^ b
  b = a ^ b
  a = a ^ b
  return a, b

if __name__ == "__main__":
  print(swap_two_numbers(10, 100))