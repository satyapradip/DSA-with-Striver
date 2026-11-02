# 📘 Stacks & Queues — Medium 01
# Topic: Monotonic Stack — Next Greater Element
# Approach: Monotonic decreasing stack
# Time: O(n) | Space: O(n)

def next_greater_element(nums):
    """
    Returns an array where each element is the next greater element to its right.
    If no greater element exists, returns -1.
    """
    n = len(nums)
    result = [-1] * n
    stack = []  # stores indices, maintaining decreasing order of values

    for i in range(n):
        # While stack is not empty and current element > stack top's value
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)

    return result


def next_greater_element_indices(nums):
    """
    Returns an array where each element is the index of the next greater element.
    """
    n = len(nums)
    result = [-1] * n
    stack = []  # stores indices

    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            result[idx] = i
        stack.append(i)

    return result


def next_greater_element_brute(nums):
    """
    Brute force: O(n^2) — check each element's right side.
    """
    n = len(nums)
    result = [-1] * n
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                result[i] = nums[j]
                break
    return result


if __name__ == "__main__":
    import unittest

    class TestNextGreaterElement(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(next_greater_element([4, 5, 2, 10]), [5, 10, 10, -1])

        def test_no_greater(self):
            self.assertEqual(next_greater_element([5, 4, 3, 2, 1]), [-1, -1, -1, -1, -1])

        def test_all_increasing(self):
            self.assertEqual(next_greater_element([1, 2, 3, 4]), [2, 3, 4, -1])

    # Demo
    demo = [4, 5, 2, 10]
    print(f"Input: {demo}")
    print(f"Next Greater Elements: {next_greater_element(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
