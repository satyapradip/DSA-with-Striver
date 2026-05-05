# String to Integer (atoi)
class Solution:
    def myAtoi(self, s: str) -> int:

        # ── Constants for 32-bit signed integer bounds ─────────────
        INT_MIN = -2**31        # -2147483648
        INT_MAX =  2**31 - 1   #  2147483647

        i = 0           # pointer walking through the string
        n = len(s)

        # ── Step 1: Skip leading whitespace ────────────────────────
        while i < n and s[i] == ' ':
            i += 1

        # ── Step 2: Read optional sign ─────────────────────────────
        sign = 1    # assume positive by default

        if i < n and s[i] in ('+', '-'):
            if s[i] == '-':
                sign = -1
            i += 1  # move past the sign character

        # ── Step 3: Read digits, build number ──────────────────────
        result = 0

        while i < n and s[i].isdigit():
            digit = int(s[i])   # convert char '7' → integer 7

            # Build number: shift existing digits left, add new digit
            # e.g. result=13, digit=3 → 13*10 + 3 = 133
            result = result * 10 + digit

            i += 1

        # Apply sign
        result *= sign

        # ── Step 4: Clamp to 32-bit signed integer range ───────────
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result
    

# Example usage:
sol = Solution()
print(sol.myAtoi("42"))            # Output: 42
print(sol.myAtoi("   -42"))        # Output: -42
print(sol.myAtoi("4193 with words")) # Output: 4193
print(sol.myAtoi("words and 987")) # Output: 0
print(sol.myAtoi("-91283472332")) # Output: -2147483648 (clamped to INT_MIN)


# Time Complexity: O(n) where n is the length of the input string. We may need to scan through the entire string once.
# Space Complexity: O(1) since we are using only a constant amount of extra space
