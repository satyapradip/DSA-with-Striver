# 📘 Stacks & Queues — Hard 01
# Topic: Monotonic Stack — Largest Rectangle in Histogram
# Approach: Monotonic increasing stack
# Time: O(n) | Space: O(n)

def largest_rectangle_area(heights):
    """
    Given an array of bar heights, returns the area of the largest rectangle in the histogram.
    Uses monotonic increasing stack to find previous/next smaller elements efficiently.
    """
    n = len(heights)
    result = 0

    # Add a 0-height bar at the end to force popping all remaining bars
    heights.append(0)
    stack = []  # stores indices, maintaining increasing order of heights

    for i in range(len(heights)):
        # While stack is not empty and current height < stack top's height
        while stack and heights[stack[-1]] > heights[i]:
            height = heights[stack.pop()]
            # Width: from stack top's index to current index (exclusive)
            width = i if not stack else i - stack[-1] - 1
            result = max(result, height * width)
        stack.append(i)

    heights.pop()  # Remove the 0 we added
    return result


def largest_rectangle_area_brute(heights):
    """
    Brute force: O(n^2) — for each bar, expand to find the area.
    """
    n = len(heights)
    result = 0

    for i in range(n):
        min_height = heights[i]
        for j in range(i, n):
            min_height = min(min_height, heights[j])
            result = max(result, min_height * (j - i + 1))

    return result


if __name__ == "__main__":
    import unittest

    class TestLargestRectangle(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(largest_rectangle_area([2, 1, 5, 6, 2, 3]), 10)

        def test_single_bar(self):
            self.assertEqual(largest_rectangle_area([1]), 1)

        def test_increasing(self):
            self.assertEqual(largest_rectangle_area([1, 2, 3, 4, 5]), 9)

        def test_decreasing(self):
            self.assertEqual(largest_rectangle_area([5, 4, 3, 2, 1]), 9)

        def test_all_same(self):
            self.assertEqual(largest_rectangle_area([2, 2, 2, 2]), 8)

    # Demo
    demo = [2, 1, 5, 6, 2, 3]
    print(f"Heights: {demo}")
    print(f"Largest Rectangle Area: {largest_rectangle_area(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
