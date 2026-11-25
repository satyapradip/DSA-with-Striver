# 📘 Greedy Algorithms (Medium 02)
# Topic: Non-overlapping Intervals
# Approach: Sort by end time, pick greedily
# Time: O(n log n) | Space: O(1)

def erase_overlap_intervals(intervals):
    """
    Find minimum intervals to remove to make rest non-overlapping.
    """
    if not intervals:
        return 0

    # Sort by end time
    intervals.sort(key=lambda x: x[1])

    count = 0
    prev_end = intervals[0][1]

    for i in range(1, len(intervals)):
        if intervals[i][0] < prev_end:
            # Overlapping - need to remove one
            count += 1
        else:
            # Non-overlapping - update prev_end
            prev_end = intervals[i][1]

    return count


def erase_overlap_intervals_brute(intervals):
    """
    Brute force: Try all combinations.
    """
    def can_remove(idx, intervals, removed_count):
        # Check if remaining intervals are non-overlapping
        remaining = [intervals[i] for i in range(len(intervals)) if i not in removed_count]
        remaining.sort(key=lambda x: x[0])
        for i in range(1, len(remaining)):
            if remaining[i][0] < remaining[i - 1][1]:
                return False
        return True

    # Try removing 0, 1, 2, ... intervals
    for k in range(len(intervals) + 1):
        from itertools import combinations
        for combo in combinations(range(len(intervals)), k):
            if can_remove(0, intervals, set(combo)):
                return k

    return len(intervals)


if __name__ == "__main__":
    import unittest

    class TestNonOverlappingIntervals(unittest.TestCase):
        def test_erase_overlap_intervals(self):
            self.assertEqual(erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]), 1)
            self.assertEqual(erase_overlap_intervals([[1, 2], [1, 2], [1, 2]]), 2)
            self.assertEqual(erase_overlap_intervals([[1, 2], [2, 3]]), 0)
            self.assertEqual(erase_overlap_intervals([]), 0)

        def test_erase_overlap_intervals_brute(self):
            self.assertEqual(erase_overlap_intervals_brute([[1, 2], [2, 3], [3, 4], [1, 3]]), 1)
            self.assertEqual(erase_overlap_intervals_brute([[1, 2], [1, 2], [1, 2]]), 2)

    # Demo
    demo = [[1, 2], [2, 3], [3, 4], [1, 3]]
    print(f"Intervals: {demo}")
    print(f"Minimum to remove: {erase_overlap_intervals(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)