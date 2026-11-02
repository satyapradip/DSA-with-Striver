# 📘 Stacks & Queues — Hard 03
# Topic: Queue / Priority Queue — Task Scheduler
# Approach: Greedy with max-heap + cooldown simulation
# Time: O(n log n) | Space: O(n)

import heapq
from collections import deque, Counter

def task_scheduler(tasks, n):
    """
    Returns the minimum number of intervals to complete all tasks.
    Each task takes 1 unit of time.
    There must be at least n intervals between same tasks.
    """
    # Count task frequencies
    task_counts = Counter(tasks)

    # Max heap to get most frequent tasks first
    max_heap = []
    for task, count in task_counts.items():
        heapq.heappush(max_heap, -count)  # Negative for max heap

    # Queue for tasks waiting for cooldown
    cooldown_queue = deque()

    time = 0

    while max_heap or cooldown_queue:
        # If we have a task to execute
        if max_heap:
            # Execute the most frequent task
            count = heapq.heappop(max_heap)
            count += 1  # Decrement frequency

            # If task still has remaining executions, add to cooldown queue
            if count < 0:
                cooldown_queue.append((count, time + n))

        # If the queue is not empty, check if cooldown has expired
        if cooldown_queue and cooldown_queue[0][1] <= time:
            # Add back to max heap
            remaining_time, _ = cooldown_queue.popleft()
            heapq.heappush(max_heap, remaining_time)

        time += 1

    return time


def task_scheduler_brute(tasks, n):
    """
    Brute force simulation of task scheduling.
    """
    if not tasks:
        return 0

    # Count frequencies
    from collections import Counter
    task_counts = Counter(tasks)
    tasks = list(task_counts.keys())
    counts = [task_counts[t] for t in tasks]
    n_tasks = len(tasks)
    current_time = 0

    while True:
        # Find the most frequent task that can be executed
        max_count = 0
        max_idx = -1
        found = False

        for i in range(n_tasks):
            if counts[i] > 0:
                # Check if we can execute this task (no cooldown or first execution)
                can_execute = False
                if counts[i] >= max_count:
                    can_execute = True
                    max_idx = i
                    max_count = counts[i]

        if max_idx == -1:
            break

        counts[max_idx] -= 1
        current_time += 1

    return current_time


if __name__ == "__main__":
    import unittest

    class TestTaskScheduler(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(task_scheduler(["A", "A", "A", "B", "B", "B"], 2), 8)

        def test_no_cooldown(self):
            self.assertEqual(task_scheduler(["A", "A", "A"], 0), 3)

        def test_single_task(self):
            self.assertEqual(task_scheduler(["A"], 1), 1)

        def test_all_different(self):
            self.assertEqual(task_scheduler(["A", "B", "C", "D"], 2), 4)

    # Demo
    demo_tasks = ["A", "A", "A", "B", "B", "B"]
    demo_n = 2
    print(f"Tasks: {demo_tasks}, cooldown: {demo_n}")
    print(f"Minimum intervals: {task_scheduler(demo_tasks, demo_n)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
