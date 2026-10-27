# 📘 Advanced Hashing — Medium 02
# Topic: Sliding Window + Hashmap — Longest Substring Without Repeating
# Approach: Variable window + character frequency map
# Time: O(n) | Space: O(min(n, m)) where m = charset size

def length_of_longest_substring(s):
    """
    Returns the length of the longest substring without repeating characters.
    """
    freq = {}
    left = 0
    max_len = 0

    for right in range(len(s)):
        # Add s[right] to window
        freq[s[right]] = freq.get(s[right], 0) + 1

        # Shrink while window has duplicate
        while freq[s[right]] > 1:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


def length_of_longest_substring_brute(s):
    """
    Brute force: O(n²) — all substrings.
    """
    n = len(s)
    max_len = 0
    for i in range(n):
        seen = set()
        for j in range(i, n):
            if s[j] in seen:
                break
            seen.add(s[j])
            max_len = max(max_len, j - i + 1)
    return max_len


def length_of_longest_substring_optimized(s):
    """
    Optimized version using a dict to store last seen index.
    """
    last_seen = {}
    left = 0
    max_len = 0

    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right
        max_len = max(max_len, right - left + 1)

    return max_len


if __name__ == "__main__":
    import unittest

    class TestLongestSubstring(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(length_of_longest_substring("abcabcbb"), 3)

        def test_no_repeat(self):
            self.assertEqual(length_of_longest_substring("abcdef"), 6)

        def test_all_repeat(self):
            self.assertEqual(length_of_longest_substring("bbbbb"), 1)

    # Demo
    demo = "abcabcbb"
    print(f"Input: '{demo}'")
    print(f"Longest substring without repeating: {length_of_longest_substring(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
