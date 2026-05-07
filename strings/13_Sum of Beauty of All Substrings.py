# 1781. Sum of Beauty of All Substrings
# https://leetcode.com/problems/sum-of-beauty-of-all-substrings/
# The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.
# For example, the beauty of "abaacc" is 3 - 1 = 2. The most frequent character is 'a' with a frequency of 3, and the least frequent character is 'b' or 'c' with a frequency of 1.
# Given a string s, return the sum of beauty of all of its substrings.


class Solution:
    def beautySum(self, s: str) -> int:

        total = 0

        for left in range(len(s)):

            freq    = {}
            max_freq = 0   # track max frequency as we go

            for right in range(left, len(s)):

                char = s[right]
                freq[char] = freq.get(char, 0) + 1

                # Update max inline — no need to scan all values
                max_freq = max(max_freq, freq[char])

                # min still requires a scan — but only over ≤26 values
                min_freq = min(freq.values())

                total += max_freq - min_freq

        return total
    
# Time Complexity: O(n²) — We have two nested loops, and the inner loop does O(1) work for updating frequencies and calculating max/min.
# Space Complexity: O(1) — The frequency dictionary can have at most 26 entries for lowercase letters, which is constant space.