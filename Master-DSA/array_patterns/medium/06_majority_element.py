# 📘 Array Patterns — Medium 06
# Topic: Hashing / Moore's Voting — Majority Element
# Approach: Moore's Voting Algorithm (O(1) space) or hashmap
# Time: O(n) | Space: O(1)

def majority_element(arr):
    """
    Returns the majority element (appears > n/2 times).
    Uses Moore's Voting Algorithm — O(n) time, O(1) space.
    """
    candidate = None
    count = 0

    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    # Verify the candidate (in case no majority exists)
    if arr.count(candidate) > len(arr) // 2:
        return candidate
    return None


def majority_element_hashmap(arr):
    """
    Hashmap approach — O(n) time, O(n) space.
    """
    freq = {}
    n = len(arr)
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
        if freq[num] > n // 2:
            return num
    return None


def majority_element_brute(arr):
    """
    Brute force: count each element's frequency.
    """
    n = len(arr)
    for num in arr:
        if arr.count(num) > n // 2:
            return num
    return None


if __name__ == "__main__":
    import unittest

    class TestMajorityElement(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(majority_element([3, 2, 3]), 3)

        def test_no_majority(self):
            self.assertIsNone(majority_element([1, 2, 3]))

        def test_majority_at_end(self):
            self.assertEqual(majority_element([1, 1, 2, 2, 2]), 2)

    # Demo
    demo = [3, 2, 3]
    print(f"Input: {demo}")
    print(f"Majority element: {majority_element(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
