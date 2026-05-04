# Maximum Nesting Depth of the Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine the maximum nesting depth of the parentheses in the string. The nesting depth is the maximum number of parentheses that are open at any time.
# Example 1:
# Input: s = "(1+(2*3)+((8)/4))+1"
# Output: 3

# Approach 1 : Use a counter to keep track of the current depth of the parentheses and update the maximum depth whenever we encounter an opening parenthesis.
def max_depth_of_parenthesis(s):
  current_depth = 0
  max_depth = 0

  for char in s:
    if char == "(":
      current_depth += 1
      max_depth = max(current_depth, max_depth)

    elif char == ")":
      current_depth -= 1
    
  return max_depth
# Time complexity: O(n) where n is the length of the string. We iterate through the string once.
# Space complexity: O(1) as we are using only a constant amount of extra space for the counters.

# Approach 2 : Use a stack to keep track of the opening parentheses and update the maximum depth whenever we encounter an opening parenthesis.
def max_depth_of_parenthesis(s):
  stack = []
  max_depth = 0

  for char in s:
    if char == "(":
      stack.append(char)
      max_depth = max(len(stack), max_depth)

    elif char == ")":
      stack.pop()
    
  return max_depth
# Time complexity: O(n) where n is the length of the string. We iterate through the string once.
# Space complexity: O(n) in the worst case when all characters are opening parentheses, as we would be storing all of them in the stack.