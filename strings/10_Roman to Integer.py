# Roman to Integer
# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the range from 1 to 3999.
# Example 1:  
# Input: s = "III"
# Output: 3
# Example 2:
# Input: s = "CXXIV"
# Output: 124

# Approach 1: Hash Map 

def roman_to_integer(s):
  roman_numerals = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
  }

  total = 0

  for i in range(len(s)):
    current = roman_numerals[s[i]]

    if i + 1 < len(s) and current < roman_numerals[s[i + 1]]:
      total -= current
    else:
      total += current
  
  return total

# Time complexity: O(n) where n is the length of the string. We iterate through the string once.
# Space complexity: O(1) as we are using only a constant amount of extra space for the hash map and the total variable.
