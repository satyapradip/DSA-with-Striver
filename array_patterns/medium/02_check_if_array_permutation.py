# 📘 Array Patterns — Medium 02
# Topic: Hashing — Check if Array is a Permutation
# Approach: Frequency count (or sum formula)
# Time: O(n) | Space: O(n)

def is_permutation(arr):
    """
    Returns True if arr is a permutation of 1..n.
    (i.e., contains all numbers 1 to n exactly once).
    """
    n = len(arr)
    seen = set()
    for num in arr:
        if num < 1 or num > n or num in seen:
            return False
        seen.add(num)
    return len(seen) == n


def is_permutation_sum(arr):
    """
    Alternative: using sum formula (n*(n+1)/2).
    Fails if duplicates present but sum matches.
    """
    n = len(arr)
    expected_sum = n * (n + 1) // 2
    return sum(arr) == expected_sum


def is_permutation_set(arr):
    """
    Alternative: using set (element distinctness).
    """
    n = len(arr)
    return set(arr) == set(range(1, n + 1))


if __name__ == "__main__":
    import unittest

    class TestIsPermutation(unittest.TestCase):
        def test_basic(self):
            self.assertTrue(is_permutation([1, 2, 3]))

        def test_with_duplicate(self):
            self.assertFalse(is_permutation([1, 2, 2]))

        def test_out_of_range(self):
            self.assertFalse(is_permutation([1, 3, 4]))

    # Demo
    demo = [4, 1, 3, 2]
    print(f"Input: {demo}")
    print(f"Is permutation? {is_permutation(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
