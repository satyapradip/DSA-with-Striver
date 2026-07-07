"""
================================================================
BIT MANIPULATION - BASICS FOR BEGINNERS
================================================================

WHAT IS BIT MANIPULATION?
-------------------------
Bit manipulation is the act of algorithmically manipulating BITS
(the 0s and 1s) that represent data in a computer.

Every number in a computer is stored as a sequence of bits.
For example, the decimal number 5 is stored in binary as: 0101

Bit manipulation lets you directly access and modify these bits,
which is often MUCH FASTER than using regular arithmetic operations.

WHY LEARN BIT MANIPULATION?
---------------------------
1. SPEED   - Bit operations are processed by the CPU in a single cycle.
2. MEMORY  - You can pack many flags/values into a single integer.
3. TRICKS  - Many problems have elegant one-line bit solutions.
4. INTERVIEWS - Frequently asked in coding interviews (DSA).

BINARY NUMBER SYSTEM (Quick Recap)
-----------------------------------
We normally use decimal (base-10):  0,1,2,3,4,5,6,7,8,9
Computers use binary (base-2):      0, 1

Each binary digit is called a BIT.
8 bits = 1 byte.

Example:
    Decimal 5  ->  Binary 0101
    (because 0*8 + 1*4 + 0*2 + 1*1 = 5)

    Decimal 13 ->  Binary 1101
    (because 1*8 + 1*4 + 0*2 + 1*1 = 13)

In Python, you can see the binary form using bin():
    bin(5)  ->  '0b101'       (0b prefix means "binary")
    bin(13) ->  '0b1101'
================================================================
"""


# ----------------------------------------------------------------
# SECTION 1: THE SIX BITWISE OPERATORS
# ----------------------------------------------------------------
# Python provides 6 bitwise operators. Let's understand each one.


def bitwise_and(a, b):
    """
    BITWISE AND  (&)
    -----------------
    Compares each bit of two numbers.
    Result bit is 1 ONLY if BOTH input bits are 1.

    Truth Table:
        1 & 1 = 1
        1 & 0 = 0
        0 & 1 = 0
        0 & 0 = 0

    Example: 12 & 10
        12 = 1100
        10 = 1010
        ------------ (AND)
         8 = 1000
    """
    print(f"{a} & {b} = {a & b}")
    print(f"  {a} = {bin(a)}")
    print(f"  {b} = {bin(b)}")
    print(f"result = {bin(a & b)}")
    return a & b


def bitwise_or(a, b):
    """
    BITWISE OR  (|)
    ----------------
    Result bit is 1 if AT LEAST ONE input bit is 1.

    Truth Table:
        1 | 1 = 1
        1 | 0 = 1
        0 | 1 = 1
        0 | 0 = 0

    Example: 12 | 10
        12 = 1100
        10 = 1010
        ------------ (OR)
        14 = 1110
    """
    print(f"{a} | {b} = {a | b}")
    print(f"  {a} = {bin(a)}")
    print(f"  {b} = {bin(b)}")
    print(f"result = {bin(a | b)}")
    return a | b


def bitwise_xor(a, b):
    """
    BITWISE XOR  (^)   (Exclusive OR)
    ----------------------------------
    Result bit is 1 if the two input bits are DIFFERENT.

    Truth Table:
        1 ^ 1 = 0
        1 ^ 0 = 1
        0 ^ 1 = 1
        0 ^ 0 = 0

    Example: 12 ^ 10
        12 = 1100
        10 = 1010
        ------------ (XOR)
         6 = 0110

    IMPORTANT PROPERTIES OF XOR:
        a ^ a = 0          (any number XOR itself = 0)
        a ^ 0 = a          (any number XOR 0 = itself)
        a ^ b ^ a = b      (used to find unique elements!)
    """
    print(f"{a} ^ {b} = {a ^ b}")
    print(f"  {a} = {bin(a)}")
    print(f"  {b} = {bin(b)}")
    print(f"result = {bin(a ^ b)}")
    return a ^ b


def bitwise_not(a):
    """
    BITWISE NOT  (~)   (One's Complement)
    --------------------------------------
    Flips every bit: 0 -> 1, and 1 -> 0.

    In Python, integers have UNLIMITED precision (no fixed bit width),
    so ~x  =  -(x + 1)

    Example:
        ~5  =  -6
        ~0  =  -1

    For a 4-bit example (conceptually):
        5  = 0101
        ~5 = 1010  (in 4-bit signed, this represents -6)

    NOTE: Beginners often find NOT confusing because of negative
    numbers. Just remember: ~x = -(x+1) in Python.
    """
    print(f"~{a} = {~a}")
    print(f"  {a} = {bin(a)}")
    print(f"result = {~a}  (because ~x = -(x+1) in Python)")
    return ~a


def left_shift(a, n):
    """
    LEFT SHIFT  (<<)
    -----------------
    Shifts all bits to the LEFT by 'n' positions.
    Zeros fill in from the right.

    a << n  is equivalent to  a * (2 ** n)
    (Left shifting multiplies by 2, n times!)

    Example: 5 << 2
        5      = 0000 0101
        5 << 2 = 0001 0100  = 20

    Because: 5 * (2^2) = 5 * 4 = 20
    """
    print(f"{a} << {n} = {a << n}")
    print(f"  {a}      = {bin(a)}")
    print(f"  {a} << {n} = {bin(a << n)}")
    print(f"  (equals {a} * 2^{n} = {a * (2 ** n)})")
    return a << n


def right_shift(a, n):
    """
    RIGHT SHIFT  (>>)
    ------------------
    Shifts all bits to the RIGHT by 'n' positions.
    Bits on the right are discarded.

    a >> n  is equivalent to  a // (2 ** n)  (for positive numbers)
    (Right shifting divides by 2, n times!)

    Example: 20 >> 2
        20      = 0001 0100
        20 >> 2 = 0000 0101  = 5

    Because: 20 // (2^2) = 20 // 4 = 5
    """
    print(f"{a} >> {n} = {a >> n}")
    print(f"  {a}      = {bin(a)}")
    print(f"  {a} >> {n} = {bin(a >> n)}")
    print(f"  (equals {a} // 2^{n} = {a // (2 ** n)})")
    return a >> n


# ----------------------------------------------------------------
# SECTION 2: COMMON BIT MANIPULATION TRICKS / PATTERNS
# ----------------------------------------------------------------
# These patterns appear again and again in DSA problems.


def is_even(n):
    """
    TRICK 1: Check if a number is EVEN or ODD using AND
    ----------------------------------------------------
    The LAST bit (least significant bit) tells us if a number is odd:
        - If last bit is 1  -> number is ODD
        - If last bit is 0  -> number is EVEN

    So: n & 1
        returns 1 if n is odd
        returns 0 if n is even

    This is FASTER than n % 2.
    """
    return n & 1 == 0  # True if even, False if odd


def get_ith_bit(n, i):
    """
    TRICK 2: Get the i-th bit (check if it is 0 or 1)
    --------------------------------------------------
    Bit positions are numbered from RIGHT to LEFT, starting at 0.

         number: 1 0 1 1 0
         index:  4 3 2 1 0

    To check the i-th bit:
        1. Create a mask:  1 << i   (only the i-th bit is 1)
        2. AND with n:     n & (1 << i)
        3. If result != 0, the i-th bit is 1.

    Example: get_ith_bit(5, 0)
        5 = 101, mask for i=0 is 1 << 0 = 001
        5 & 1 = 101 & 001 = 001  -> bit is 1
    """
    mask = 1 << i
    return 1 if (n & mask) != 0 else 0


def set_ith_bit(n, i):
    """
    TRICK 3: Set the i-th bit (make it 1)
    --------------------------------------
    Use OR to force a bit to 1.

    mask = 1 << i
    result = n | mask

    Example: set_ith_bit(5, 1)
        5 = 101,  mask = 010
        5 | 2 = 101 | 010 = 111 = 7
    """
    mask = 1 << i
    return n | mask


def clear_ith_bit(n, i):
    """
    TRICK 4: Clear the i-th bit (make it 0)
    ---------------------------------------
    Use AND with the INVERTED mask.

    mask = ~(1 << i)     -> all bits 1 EXCEPT the i-th bit
    result = n & mask

    Example: clear_ith_bit(7, 1)
        7 = 111,  mask = ~010 = ...111101
        7 & ~2 = 111 & ...101 = 101 = 5
    """
    mask = ~(1 << i)
    return n & mask


def toggle_ith_bit(n, i):
    """
    TRICK 5: Toggle the i-th bit (flip 0<->1)
    -----------------------------------------
    Use XOR. XOR with 1 flips a bit; XOR with 0 keeps it.

    mask = 1 << i
    result = n ^ mask

    Example: toggle_ith_bit(5, 0)
        5 = 101,  mask = 001
        5 ^ 1 = 101 ^ 001 = 100 = 4
    """
    mask = 1 << i
    return n ^ mask


def count_set_bits(n):
    """
    TRICK 6: Count the number of SET bits (1s) - Brian Kernighan's Algorithm
    -------------------------------------------------------------------------
    A "set bit" is a bit that is 1.

    NAIVE METHOD: Check every bit one by one (32/64 iterations).

    KERNIGHAN'S METHOD (smart!):
        The trick: n & (n-1)  clears the RIGHTMOST set bit of n.

        So we repeatedly do  n = n & (n-1)  and count how many times
        we do this until n becomes 0.

        Each operation removes exactly ONE set bit, so the number of
        operations = number of set bits.

    Example: count set bits in 9
        9 = 1001  (two 1s)
        Step 1: 9 & 8  = 1001 & 1000 = 1000 = 8,  count=1
        Step 2: 8 & 7  = 1000 & 0111 = 0000 = 0,  count=2
        Done! Count = 2

    Time Complexity: O(number of set bits)  -> faster than checking all bits
    """
    count = 0
    while n > 0:
        n = n & (n - 1)  # clears the rightmost set bit
        count += 1
    return count


def is_power_of_two(n):
    """
    TRICK 7: Check if a number is a POWER OF TWO
    --------------------------------------------
    Powers of two in binary have EXACTLY ONE set bit:
        1  = 0001
        2  = 0010
        4  = 0100
        8  = 1000
        16 = 10000

    KEY INSIGHT:
        If n is a power of two, then  n & (n-1) == 0
        Because removing the only set bit gives 0.

    Example: n=8
        8 = 1000,  7 = 0111
        8 & 7 = 0000  -> is a power of two!

    Example: n=6
        6 = 0110,  5 = 0101
        6 & 5 = 0100  -> NOT zero, so NOT a power of two.

    We also check n > 0 because 0 is not a power of two.
    """
    return n > 0 and (n & (n - 1)) == 0


def swap_without_temp(a, b):
    """
    TRICK 8: Swap two numbers WITHOUT a temporary variable (using XOR)
    -----------------------------------------------------------------
    Using the XOR properties: a ^ a = 0  and  a ^ 0 = a

    Steps:
        a = a ^ b
        b = a ^ b    ->  (a^b) ^ b = a    (b becomes old a)
        a = a ^ b    ->  (a^b) ^ a = b    (a becomes old b)

    Example: a=5, b=3
        a = 5 ^ 3 = 6
        b = 6 ^ 3 = 5   (now b holds old a)
        a = 6 ^ 5 = 3   (now a holds old b)
    Swapped! a=3, b=5
    """
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


def find_unique_in_pairs(arr):
    """
    TRICK 9: Find the only NON-repeating element (all others appear twice)
    -----------------------------------------------------------------------
    XOR PROPERTY:  a ^ a = 0   and   a ^ 0 = a

    If we XOR all elements together:
        - Pairs cancel out (become 0)
        - The unique element remains

    Example: [2, 3, 4, 2, 3]
        2 ^ 3 ^ 4 ^ 2 ^ 3
        = (2^2) ^ (3^3) ^ 4
        = 0 ^ 0 ^ 4
        = 4   <- the unique element!

    This is O(n) time and O(1) space. VERY common interview question.
    """
    result = 0
    for num in arr:
        result = result ^ num
    return result


def rightmost_set_bit_position(n):
    """
    TRICK 10: Find the POSITION of the rightmost set bit
    ----------------------------------------------------
    n & (n-1)  clears the rightmost set bit.
    So  n ^ (n & (n-1))  ISOLATES the rightmost set bit.

    Then we can find its position.

    Example: n = 18  = 10010
        n - 1 = 17 = 10001
        n & (n-1) = 10000
        n ^ that = 00010  -> the isolated rightmost set bit (value 2)
        position = 2  (1-based from the right)
    """
    if n == 0:
        return 0
    isolated = n ^ (n & (n - 1))  # isolates rightmost set bit
    position = 0
    while isolated > 1:
        isolated >>= 1
        position += 1
    return position + 1  # 1-based position


# ----------------------------------------------------------------
# SECTION 3: RUN ALL EXAMPLES (Main demonstration)
# ----------------------------------------------------------------

def main():
    print("=" * 60)
    print("BIT MANIPULATION DEMO")
    print("=" * 60)

    print("\n--- SECTION 1: Bitwise Operators ---\n")

    print("1) AND:")
    bitwise_and(12, 10)

    print("\n2) OR:")
    bitwise_or(12, 10)

    print("\n3) XOR:")
    bitwise_xor(12, 10)

    print("\n4) NOT:")
    bitwise_not(5)

    print("\n5) LEFT SHIFT:")
    left_shift(5, 2)

    print("\n6) RIGHT SHIFT:")
    right_shift(20, 2)

    print("\n--- SECTION 2: Common Tricks ---\n")

    print("1) Is 7 even?", is_even(7))    # False (odd)
    print("   Is 8 even?", is_even(8))    # True  (even)

    print("\n2) Get i-th bit of 5 (binary 101):")
    for i in range(3):
        print(f"   bit {i} of 5 = {get_ith_bit(5, i)}")

    print("\n3) Set bit 1 of 5:", set_ith_bit(5, 1))      # 5 (101) -> 7 (111)
    print("\n4) Clear bit 1 of 7:", clear_ith_bit(7, 1))  # 7 (111) -> 5 (101)
    print("\n5) Toggle bit 0 of 5:", toggle_ith_bit(5, 0))# 5 (101) -> 4 (100)

    print("\n6) Count set bits in 9 (binary 1001):", count_set_bits(9))  # 2

    print("\n7) Is 16 a power of two?", is_power_of_two(16))  # True
    print("   Is 6 a power of two?", is_power_of_two(6))     # False

    print("\n8) Swap 5 and 3 without temp variable:")
    a, b = swap_without_temp(5, 3)
    print(f"   After swap: a={a}, b={b}")

    print("\n9) Find unique element in [2, 3, 4, 2, 3]:")
    print("   Unique element:", find_unique_in_pairs([2, 3, 4, 2, 3]))  # 4

    print("\n10) Rightmost set bit position of 18 (binary 10010):")
    print("    Position:", rightmost_set_bit_position(18))  # 2

    print("\n" + "=" * 60)
    print("SUMMARY OF KEY OPERATORS:")
    print("=" * 60)
    print("  &   AND      - 1 only if both bits are 1")
    print("  |   OR       - 1 if at least one bit is 1")
    print("  ^   XOR      - 1 if bits are different")
    print("  ~   NOT      - flips all bits")
    print("  <<  Left     - shifts left, multiplies by 2")
    print("  >>  Right    - shifts right, divides by 2")
    print("=" * 60)


if __name__ == "__main__":
    main()


"""
================================================================
QUICK REFERENCE CHEAT SHEET
================================================================

OPERATOR  | NAME        | EXAMPLE  | RESULT | USE
----------|-------------|----------|--------|-------------------------
   &      | AND         | 12 & 10  |   8    | masking/checking bits
   |      | OR          | 12 | 10  |  14    | setting bits
   ^      | XOR         | 12 ^ 10  |   6    | toggling/finding unique
   ~      | NOT         |   ~5     |  -6    | flipping bits
   <<     | Left Shift  | 5 << 2   |  20    | multiply by 2^n
   >>     | Right Shift | 20 >> 2  |   5    | divide by 2^n

COMMON BITMASK FORMULAS:
------------------------
  Get i-th bit:        (n >> i) & 1            OR   n & (1 << i)
  Set i-th bit:        n | (1 << i)
  Clear i-th bit:      n & ~(1 << i)
  Toggle i-th bit:     n ^ (1 << i)
  Clear rightmost bit: n & (n - 1)
  Is power of two:     n > 0 and (n & (n - 1)) == 0
  Is even:             (n & 1) == 0
  Is odd:              (n & 1) == 1

XOR PROPERTIES (very important!):
---------------------------------
  a ^ a = 0       (same numbers cancel)
  a ^ 0 = a       (XOR with 0 does nothing)
  XOR is commutative & associative (order doesn't matter)
  => XOR all elements; pairs cancel, unique element remains

PRACTICE PROBLEMS TO TRY NEXT:
------------------------------
  1. Single Number (LeetCode 136)        - find unique in pairs
  2. Number of 1 Bits (LeetCode 191)     - count set bits
  3. Power of Two (LeetCode 231)         - check power of two
  4. Missing Number (LeetCode 268)       - XOR approach
  5. Single Number II (LeetCode 137)     - appears 3 times except one
  6. Reverse Bits (LeetCode 190)
  7. XOR of numbers from 1 to N          - find the pattern!
================================================================
"""