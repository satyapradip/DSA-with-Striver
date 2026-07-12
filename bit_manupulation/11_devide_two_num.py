# 29. Divide Two Integers
# 
# Problem: Given two integers dividend and divisor, divide them WITHOUT using 
# multiplication, division, or mod operator. Return the quotient after integer division.
# Truncate toward zero (floor for positive, ceiling for negative).
#
# Constraints: 32-bit signed integer range [-2^31, 2^31 - 1]
#
# Approach: Bit Manipulation (Binary Long Division)
#
# Intuition:
# - Any integer can be expressed as a sum of powers of 2 (its binary representation).
# - For example: 10 = 8 + 2 = 2^3 + 2^1, so 10 / 3 = (8/3) + (2/3) ≈ 2 + 0 = 3
# - We can find the largest multiple of divisor that fits into dividend by
#   repeatedly shifting divisor left (multiplying by 2) until it exceeds dividend.
#
# Algorithm:
# 1. Handle the overflow edge case: INT_MIN / -1 would overflow 32-bit int.
# 2. Determine the sign of the result using XOR of signs.
# 3. Work with absolute values to simplify bit operations.
# 4. Iterate from the highest possible bit (31) down to 0:
#    - Check if (divisor << shift) fits into the remaining dividend.
#    - If yes, subtract it and add (1 << shift) to the quotient.
# 5. Apply the sign to the quotient.
#
# Why this works:
# - (divisor << shift) is equivalent to divisor * 2^shift
# - By trying larger shifts first, we greedily subtract the largest possible
#   multiple, building the quotient in binary from MSB to LSB.
# - This is essentially performing long division in binary.
#
# Time Complexity: O(32) = O(1) — we loop over 32 bits (constant for 32-bit ints)
# Space Complexity: O(1) — only a few variables used

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # ─────────────────────────────────────────────────────────
        # Step 1: Handle overflow edge case
        # ─────────────────────────────────────────────────────────
        # INT_MIN = -2^31 = -2147483648
        # INT_MAX = 2^31 - 1 = 2147483647
        # If we try (-2147483648) / (-1), the true quotient is 2147483648,
        # which is OUTSIDE the 32-bit signed integer range (overflows to INT_MIN).
        # Problem says to clamp to INT_MAX in this case.
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # ─────────────────────────────────────────────────────────
        # Step 2: Determine the sign of the result
        # ─────────────────────────────────────────────────────────
        # XOR (^) returns True when exactly one operand is True.
        # (dividend < 0) ^ (divisor < 0) is True when signs differ → result is negative.
        # Example: True ^ False = True → negative; False ^ False = False → positive.
        negative = (dividend < 0) ^ (divisor < 0)

        # ─────────────────────────────────────────────────────────
        # Step 3: Work with absolute values
        # ─────────────────────────────────────────────────────────
        # Bit manipulation is simpler with positive numbers.
        # We'll handle the sign at the end.
        dividend_abs = abs(dividend)
        divisor_abs = abs(divisor)

        # ─────────────────────────────────────────────────────────
        # Step 4: Early exit if dividend < divisor
        # ─────────────────────────────────────────────────────────
        # If the absolute dividend is smaller than the absolute divisor,
        # the quotient is 0 (integer division truncates toward zero).
        if dividend_abs < divisor_abs:
            return 0

        # ─────────────────────────────────────────────────────────
        # Step 5: Build the quotient using bit shifting
        # ─────────────────────────────────────────────────────────
        quotient = 0

        # We try subtracting the largest possible multiple of divisor
        # from dividend. Starting from the highest bit (31) down to 0.
        # Why 31? Because for 32-bit signed integers, the quotient can
        # be at most 2^31 - 1 (INT_MAX), which fits in 31 bits.
        #
        # For each shift value:
        #   - divisor_abs << shift  =  divisor_abs * 2^shift
        #   - If this value fits into the remaining dividend, we:
        #       1. Subtract it from dividend_abs
        #       2. Add 2^shift (= 1 << shift) to the quotient
        #
        # This is analogous to long division in decimal, but in binary:
        #   Decimal: 100 / 3 → try 3*30=90 (fits), remainder 10 → try 3*3=9 (fits) → quotient=33
        #   Binary:  100 / 3 → try 3*32=96 (fits), remainder 4 → try 3*1=3 (fits) → quotient=33
        for shift in range(31, -1, -1):
            # Check if divisor * 2^shift fits into the remaining dividend
            if dividend_abs >= (divisor_abs << shift):
                # Subtract the largest multiple that fits
                dividend_abs -= (divisor_abs << shift)
                # Add the corresponding power of 2 to the quotient
                quotient += 1 << shift

        # ─────────────────────────────────────────────────────────
        # Step 6: Apply the sign and return
        # ─────────────────────────────────────────────────────────
        return -quotient if negative else quotient

