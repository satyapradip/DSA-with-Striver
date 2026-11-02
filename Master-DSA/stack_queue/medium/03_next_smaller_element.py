# 📘 Stacks & Queues — Medium 03
# Topic: Monotonic Stack — Next Smaller Element
# Approach: Monotonic increasing stack
# Time: O(n) | Space: O(n)

def next_smaller_element(nums):
    """
    Returns an array where each element is the next smaller element to its right.
    If no smaller element exists, returns -1.
    Uses a strictly increasing monotonic stack.
    """
    n = len(nums)
    result = [-1] * n
    stack = []  # stores indices, maintaining increasing order of values

    for i in range(n):
        # While stack is not empty and current < stack top's value
        while stack and nums[stack[-1]] > nums[i]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)

    return result


def next_smaller_element_index(nums):
    """
    Returns an array where each element is the index of the next smaller element.
    """
    n = len(nums)
    result = [-1] * n
    stack = []

    for i in range(n):
        while stack and nums[stack[-1]] > nums[i]:
            idx = stack.pop()
            result[idx] = i
        stack.append(i)

    return result


def next_greater_element(nums):
    """
    Returns an array where each element is the next greater element to its right.
    """
    n = len(nums)
    result = [-1] * n
    stack = []

    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)

    return result


def previous_greater_element(nums):
    """
    Returns an array where each element is the nearest greater element to its left.
    """
    n = len(nums)
    result = [-1] * n
    stack = []

    for i in range(n):
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()
        if stack:
            result[i] = nums[stack[-1]]
        stack.append(i)

    return result


if __name__ == "__main__":
    import unittest

    class TestNextSmallerElement(unittest.TestCase):
        def test_basic(self):
            # [4, 5, 2, 10]
            # 4: next smaller → 2
            # 5: next smaller → 2
            # 2: no smaller to right → -1
            # 10: no smaller to right → -1
            self.assertEqual(next_smaller_element([4, 5, 2, 10]), [2, 2, -1, -1])

        def test_all_increasing(self):
            # [1, 2, 3, 4]
            # For increasing arrays, there's no next SMALLER element
            # 1: next smaller → -1 (2 > 1, not smaller)
            # 2: next smaller → -1
            # 3: next smaller → -1
            # 4: -1 (no elements to the right)
            self.assertEqual(next_smaller_element([1, 2, 3, 4]), [-1, -1, -1, -1])

        def test_mixed(self):
            # [3, 1, 4, 2]
            # 3: next smaller → 1
            # 1: no smaller to right → -1
            # 4: next smaller → 2
            # 2: -1 (no smaller to right)
            self.assertEqual(next_smaller_element([3, 1, 4, 2]), [1, -1, 2, -1])

        def test_decreasing_sequence(self):
            # [5, 4, 3, 2, 1] is strictly decreasing
            # Each element HAS a smaller element to its right
            # 5: next smaller → 4
            # 4: next smaller → 3
            # 3: next smaller → 2
            # 2: next smaller → 1
            # 1: -1 (no smaller to right)
            self.assertEqual(next_smaller_element([5, 4, 3, 2, 1]), [4, 3, 2, 1, -1])

    # Demo
    demo = [4, 5, 2, 10]
    print(f"Input: {demo}")
    print(f"Next Smaller Elements: {next_smaller_element(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)