# 📘 Sliding Window — Hard 03
# Topic: Minimum Window Sorted (GFG)
# Approach: Sliding window with character frequency check
# Time: O(n * 26) or O(n) | Space: O(1)

def min_window_sorted(s, t):
    """
    Find the minimum window in s such that every character in t
    (including duplicates) is included in the window.
    """
    n, m = len(s), len(t)
    if m > n or m == 0:
        return ""

    # Count characters in t
    need = [0] * 256
    for ch in t:
        need[ord(ch)] += 1

    # Sliding window
    left = 0
    min_len = float('inf')
    min_left = 0
    min_right = 0
    formed = 0
    have = [0] * 256

    for right in range(n):
        # Add right character to window
        idx = ord(s[right])
        have[idx] += 1

        # If this character meets the need count, increment formed
        if need[idx] > 0 and have[idx] == need[idx]:
            formed += 1

        # Shrink while window is valid
        while formed == m:
            window_len = right - left + 1
            if window_len < min_len:
                min_len = window_len
                min_left = left
                min_right = right

            # Remove left character
            left_idx = ord(s[left])
            have[left_idx] -= 1
            if need[left_idx] > 0 and have[left_idx] < need[left_idx]:
                formed -= 1
            left += 1

    return s[min_left:min_right + 1] if min_len != float('inf') else ""


if __name__ == "__main__":
    import unittest

    class TestMinWindowSorted(unittest.TestCase):
        def test_basic(self):
            # "geeksforgeeks" contains 'o','r','k' in "ksfor" (len=5) — shortest
            self.assertEqual(min_window_sorted("geeksforgeeks", "ork"), "ksfor")

        def test_no_match(self):
            self.assertEqual(min_window_sorted("a", "aa"), "")

        def test_exact(self):
            self.assertEqual(min_window_sorted("a", "a"), "a")

    # Demo
    demo_s = "geeksforgeeks"
    demo_t = "ork"
    print(f"Input: s='{demo_s}', t='{demo_t}'")
    print(f"Minimum window: '{min_window_sorted(demo_s, demo_t)}'")
    print("Running unit tests...")
    unittest.main(verbosity=0)
