# 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"



def longestCommonPrefix(strs):
  strs.sort()  # Sort the array of strings
  res = ""  # Initialize the longest common prefix as an empty string
  i = 0 # Initialize an index to compare characters
  n = len(strs)
  # Compare characters of the first and last strings in the sorted array
  while i < len(strs[0]):
    if strs[0][i] == strs[n-1][i]:  # Compare the first and last strings
      res += strs[0][i]  # If they match, add the character to the result
    else: # If they don't match, we've found the longest common prefix, so we can stop
      break
  return res


# Time complexity: O(m log n) where m is the length of the longest string in the array and n is the number of strings. Sorting takes O(n log n) and comparing characters takes O(m).
# Space complexity: O(1) if we don't consider the space used for the output string, otherwise O(m) for the longest common prefix string.

# type -2 

from ast import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first = strs[0]
        last = strs[-1]
        
        i = 0
        while i < len(first) and first[i] == last[i]:
            i += 1
        
        return first[:i]
    
