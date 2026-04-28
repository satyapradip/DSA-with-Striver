# Given an input string s, reverse the order of the words.

#A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

#Return a string of the words in reverse order concatenated by a single space.

#Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

#Example 1:

#Input: s = "the sky is blue"
#Output: "blue is sky the"

def reverseWords(s):
  return " ".join(s.split()[::-1])

if __name__ == "__main__":
    s = "the sky is blue"
    print(reverseWords(s))  # Output: "blue is sky the"

# Time complexity: O(n) where n is the length of the input string s. We split the string into words and reverse the list of words, which takes O(n) time.
# Space complexity: O(n) in the worst case, if all characters in the input string
# are non-space characters, we will store all characters in the result string. However, in general, the space complexity is O(n) due to the result string.