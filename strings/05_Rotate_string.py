# Rotate String 
# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

#A shift on s consists of moving the leftmost character of s to the rightmost position.

#For example, if s = "abcde", then it will be "bcdea" after one shift.

#Example 1:

#Input: s = "abcde", goal = "cdeab"
#Output: true
#Example 2:

#Input: s = "abcde", goal = "abced"
#Output: false

def rotate_string(s, goal):
  if len(s) != len(goal):
    return False  # If the lengths of s and goal are different, they cannot be rotations of each other
  return goal in s+s  # Check if goal is a substring of s concatenated with itself

# Time complexity: O(n) where n is the length of the string s. Checking if goal is a substring of s+s takes O(n) time.
# Space complexity: O(n) for the concatenated string s+s.
