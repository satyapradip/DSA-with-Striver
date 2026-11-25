# 📘 Greedy Algorithms (Easy 03)
# Topic: Boyer-Moore Voting Algorithm
# Approach: Cancel pairs, remaining element is candidate
# Time: O(n) | Space: O(1)

def majority_element(nums):
    """
    Find the majority element (appears more than n/2 times).
    Boyer-Moore Voting Algorithm.
    """
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


def majority_element_verify(nums, candidate):
    """
    Verify if candidate is actually majority (appears more than n/2 times).
    """
    count = sum(1 for num in nums if num == candidate)
    return count > len(nums) // 2


def majority_element_brute(nums):
    """
    Brute force: O(n²) time.
    Count occurrences of each element.
    """
    for num in nums:
        count = sum(1 for x in nums if x == num)
        if count > len(nums) // 2:
            return num

    return None


if __name__ == "__main__":
    import unittest

    class TestMajorityElement(unittest.TestCase):
        def test_majority_element(self):
            self.assertEqual(majority_element([3, 2, 3]), 3)
            self.assertEqual(majority_element([2, 2, 1, 1, 1, 2, 2]), 2)
            self.assertEqual(majority_element([1]), 1)

        def test_majority_element_verify(self):
            self.assertTrue(majority_element_verify([3, 2, 3], 3))
            self.assertFalse(majority_element_verify([1, 2, 3], 2))

        def test_majority_element_brute(self):
            self.assertEqual(majority_element_brute([3, 2, 3]), 3)
            self.assertEqual(majority_element_brute([2, 2, 1, 1, 1, 2, 2]), 2)

    # Demo
    demo = [2, 2, 1, 1, 1, 2, 2]
    candidate = majority_element(demo)
    print(f"Array: {demo}")
    print(f"Majority candidate: {candidate}")
    print(f"Is majority? {majority_element_verify(demo, candidate)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)