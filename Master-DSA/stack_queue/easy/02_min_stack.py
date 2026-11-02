# 📘 Stacks & Queues — Easy 02
# Topic: Stack Basics — Min Stack
# Approach: Two stacks — main stack + min stack
# Time: O(1) for all operations | Space: O(n)

class MinStack:
    """
    Design a stack that supports push, pop, top, and retrieving the minimum element in O(1) time.
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        """
        Push element val onto stack.
        """
        self.stack.append(val)
        # Only push to min_stack if it's empty or val is smaller or equal
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        """
        Remove the top element from stack.
        """
        if self.stack:
            top = self.stack.pop()
            # If popped element is the current minimum, pop from min_stack too
            if top == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        """
        Retrieve the minimum element in the stack.
        """
        return self.min_stack[-1] if self.min_stack else None


class MinStackBrute:
    """
    Brute force version using a single stack with extra scanning for min.
    """

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return min(self.stack) if self.stack else None


if __name__ == "__main__":
    import unittest

    class TestMinStack(unittest.TestCase):
        def test_min_stack(self):
            min_stack = MinStack()
            min_stack.push(-2)
            min_stack.push(0)
            min_stack.push(-3)
            self.assertEqual(min_stack.getMin(), -3)  # Returns -3
            min_stack.pop()
            self.assertEqual(min_stack.top(), 0)
            self.assertEqual(min_stack.getMin(), -2)

    # Demo
    print("Min Stack Demo:")
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print(f"Push -2, 0, -3")
    print(f"Get Min: {min_stack.getMin()}")
    min_stack.pop()
    print(f"After pop, Top: {min_stack.top()}, Min: {min_stack.getMin()}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
