# Single Element in a Sorted Array
# Problem Statement: Given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.
# time complexity: O(log n) since we are using binary search.
# space complexity: O(1) since we are using a constant amount of extra space.

def single_non_duplicate(nums):
  left, right = 0, len(nums) - 1
  while left < right:
    mid = left + (right - left) // 2

    # check if mid is even or odd, if it's odd we need to move it back to the previous even index
    if mid % 2 == 1:
      mid -= 1   # we want to compare pairs, so we need to ensure mid is even
    if nums[mid] == nums[mid+1]: # if the pair is valid, the single element must be in the right half
      left = mid + 2
    else:
      right = mid 
  return nums[left]  # at the end of the loop, left will be pointing to the single element.

# Example usage:
nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
print(single_non_duplicate(nums))  # Output: 2