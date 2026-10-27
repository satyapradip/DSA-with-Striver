# 📘 Sliding Window — Medium 04
# Topic: Minimum Window Substring (LeetCode 76)
# Approach: Variable-size sliding window + frequency hashmap
# Time: O(|s| + |t| * 26) or O(|s| + |t|) | Space: O(1)

def min_window(s, t):
    """
    Find the minimum window substring of s such that every character
    in t (including duplicates) is included in the window.
    """
    if not s or not t:
        return ""

    # frequency of chars in t
    need = {}
    for ch in t:
        need[ch] = need.get(ch, 0) + 1

    # "have" window frequency
    have = {}
    required = len(need)          # number of distinct chars we need
    formed = 0                     # how many distinct chars we have met the count for
    have_count = {}

    left = 0
    min_len = float('inf')
    min_left = 0
    min_right = 0

    for right in range(len(s)):
        ch = s[right]

        # add char to have
        have[ch] = have.get(ch, 0) + 1

        # check if this char meets the need count
        if ch in need and have[ch] == need[ch]:
            formed += 1

        # shrink from left while window is valid
        while formed == required:
            # update min window
            window_len = right - left + 1
            if window_len < min_len:
                min_len = window_len
                min_left = left
                min_right = right

            # remove left char from window
            left_ch = s[left]
            have[left_ch] -= 1
            if left_ch in need and have[left_ch] < need[left_ch]:
                formed -= 1
            left += 1

    return s[min_left:min_right + 1] if min_len != float('inf') else ""


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
