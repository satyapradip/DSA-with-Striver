# 📘 Stacks & Queues — Easy 01
# Topic: Stack Basics — Valid Parentheses
# Approach: Stack (LIFO) — match closing bracket with top of stack
# Time: O(n) | Space: O(n)

def is_valid(s):
    """
    Returns True if the input string has valid parentheses.
    A string is valid if:
    - Open brackets are closed by the same type of brackets
    - Open brackets are closed in the correct order
    """
    # Mapping of closing to opening brackets
    mapping = {')': '(', '}': '{', ']': '['}
    stack = []

    for ch in s:
        if ch in mapping:
            # It's a closing bracket
            if not stack or stack.pop() != mapping[ch]:
                return False
        else:
            # It's an opening bracket
            stack.append(ch)

    return len(stack) == 0


if __name__ == "__main__":
    import unittest

    class TestValidParentheses(unittest.TestCase):
        def test_basic_valid(self):
            self.assertTrue(is_valid("()"))
            self.assertTrue(is_valid("()[]{}"))
            self.assertTrue(is_valid("([])"))

        def test_invalid(self):
            self.assertFalse(is_valid("(]"))
            self.assertFalse(is_valid("([)]"))
            self.assertFalse(is_valid("(("))

        def test_empty(self):
            self.assertTrue(is_valid(""))

    # Demo
    demo = "()[]{}"
    print(f"Input: {demo}")
    print(f"Valid: {is_valid(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
