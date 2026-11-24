# 📘 Stack & Queue (Easy 04)
# Topic: Valid Parentheses Variations
# Approach: Stack matching
# Time: O(n) | Space: O(n)

def is_valid_parentheses(s):
    """
    Check if a string of parentheses is valid.
    """
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()

    return len(stack) == 0


def longest_valid_parentheses(s):
    """
    Find the length of the longest valid (well-formed) parentheses substring.
    """
    stack = [-1]  # Initialize with -1 to handle edge cases
    max_len = 0

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_len = max(max_len, i - stack[-1])

    return max_len


def min_add_to_make_valid(s):
    """
    Find the minimum number of parentheses to add to make the string valid.
    """
    open_count = 0
    close_count = 0

    for char in s:
        if char == '(':
            open_count += 1
        elif char == ')':
            if open_count > 0:
                open_count -= 1
            else:
                close_count += 1

    return open_count + close_count


if __name__ == "__main__":
    import unittest

    class TestValidParenthesesVariations(unittest.TestCase):
        def test_is_valid_parentheses(self):
            self.assertTrue(is_valid_parentheses("()"))
            self.assertTrue(is_valid_parentheses("()[]{}"))
            self.assertTrue(is_valid_parentheses("{[]}"))
            self.assertFalse(is_valid_parentheses("(]"))
            self.assertFalse(is_valid_parentheses("([)]"))
            self.assertFalse(is_valid_parentheses("]"))

        def test_longest_valid_parentheses(self):
            self.assertEqual(longest_valid_parentheses("(()"), 2)
            self.assertEqual(longest_valid_parentheses(")()())"), 4)
            self.assertEqual(longest_valid_parentheses(""), 0)
            self.assertEqual(longest_valid_parentheses("()(()"), 2)

        def test_min_add_to_make_valid(self):
            self.assertEqual(min_add_to_make_valid("())"), 1)
            self.assertEqual(min_add_to_make_valid("((("), 3)
            self.assertEqual(min_add_to_make_valid("()"), 0)
            self.assertEqual(min_add_to_make_valid("()))(("), 4)

    # Demo
    print("Valid Parentheses Tests:")
    print(f"() -> {is_valid_parentheses('()')}")
    print(f"(] -> {is_valid_parentheses('(]')}")
    print(f"Longest valid in '(()': {longest_valid_parentheses('(()')}")
    print(f"Min add for '())': {min_add_to_make_valid('())')}")
    print("Running unit tests...")
    unittest.main(verbosity=0)