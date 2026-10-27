# 📘 Array Patterns — Medium 04
# Topic: Prefix Sum / Math — Find the Missing Number
# Approach: Gauss sum formula (O(1) space) or hashset
# Time: O(n) | Space: O(1)

def find_missing_number(arr):
    """
    Returns the missing number in array [1..n+1] (n elements, one missing).
    Uses Gauss sum formula: n(n+1)/2 - sum(arr)
    """
    n = len(arr) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum


def find_missing_number_xor(arr):
    """
    XOR approach — avoids overflow (if using C++/Java).
    XOR all indices 1..n+1 with all array elements.
    """
    n = len(arr) + 1
    xor_all = 0
    for i in range(1, n + 1):
        xor_all ^= i
    for num in arr:
        xor_all ^= num
    return xor_all


def find_missing_number_hash(arr):
    """
    Hashset approach — O(n) time, O(n) space.
    """
    num_set = set(arr)
    n = len(arr) + 1
    for i in range(1, n + 1):
        if i not in num_set:
            return i
    return -1


if __name__ == "__main__":
    import unittest

    class TestFindMissingNumber(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(find_missing_number([1, 2, 4, 5]), 3)

        def test_first_missing(self):
            self.assertEqual(find_missing_number([2, 3, 4, 5]), 1)

        def test_last_missing(self):
            self.assertEqual(find_missing_number([1, 2, 3, 4]), 5)

    # Demo
    demo = [1, 2, 4, 5]
    print(f"Input: {demo}")
    print(f"Missing number: {find_missing_number(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
