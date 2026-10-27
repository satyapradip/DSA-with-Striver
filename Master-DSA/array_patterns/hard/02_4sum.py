# 📘 Array Patterns — Hard 02
# Topic: Two Pointers — 4Sum
# Approach: Sort + two pointers (O(n³) time)
# Note: Avoid duplicates by skipping equal elements

def four_sum(nums, target):
    """
    Finds all unique quadruplets [a, b, c, d] such that a + b + c + d = target.
    """
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # Early termination: smallest possible sum > target
        if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
            break
        # Prune: largest possible sum < target
        if nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
            continue

        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            # Early termination for inner loop
            if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                break
            if nums[i] + nums[j] + nums[n - 1] + nums[n - 2] < target:
                continue

            left, right = j + 1, n - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1

    return result


def four_sum_brute(nums, target):
    """
    Brute force: O(n⁴) — all quadruplets.
    """
    n = len(nums)
    result = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        result.add(tuple(sorted([nums[i], nums[j], nums[k], nums[l]])))
    return [list(quad) for quad in result]


if __name__ == "__main__":
    import unittest

    class TestFourSum(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(four_sum([1, 0, -1, 0, -2, 2], 0),
                             [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]])

        def test_no_solution(self):
            self.assertEqual(four_sum([2, 2], 0), [])

    # Demo
    demo = [1, 0, -1, 0, -2, 2]
    target = 0
    print(f"Input: {demo}, target = {target}")
    print(f"4Sum: {four_sum(demo, target)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
