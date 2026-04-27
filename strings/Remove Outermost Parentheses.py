# Remove the outermost parentheses of every primitive string in the primitive decomposition of s.
# A primitive string is a non-empty string that cannot be written as the concatenation of two non-empty primitive strings. 
# Example 1:
# Input: s = "(()())(())"
# Output: "()()()"
# Explanation: The input string is "(()())(())", with primitive decomposition "(()())" + "(())".

# Example 2:
# Input: s = "(()())(())(()(()))"
# Output: "()()()()(())"
# Explanation: The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".

def removeOuterParentheses(s):
      # Initialize result string
      result = ""  
      # Initialize nesting level counter
      level = 0     
      # Traverse the string
      for char in s:
          # If we encounter '(', increase the level
          if char == '(':
              # If we're inside a primitive, add '(' to result
              if level > 0:
                  result += char
              # Increase the nesting level for '('
              level += 1  
          elif char == ')':
              # Decrease the nesting level for ')'
              level -= 1  
              # If we're inside a primitive, add ')' to result
              if level > 0:
                  result += char
      # Return the final result after removing the outer parentheses
      return result

# Time complexity: O(n) where n is the length of the input string s. We traverse the string once to build the result.
# Space complexity: O(n) in the worst case, if all parentheses are nested, we will store all characters in the result string. However, in general, the space complexity is O(n) due to the result string.

if __name__ == "__main__":
    s = "(()())(())(()(()))"
    print(removeOuterParentheses(s))  # Output: "()()()()(())"