# 📘 Advanced Hashing — Medium 03
# Topic: Frequency Map — Sum of Unique Characters
# Approach: Frequency counting + summation
# Time: O(n) | Space: O(1) (charset limited)

def sum_of_unique(s):
    """
    Returns the sum of the ASCII values of all unique characters (frequency = 1).
    """
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    total = 0
    for ch, count in freq.items():
        if count == 1:
            total += ord(ch)

    return total


def sum_of_unique_char(s):
    """
    Alternative: single pass with set / seen tracking.
    """
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    return sum(ord(ch) for ch, count in freq.items() if count == 1)


def sum_of_unique_brute(s):
    """
    Brute force: O(n²) — check each char.
    """
    total = 0
    for ch in s:
        if s.count(ch) == 1:
            total += ord(ch)
    return total


if __name__ == "__main__":
    import unittest

    class TestSumOfUnique(unittest.TestCase):
        def test_basic(self):
            # A=65, B=66, C=67 → 65+66+67 = 198
            self.assertEqual(sum_of_unique("ABC"), 198)

        def test_with_repeats(self):
            # A=65, B=66 → only B is unique → 66
            self.assertEqual(sum_of_unique("ABA"), 66)

        def test_single_char(self):
            self.assertEqual(sum_of_unique("Z"), 90)

    # Demo
    demo = "ABC"
    print(f"Input: '{demo}'")
    print(f"Sum of unique chars: {sum_of_unique(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
