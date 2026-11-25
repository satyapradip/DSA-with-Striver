# 📘 Greedy Algorithms (Hard 01)
# Topic: Jump Game II — Forward Greedy
# Approach: Greedy reach forward with BFS-like levels
# Time: O(n) | Space: O(1)

def jump(nums):
    """
    Find minimum jumps to reach the last index.
    Each element represents max jump length from that position.
    """
    if len(nums) <= 1:
        return 0

    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])

        if i == current_end:
            # Reached end of current level
            jumps += 1
            current_end = farthest

            if current_end >= len(nums) - 1:
                break

    return jumps


def jump_brute(nums):
    """
    Brute force: O(n²) time.
    Try all possible jumps from each position.
    """
    from functools import lru_cache

    @lru_cache(None)
    def min_jumps_from(idx):
        if idx >= len(nums) - 1:
            return 0

        min_jumps = float('inf')
        for step in range(1, nums[idx] + 1):
            jumps = min_jumps_from(idx + step)
            if jumps != float('inf'):
                min_jumps = min(min_jumps, jumps + 1)

        return min_jumps

    return min_jumps_from(0)


if __name__ == "__main__":
    import unittest

    class TestJumpGameII(unittest.TestCase):
        def test_jump(self):
            self.assertEqual(jump([2, 3, 1, 1, 4]), 2)
            self.assertEqual(jump([2, 3, 0, 1, 4]), 2)
            self.assertEqual(jump([0]), 0)
            self.assertEqual(jump([1]), 0)
            self.assertEqual(jump([1, 2, 3]), 2)

        def test_jump_brute(self):
            self.assertEqual(jump_brute([2, 3, 1, 1, 4]), 2)
            self.assertEqual(jump_brute([2, 3, 0, 1, 4]), 2)

    # Demo
    demo = [2, 3, 1, 1, 4]
    print(f"Array: {demo}")
    print(f"Minimum jumps: {jump(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)