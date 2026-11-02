# 📘 Stacks & Queues — Medium 02
# Topic: Monotonic Stack — Nearest Greater Element to Left
# Approach: Monotonic decreasing stack
# Time: O(n) | Space: O(n)

def previous_greater_element(nums):
    """
    Returns an array where each element is the nearest greater element to its left.
    If no greater element exists, returns -1.
    Uses a strictly decreasing monotonic stack.
    """
    n = len(nums)
    result = [-1] * n
    stack = []  # stores indices, maintaining strictly decreasing values

    for i in range(n):
        # While stack is not empty and current >= stack top's value
        # Pop elements that are <= current (they can't be "greater")
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()
        # Stack top is the nearest greater element to the left
        if stack:
            result[i] = nums[stack[-1]]
        stack.append(i)

    return result


def previous_greater_element_index(nums):
    """
    Returns an array where each element is the index of the nearest greater element to its left.
    """
    n = len(nums)
    result = [-1] * n
    stack = []

    for i in range(n):
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(i)

    return result


def previous_greater_element_brute(nums):
    """
    Brute force: O(n^2) — check each element's left side.
    """
    n = len(nums)
    result = [-1] * n
    for i in range(n):
        for j in range(i - 1, -1, -1):
            if nums[j] > nums[i]:
                result[i] = nums[j]
                break
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


if __name__ == "__main__":
    import unittest

    class TestPreviousGreaterElement(unittest.TestCase):
        def test_basic(self):
            # [4, 5, 2, 10]
            # 4: no greater to left → -1 (it's the first element)
            # 5: nearest greater to left → 4 (since 5 > 4, but 4 is the only left element)
            # Wait, let me trace through the algorithm:
            # i=0, val=4: stack empty → result[0]=-1, push 0
            # i=1, val=5: stack=[0], nums[0]=4 <= 5 → pop, stack empty → result[1]=-1, push 1
            # i=2, val=2: stack=[1], nums[1]=5 > 2 → result[2]=5, push 2
            # i=3, val=10: stack=[1], nums[1]=5 <= 10 → pop, stack empty → result[3]=-1, push 3
            # Result: [-1, -1, 5, -1]
            self.assertEqual(previous_greater_element([4, 5, 2, 10]), [-1, -1, 5, -1])

        def test_no_greater(self):
            # [1, 2, 3, 4] is strictly increasing
            # Each element has a smaller element to its left
            # 1: -1 (no elements to the left)
            # 2: left elements: 1. 1 < 2, no greater → -1
            # 3: left elements: 1, 2. Neither > 3 → -1
            # 4: left elements: 1, 2, 3. None > 4 → -1
            self.assertEqual(previous_greater_element([1, 2, 3, 4]), [-1, -1, -1, -1])

        def test_all_decreasing(self):
            # [4, 3, 2, 1]
            # 4: -1
            # 3: nearest greater to left = 4
            # 2: nearest greater to left = 3 (not 4, since 3 > 2 and is closer)
            # 1: nearest greater to left = 2 (not 3, since 2 > 1 and is closer)
            self.assertEqual(previous_greater_element([4, 3, 2, 1]), [-1, 4, 3, 2])

        def test_equal_elements(self):
            # [3, 3, 3]
            # All equal, no strictly greater element
            self.assertEqual(previous_greater_element([3, 3, 3]), [-1, -1, -1])

        def test_full_example(self):
            # [3, 5, 2, 8, 1]
            # 3: -1
            # 5: greater to left → 3? No, 5 > 3, so nearest greater = 4? No, we want the NEAREST greater.
            # For 5 (idx 1): left elements: 3 (idx 0). 3 < 5, so no greater element → -1
            # For 2 (idx 2): left elements: 5 (idx 1), 3 (idx 0). 5 > 2, nearest greater = 5
            # For 8 (idx 3): left: 2, 5, 3. None > 8 → -1
            # For 1 (idx 4): left: 8, 2, 5, 3. 8 > 1, nearest greater = 8
            self.assertEqual(previous_greater_element([3, 5, 2, 8, 1]), [-1, -1, 5, -1, 8])

        def test_example_from_scratch(self):
            # [5, 4, 3, 2, 1]
            # 5: -1
            # 4: nearest greater to left → 5
            # 3: nearest greater to left → 4 (not 5, since 4 > 3 and is closer)
            # 2: nearest greater to left → 3
            # 1: nearest greater to left → 2
            self.assertEqual(previous_greater_element([5, 4, 3, 2, 1]), [-1, 5, 4, 3, 2])

    # Demo
    demo = [4, 5, 2, 10]
    print(f"Input: {demo}")
    print(f"Previous Greater Elements: {previous_greater_element(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)