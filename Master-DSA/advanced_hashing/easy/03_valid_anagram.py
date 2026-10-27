# 📘 Advanced Hashing — Easy 03
# Topic: Dict Hashing — Valid Anagram
# Approach: Character frequency map
# Time: O(n) | Space: O(1) or O(n)

def is_anagram(s, t):
    """
    Returns True if t is an anagram of s.
    Uses frequency map comparison.
    """
    if len(s) != len(t):
        return False

    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in t:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] == 0:
            del freq[ch]

    return len(freq) == 0


def is_anagram_counter(s, t):
    """
    Counter approach — more Pythonic.
    """
    from collections import Counter
    return Counter(s) == Counter(t)


def is_anagram_sort(s, t):
    """
    Sort approach — O(n log n) time.
    """
    return sorted(s) == sorted(t)


if __name__ == "__main__":
    import unittest

    class TestValidAnagram(unittest.TestCase):
        def test_basic(self):
            self.assertTrue(is_anagram("anagram", "nagaram"))

        def test_not_anagram(self):
            self.assertFalse(is_anagram("rat", "car"))

        def test_empty(self):
            self.assertTrue(is_anagram("", ""))

    # Demo
    demo_s = "anagram"
    demo_t = "nagaram"
    print(f"'{demo_s}' vs '{demo_t}': {is_anagram(demo_s, demo_t)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
