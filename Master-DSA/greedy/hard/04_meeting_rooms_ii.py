# 📘 Greedy Algorithms (Hard 04)
# Topic: Meeting Rooms II — Priority Queue Greedy
# Approach: Sort by start time, use min heap for end times
# Time: O(n log n) | Space: O(n)

import heapq

def min_meeting_rooms(intervals):
    """
    Find minimum number of meeting rooms required.
    """
    if not intervals:
        return 0

    # Sort by start time
    intervals.sort(key=lambda x: x[0])

    # Min heap to track end times of ongoing meetings
    heap = []
    heapq.heappush(heap, intervals[0][1])

    for i in range(1, len(intervals)):
        # If current meeting starts after earliest ending meeting, reuse room
        if intervals[i][0] >= heap[0]:
            heapq.heappop(heap)

        # Add current meeting's end time
        heapq.heappush(heap, intervals[i][1])

    return len(heap)


def min_meeting_rooms_brute(intervals):
    """
    Brute force: O(n²) time.
    Count max overlapping intervals at any point.
    """
    if not intervals:
        return 0

    # Collect all start and end points
    points = []
    for start, end in intervals:
        points.append((start, 1))   # +1 for start
        points.append((end, -1))     # -1 for end

    # Sort by time, process ends before starts at same time
    points.sort(key=lambda x: (x[0], x[1]))

    max_rooms = 0
    current_rooms = 0

    for _, delta in points:
        current_rooms += delta
        max_rooms = max(max_rooms, current_rooms)

    return max_rooms


if __name__ == "__main__":
    import unittest

    class TestMeetingRoomsII(unittest.TestCase):
        def test_min_meeting_rooms(self):
            self.assertEqual(min_meeting_rooms([[0, 30], [5, 10], [15, 20]]), 2)
            self.assertEqual(min_meeting_rooms([[7, 10], [2, 4]]), 1)
            self.assertEqual(min_meeting_rooms([]), 0)
            self.assertEqual(min_meeting_rooms([[1, 5], [8, 9], [8, 9]]), 2)

        def test_min_meeting_rooms_brute(self):
            self.assertEqual(min_meeting_rooms_brute([[0, 30], [5, 10], [15, 20]]), 2)
            self.assertEqual(min_meeting_rooms_brute([[7, 10], [2, 4]]), 1)

    # Demo
    demo = [[0, 30], [5, 10], [15, 20]]
    print(f"Intervals: {demo}")
    print(f"Minimum rooms: {min_meeting_rooms(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)