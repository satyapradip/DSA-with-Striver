# Find Peak Element
# Problem Statement: A peak element is an element that is strictly greater than its neighbors.
# time complexity: O(log n) since we are using binary search.
# space complexity: O(1) since we are using a constant amount of extra space.

def find_peak_element(nums):
  left, right = 0, len(nums) - 1
  while left < right:
    mid = left + (right - left) // 2
    if nums[mid] > nums[mid + 1]:
      # We are in the descending part of the array, so the peak must be on the left side (including mid)
      right = mid
    else:
      # We are in the ascending part of the array, so the peak must be on the right side
      left = mid + 1
  return nums[left]  # At the end of the loop, left will be pointing to a peak element.

# Example usage:
nums = [1, 2, 3, 1]
print(find_peak_element(nums))  # Output: 3