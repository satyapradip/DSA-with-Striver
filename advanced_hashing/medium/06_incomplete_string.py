# 📘 Advanced Hashing — Medium 06
# Topic: Frequency Map + Two Pointers — Minimum Window to Make Complete
# Approach: Sliding window + character frequency counting
# Time: O(n) | Space: O(1)

def min_window_complete(s, chars_needed):
    """
    Returns the minimum window in s that contains all characters in chars_needed.
    """
    if not s or not chars_needed:
        return ""

    # Count chars needed
    need = {}
    for ch in chars_needed:
        need[ch] = need.get(ch, 0) + 1

    required = len(need)
    formed = 0
    have = {}

    left = 0
    min_len = float('inf')
    min_left = 0
    min_right = 0

    for right in range(len(s)):
        ch = s[right]
        have[ch] = have.get(ch, 0) + 1

        if ch in need and have[ch] == need[ch]:
            formed += 1

        while formed == required:
            window_len = right - left + 1
            if window_len < min_len:
                min_len = window_len
                min_left = left
                min_right = right

            left_ch = s[left]
            have[left_ch] -= 1
            if left_ch in need and have[left_ch] < need[left_ch]:
                formed -= 1
            left += 1

    return s[min_left:min_right + 1] if min_len != float('inf') else ""


def min_window_complete_brute(s, chars_needed):
    """
    Brute force: O(n²) — all substrings.
    """
    n = len(s)
    result = ""
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            window = s[i:i + length]
            if all(window.count(ch) >= chars_needed.count(ch) for ch in set(chars_needed)):
                if len(window) < len(result) or not result:
                    result = window
    return result


if __name__ == "__main__":
    import unittest

    class TestMinWindowComplete(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(min_window_complete("ADOBECODEBANC", "ABC"), "BANC")

        def test_no_match(self):
            self.assertEqual(min_window_complete("a", "ab"), "")

        def test_exact(self):
            self.assertEqual(min_window_complete("a", "a"), "a")

    # Demo
    demo_s = "ADOBECODEBANC"
    demo_chars = "ABC"
    print(f"Input: s='{demo_s}', chars='{demo_chars}'")
    print(f"Minimum window: '{min_window_complete(demo_s, demo_chars)}'")
    print("Running unit tests...")
    unittest.main(verbosity=0)
