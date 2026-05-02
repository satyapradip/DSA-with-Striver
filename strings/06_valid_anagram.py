# Check if two strings are anagrams of each other
# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
# Approach 1 : Sort the characters of both strings and compare them. If they are the same, then the strings are anagrams.
def is_anagram(s, t):
  return sorted(s) == sorted(t)

# Time complexity: O(n log n) where n is the length of the strings. Sorting takes O(n log n) time.
# Space complexity: O(n) for the sorted lists of characters.

# Approach 2 : Use a hash map (dictionary) to count the occurrences of each character in both strings. Then compare the counts.
def is_anagram(s, t):
  if len(s) != len(t):
    return False  # If the lengths of s and t are different, they cannot be anagrams of each other

  char_count = {}

  # Count the occurrences of each character in string s
  for char in s:
    char_count[char] = char_count.get(char, 0) + 1

  # Subtract the counts based on characters in string t
  for char in t:
    if char not in char_count or char_count[char] == 0:
      return False  # If a character in t is not found in s or its count is already zero, they are not anagrams
    char_count[char] -= 1

  return True

# Time complexity: O(n) where n is the length of the strings. We iterate through both strings once.
# Space complexity: O(1) if we assume the character set is fixed (e.g., ASCII), otherwise O(n) in the worst case if all characters are unique.

# Approach 3 : Use a hash map (dictionary) to count the occurrences of each character in string s, and then check if the counts match for string t.
def is_anagram(s, t):
  if len(s) != len(t):
    return False  # If the lengths of s and t are different, they cannot be anagrams of each other

  char_count = {}

  # Count the occurrences of each character in string s
  for char in s:
    char_count[char] = char_count.get(char, 0) + 1

  # Check if the counts match for string t
  for char in t:
    if char not in char_count or char_count[char] == 0:
      return False  # If a character in t is not found in s or its count is already zero, they are not anagrams
    char_count[char] -= 1

  return True