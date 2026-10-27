# 📘 Sliding Window — Easy 04
# Topic: Count occurrences of a pattern (anagram) in a string
# Approach: Fixed-size sliding window + character frequency map
# Time: O(n) | Space: O(1) (26 letters)

def count_anagram_occurrences(text, pattern):
    n = len(text)
    m = len(pattern)
    if m > n:
        return 0

    # frequency of pattern
    pattern_count = [0] * 26
    window_count = [0] * 26
    for ch in pattern:
        pattern_count[ord(ch) - ord('a')] += 1

    matches = 0
    for i in range(n):
        # add current character to window
        idx = ord(text[i]) - ord('a')
        window_count[idx] += 1

        # remove character that falls out of window
        if i >= m:
            out_idx = ord(text[i - m]) - ord('a')
            window_count[out_idx] -= 1

        # compare counts
        if window_count == pattern_count:
            matches += 1

    return matches


if __name__ == "__main__":
    import unittest

    class TestCountAnagram(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(count_anagram_occurrences("forxxorfxdofr", "for"), 3)

        def test_no_match(self):
            self.assertEqual(count_anagram_occurrences("abcdef", "xyz"), 0)

        def test_full_match(self):
            self.assertEqual(count_anagram_occurrences("a", "a"), 1)

    # Demo
    demo_text = "forxxorfxdofr"
    demo_pattern = "for"
    print(f"Input: text='{demo_text}', pattern='{demo_pattern}'")
    print(f"Anagram occurrences: {count_anagram_occurrences(demo_text, demo_pattern)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
