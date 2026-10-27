# 📘 Array Patterns — Hard 01
# Topic: Two Pointers — 3Sum
# Approach: Sort + two pointers (O(n²) time, O(1) space)
# Note: Avoid duplicates by skipping equal elements

def three_sum(nums):
    """
    Finds all unique triplets [a, b, c] such that a + b + c = 0.
    """
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n - 2):
        # Skip duplicates for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # Early termination: if smallest number > 0, no solution
        if nums[i] > 0:
            break

        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                # Skip duplicates for the second and third elements
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result


def three_sum_brute(nums):
    """
    Brute force: O(n³) — all triplets.
    """
    n = len(nums)
    result = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    result.add(tuple(sorted([nums[i], nums[j], nums[k]])))
    return [list(triplet) for triplet in result]


if __name__ == "__main__":
    import unittest

    class TestThreeSum(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(three_sum([-1, 0, 1, 2, -1, -4]),
                             [[-1, -1, 2], [-1, 0, 1]])

        def test_no_solution(self):
            self.assertEqual(three_sum([1, 2, 3]), [])

        def test_all_zeros(self):
            self.assertEqual(three_sum([0, 0, 0, 0]), [[0, 0, 0]])

    # Demo
    demo = [-1, 0, 1, 2, -1, -4]
    print(f"Input: {demo}")
    print(f"3Sum: {three_sum(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
