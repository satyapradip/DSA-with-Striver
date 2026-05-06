#Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.

# Approach 1 — Brute Force (O(n³)) — Know why it's bad

class Solution:
    def longestPalindrome(self, s: str) -> str:

        def isPalindrome(sub):
            return sub == sub[::-1]   # O(n) check

        result = ""

        # Try every possible substring — O(n²) pairs
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub = s[i:j+1]
                if isPalindrome(sub) and len(sub) > len(result):
                    result = sub

        return result
    

# Approach 2 — Expand Around Center (O(n²)) — Much better than brute force
class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        if not s:
            return ""

        result = ""
        for i in range(len(s)):
            # Odd length palindromes
            palindrome1 = expandAroundCenter(i, i)
            # Even length palindromes
            palindrome2 = expandAroundCenter(i, i + 1)

            # Update result if a longer palindrome is found
            if len(palindrome1) > len(result):
                result = palindrome1
            if len(palindrome2) > len(result):
                result = palindrome2

        return result
