# 📘 Recursion — Medium 03
# Topic: Backtracking — Subset Sum
# Approach: Backtracking (choose → recurse → unchoose)
# Time: O(2^n) | Space: O(n)

def subset_sum(nums, target):
    """
    Finds all unique subsets of nums that sum to target.
    """
    def backtrack(start, remaining, subset, results):
        if remaining == 0:
            results.append(list(subset))
            return
        if remaining < 0:
            return

        for i in range(start, len(nums)):
            # Skip duplicates to avoid duplicate subsets
            if i > start and nums[i] == nums[i - 1]:
                continue
            subset.append(nums[i])
            backtrack(i + 1, remaining - nums[i], subset, results)
            subset.pop()

    nums.sort()
    results = []
    backtrack(0, target, [], results)
    return results


def subset_sum_unique(nums, target):
    """
    Finds all unique subsets (any size) that sum to target.
    Handles duplicates in the input array.
    """
    def backtrack(index, remaining, subset, results):
        if remaining == 0:
            results.append(list(subset))
            return

        for i in range(index, len(nums)):
            # Skip duplicates
            if i > index and nums[i] == nums[i - 1]:
                continue
            subset.append(nums[i])
            backtrack(i + 1, remaining - nums[i], subset, results)
            subset.pop()  # Backtrack

    nums.sort()
    results = []
    backtrack(0, target, [], results)
    return results


def subset_sum_brute(nums, target):
    """
    Brute force: all subsets using bitmask.
    """
    n = len(nums)
    result = []
    for mask in range(1 << n):
        subset = []
        total = 0
        for i in range(n):
            if mask & (1 << i):
                subset.append(nums[i])
                total += nums[i]
        if total == target:
            result.append(subset)
    return result


if __name__ == "__main__":
    import unittest

    class TestSubsetSum(unittest.TestCase):
        def test_basic(self):
            result = subset_sum([1, 2, 3, 4, 5], 5)
            self.assertEqual(len(result), 3)
            # Check each subset sums to 5
            for subset in result:
                self.assertEqual(sum(subset), 5)

        def test_unique(self):
            # With input [4, 4, 4, 4] and target=4, we can only use ONE 4
            # so there should be 1 unique subset (not 4)
            result = subset_sum_unique([4, 4, 4, 4], 4)
            self.assertEqual(len(result), 1)

    # Demo
    demo_nums = [1, 2, 3, 4, 5]
    demo_target = 5
    print(f"Subset Sum: nums={demo_nums}, target={demo_target}")
    solutions = subset_sum(demo_nums, demo_target)
    for i, sol in enumerate(solutions):
        print(f"Solution {i + 1}: {sol}")
    print("Running unit tests...")
    unittest.main(verbosity=0)