# 📘 Greedy Algorithms (Medium 03)
# Topic: Merge Intervals
# Approach: Sort by start time, merge overlapping
# Time: O(n log n) | Space: O(n)

def merge(intervals):
    """
    Merge all overlapping intervals.
    """
    if not intervals:
        return []

    # Sort by start time
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]

        if current[0] <= last[1]:
            # Overlapping - merge
            merged[-1][1] = max(last[1], current[1])
        else:
            # Non-overlapping - add new interval
            merged.append(current)

    return merged


def merge_brute(intervals):
    """
    Brute force: O(n²) time.
    Check all pairs for overlap.
    """
    if not intervals:
        return []

    result = []
    used = [False] * len(intervals)

    for i in range(len(intervals)):
        if used[i]:
            continue

        start, end = intervals[i]
        used[i] = True

        # Find all overlapping intervals
        changed = True
        while changed:
            changed = False
            for j in range(len(intervals)):
                if not used[j]:
                    s, e = intervals[j]
                    if s <= end and e >= start:  # Overlapping
                        start = min(start, s)
                        end = max(end, e)
                        used[j] = True
                        changed = True

        result.append([start, end])

    return result


if __name__ == "__main__":
    import unittest

    class TestMergeIntervals(unittest.TestCase):
        def test_merge(self):
            self.assertEqual(merge([[1, 3], [2, 6], [8, 10], [15, 18]]), [[1, 6], [8, 10], [15, 18]])
            self.assertEqual(merge([[1, 4], [4, 5]]), [[1, 5]])
            self.assertEqual(merge([]), [])
            self.assertEqual(merge([[1, 4], [2, 3]]), [[1, 4]])

        def test_merge_brute(self):
            self.assertEqual(merge_brute([[1, 3], [2, 6], [8, 10], [15, 18]]), [[1, 6], [8, 10], [15, 18]])
            self.assertEqual(merge_brute([[1, 4], [4, 5]]), [[1, 5]])

    # Demo
    demo = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(f"Intervals: {demo}")
    print(f"Merged: {merge(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)