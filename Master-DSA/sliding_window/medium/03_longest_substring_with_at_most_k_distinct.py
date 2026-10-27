# 📘 Sliding Window — Medium 03
# Topic: Longest Substring with At Most K Distinct Characters (LeetCode 340)
# Approach: Variable-size sliding window + hashmap
# Time: O(n) | Space: O(k)

def length_of_longest_substring_k_distinct(s, k):
    n = len(s)
    if n == 0 or k == 0:
        return 0

    freq = {}
    left = 0
    max_len = 0

    for right in range(n):
        # add s[right] to window
        freq[s[right]] = freq.get(s[right], 0) + 1

        # shrink while distinct chars > k
        while len(freq) > k:
            left_char = s[left]
            freq[left_char] -= 1
            if freq[left_char] == 0:
                del freq[left_char]
            left += 1

        # update answer
        max_len = max(max_len, right - left + 1)

    return max_len


def length_of_longest_substring_k_distinct_brute(s, k):
    n = len(s)
    max_len = 0
    for i in range(n):
        freq = {}
        for j in range(i, n):
            freq[s[j]] = freq.get(s[j], 0) + 1
            if len(freq) <= k:
                max_len = max(max_len, j - i + 1)
            else:
                break
    return max_len


if __name__ == "__main__":
    import unittest

    class TestLongestSubstringKDistinct(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(length_of_longest_substring_k_distinct("eceba", 2), 3)

        def test_one_distinct(self):
            self.assertEqual(length_of_longest_substring_k_distinct("aa", 1), 2)

        def test_k_larger(self):
            self.assertEqual(length_of_longest_substring_k_distinct("a", 5), 1)

    # Demo
    demo = "eceba"
    k = 2
    print(f"Input: '{demo}', k = {k}")
    print(f"Longest substring with ≤ {k} distinct chars: {length_of_longest_substring_k_distinct(demo, k)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
