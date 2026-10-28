# 📘 Binary Search — Advanced Medium 04
# Topic: Binary Search on Answer — Painter's Partition
# Approach: Search the max time answer
# Time: O(n log(max_time))
# Space: O(1)

def painters_partition(times, k):
    """
    Returns the minimum time to paint all boards with k painters.
    Each painter paints contiguous boards.
    """
    def can_paint(max_time):
        painters = 1
        current_time = 0
        for time in times:
            if current_time + time > max_time:
                painters += 1
                current_time = time
                if painters > k:
                    return False
            else:
                current_time += time
        return True

    if k > len(times):
        return -1

    low, high = max(times), sum(times)
    while low < high:
        mid = (low + high) // 2
        if can_paint(mid):
            high = mid
        else:
            low = mid + 1
    return low


def painters_partition_brute(times, k):
    """
    Brute force: check each possible max time from max(times) to sum(times).
    """
    for max_time in range(max(times), sum(times) + 1):
        painters = 1
        current_time = 0
        for time in times:
            if current_time + time > max_time:
                painters += 1
                current_time = time
                if painters > k:
                    break
            else:
                current_time += time
        if painters <= k:
            return max_time
    return -1


if __name__ == "__main__":
    import unittest

    class TestPaintersPartition(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(painters_partition([10, 20, 30, 40], 2), 60)

        def test_single_painter(self):
            self.assertEqual(painters_partition([10, 20, 30, 40], 4), 40)

        def test_single_board(self):
            self.assertEqual(painters_partition([5], 1), 5)

    # Demo
    demo_times = [10, 20, 30, 40]
    demo_k = 2
    print(f"Painting times: {demo_times}, painters: {demo_k}")
    print(f"Min max time: {painters_partition(demo_times, demo_k)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
