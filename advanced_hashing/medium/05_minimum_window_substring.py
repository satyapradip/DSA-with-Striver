# 📘 Advanced Hashing — Medium 05
# Topic: Sliding Window + Hashmap — Minimum Window Substring
# Approach: Two-pointer window + character frequency hashmap
# Time: O(|s| + |t| * 26) or O(|s| + |t|)
# Space: O(1) or O(26)

def min_window(s, t):
    """
    Find the minimum window substring of s such that every character
    in t (including duplicates) is included in the window.
    """
    if not s or not t:
        return ""

    # Frequency of chars in t
    need = {}
    for ch in t:
        need[ch] = need.get(ch, 0) + 1

    # "have" window frequency
    have = {}
    required = len(need)          # distinct chars needed
    formed = 0                     # how many distinct chars met the count
    required_count = {}

    for ch, count in need.items():
        required_count[ch] = count

    left = 0
    min_len = float('inf')
    min_left = 0
    min_right = 0

    for right in range(len(s)):
        ch = s[right]

        # Add char to have
        have[ch] = have.get(ch, 0) + 1

        # Check if this char meets the need count
        if ch in need and have[ch] == required_count[ch]:
            formed += 1

        # Shrink while window is valid
        while formed == required:
            # Update min window
            window_len = right - left + 1
            if window_len < min_len:
                min_len = window_len
                min_left = left
                min_right = right

            # Remove left char from window
            left_ch = s[left]
            have[left_ch] -= 1
            if left_ch in need and have[left_ch] < required_count[left_ch]:
                formed -= 1
            left += 1

    return s[min_left:min_right + 1] if min_len != float('inf') else ""


def min_window_brute(s, t):
    """
    Brute force: O(n!) — all substrings.
    """
    from itertools import combinations
    n = len(s)
    result = ""
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            window = s[i:i + length]
            if all(window.count(ch) >= t.count(ch) for ch in set(t)):
                if len(window) < len(result) or not result:
                    result = window
    return result


if __name__ == "__main__":
    import unittest

    class TestMinWindow(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(min_window("ADOBECODEBANC", "ABC"), "BANC")

        def test_no_match(self):
            self.assertEqual(min_window("a", "aa"), "")

        def test_exact(self):
            self.assertEqual(min_window("a", "a"), "a")

    # Demo
    demo_s = "ADOBECODEBANC"
    demo_t = "ABC"
    print(f"Input: s='{demo_s}', t='{demo_t}'")
    print(f"Minimum window: '{min_window(demo_s, demo_t)}'")
    print("Running unit tests...")
    unittest.main(verbosity=0)
