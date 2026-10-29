# 📘 Recursion — Medium 02
# Topic: Backtracking — Combination Sum
# Approach: Backtracking (choose → recurse → unchoose)
# Time: O(2^target) | Space: O(target)
# Note: Each number may be used unlimited times.

def combination_sum(candidates, target):
    """
    Finds all unique combinations in candidates where the candidate numbers sum to target.
    Each number may be used unlimited times.
    """
    def backtrack(start, remaining, combo, results):
        if remaining == 0:
            results.append(list(combo))
            return
        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            # Choose: include candidates[i]
            combo.append(candidates[i])
            # Explore: same starting index (can reuse same number)
            backtrack(i, remaining - candidates[i], combo, results)
            # Unchoose: remove candidates[i] to try next candidate
            combo.pop()

    candidates.sort()
    results = []
    backtrack(0, target, [], results)
    return results


def combination_sum_unique(candidates, target):
    """
    Same as above, but each number can only be used ONCE.
    """
    def backtrack(start, remaining, combo, results):
        if remaining == 0:
            results.append(list(combo))
            return
        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            # Skip duplicates to avoid duplicate combinations
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            combo.append(candidates[i])
            backtrack(i + 1, remaining - candidates[i], combo, results)
            combo.pop()

    candidates.sort()
    results = []
    backtrack(0, target, [], results)
    return results


if __name__ == "__main__":
    import unittest

    class TestCombinationSum(unittest.TestCase):
        def test_basic(self):
            result = combination_sum([2, 3, 6, 7], 7)
            self.assertEqual(len(result), 2)
            self.assertIn([2, 2, 3], result)
            self.assertIn([7], result)

        def test_unique(self):
            result = combination_sum_unique([10, 1, 2, 7, 6, 1, 5], 8)
            self.assertEqual(len(result), 4)
            # Check each combination sums to 8
            for combo in result:
                self.assertEqual(sum(combo), 8)

    # Demo
    demo_candidates = [2, 3, 6, 7]
    demo_target = 7
    print(f"Combination Sum: candidates={demo_candidates}, target={demo_target}")
    solutions = combination_sum(demo_candidates, demo_target)
    for i, sol in enumerate(solutions):
        print(f"Solution {i + 1}: {sol}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
