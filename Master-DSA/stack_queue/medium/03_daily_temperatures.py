# 📘 Stack & Queue (Medium 03)
# Topic: Daily Temperatures - Monotonic Stack
# Approach: Monotonic decreasing stack
# Time: O(n) | Space: O(n)

def daily_temperatures(temperatures):
    """
    Daily Temperatures: For each day, find how many days until a warmer temperature.
    """
    n = len(temperatures)
    result = [0] * n
    stack = []  # Monotonic decreasing stack: stores indices with decreasing temps

    for i, temp in enumerate(temperatures):
        # While stack is not empty and current temp is warmer than stack top
        while stack and temperatures[stack[-1]] < temp:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index
        stack.append(i)

    return result


def next_greater_element(nums):
    """
    Next Greater Element: For each element, find the next greater element.
    """
    n = len(nums)
    result = [-1] * n
    stack = []  # Monotonic decreasing stack

    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            result[stack.pop()] = nums[i]
        stack.append(i)

    return result


if __name__ == "__main__":
    import unittest

    class TestDailyTemperatures(unittest.TestCase):
        def test_daily_temperatures(self):
            self.assertEqual(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]), [1, 1, 4, 2, 1, 1, 0, 0])
            self.assertEqual(daily_temperatures([30, 40, 50, 60]), [1, 1, 1, 0])
            self.assertEqual(daily_temperatures([30, 60, 90]), [1, 1, 0])

        def test_next_greater_element(self):
            self.assertEqual(next_greater_element([4, 5, 2, 25]), [5, 25, 25, -1])
            self.assertEqual(next_greater_element([13, 7, 6, 12]), [-1, 12, 12, -1])
            self.assertEqual(next_greater_element([1, 2, 3, 4]), [2, 3, 4, -1])

    # Demo
    print("Daily Temperatures:")
    print(f"Temperatures [73,74,75,71,69,72,76,73]: {daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73])}")
    print("Next Greater Element:")
    print(f"[4,5,2,25]: {next_greater_element([4, 5, 2, 25])}")
    print("Running unit tests...")
    unittest.main(verbosity=0)