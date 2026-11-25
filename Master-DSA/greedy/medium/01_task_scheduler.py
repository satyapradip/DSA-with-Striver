# 📘 Greedy Algorithms (Medium 01)
# Topic: Task Scheduler — Priority Queue Greedy
# Approach: Max heap with cooldown
# Time: O(n log n) | Space: O(n)

import heapq
from collections import Counter, deque

def least_interval(tasks, n):
    """
    Find minimum intervals to complete all tasks with cooldown n.
    Tasks of same type must be separated by at least n intervals.
    """
    if n == 0:
        return len(tasks)

    # Count task frequencies
    freq = Counter(tasks)
    max_freq = max(freq.values())
    max_count = sum(1 for v in freq.values() if v == max_freq)

    # Formula: (max_freq - 1) * (n + 1) + max_count
    result = (max_freq - 1) * (n + 1) + max_count
    return max(result, len(tasks))


def least_interval_pq(tasks, n):
    """
    Priority Queue approach for Task Scheduler.
    """
    if n == 0:
        return len(tasks)

    freq = Counter(tasks)
    max_heap = [-count for count in freq.values()]
    heapq.heapify(max_heap)

    time = 0
    queue = deque()  # Stores (count, available_time)

    while max_heap or queue:
        time += 1

        if max_heap:
            count = heapq.heappop(max_heap) + 1  # Add 1 because negative
            if count < 0:
                queue.append((count, time + n))

        if queue and queue[0][1] == time:
            heapq.heappush(max_heap, queue.popleft()[0])

    return time


if __name__ == "__main__":
    import unittest

    class TestTaskScheduler(unittest.TestCase):
        def test_least_interval(self):
            self.assertEqual(least_interval(["A", "A", "A", "B", "B", "B"], 2), 8)
            self.assertEqual(least_interval(["A", "A", "A", "B", "B", "B"], 0), 6)
            self.assertEqual(least_interval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2), 16)

        def test_least_interval_pq(self):
            self.assertEqual(least_interval_pq(["A", "A", "A", "B", "B", "B"], 2), 8)
            self.assertEqual(least_interval_pq(["A", "A", "A", "B", "B", "B"], 0), 6)

    # Demo
    demo_tasks = ["A", "A", "A", "B", "B", "B"]
    demo_n = 2
    print(f"Tasks: {demo_tasks}, Cooldown: {demo_n}")
    print(f"Minimum intervals: {least_interval(demo_tasks, demo_n)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)