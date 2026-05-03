# Sort Characters by Frequency
# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.
# Example 1:
# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once. So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

# Approach 1 : Use a hash map (dictionary) to count the occurrences of each character in the string, and then sort the characters based on their frequency.
def frequency_sort(s):
  char_count = {}

  # Count the occurrences of each character in the string
  for char in s:
    char_count[char] = char_count.get(char, 0) + 1

  # Sort the characters based on their frequency
  sorted_chars = sorted(char_count.keys(), key=lambda x: char_count[x], reverse=True)

  # Build the result string based on the sorted characters and their counts
  result = []
  for char in sorted_chars:
    result.append(char * char_count[char])  # Append the character repeated by its count

  return ''.join(result)

# Time complexity: O(n log n) where n is the number of unique characters in the string. Sorting takes O(n log n) time.
# Space complexity: O(n) for the hash map and the result string.

# Approach 2 : Use a hash map (dictionary) to count the occurrences of each character in the string, and then use a bucket sort approach to sort the characters based on their frequency.
def frequency_sort(s):
  char_count = {}

  # Count the occurrences of each character in the string
  for char in s:
    char_count[char] = char_count.get(char, 0) + 1

  # Create buckets for characters based on their frequency
  buckets = [[] for _ in range(len(s) + 1)]
  for char, count in char_count.items():
    buckets[count].append(char)

  # Build the result string based on the buckets
  result = []
  for i in range(len(buckets) - 1, 0, -1):
    for char in buckets[i]:
      result.append(char * i)  # Append the character repeated by its count

  return ''.join(result)

# Time complexity: O(n) where n is the length of the string. We iterate through the string to count characters and then through the buckets to build the result.
# Space complexity: O(n) for the hash map and the result string.

# Approach 3 : Use a hash map (dictionary) to count the occurrences of each character in the string, and then use a max heap to sort the characters based on their frequency.
import heapq

def frequency_sort(s):
  char_count = {}

  # Count the occurrences of each character in the string
  for char in s:
    char_count[char] = char_count.get(char, 0) + 1

  # Create a max heap with negative frequencies
  heap = [(-count, char) for char, count in char_count.items()]
  heapq.heapify(heap)

  # Build the result string based on the heap
  result = []
  while heap:
    neg_count, char = heapq.heappop(heap)
    result.append(char * (-neg_count))  # Append the character repeated by its count

  return ''.join(result)

# Time complexity: O(n log n) where n is the number of unique characters in the string. Heap operations take O(log n) time.
# Space complexity: O(n) for the hash map and the result string.