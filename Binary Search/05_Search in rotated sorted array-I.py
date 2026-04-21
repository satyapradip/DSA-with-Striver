# Search in rotated sorted array-I, LeetCode #33
# Time complexity: O(log n)
# Space complexity: O(1)
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand. (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]), find the index of a given target element. If not found in the array, return -1.
# You may assume no duplicate exists in the array.

def search_in_rotated_sorted_array(arr, target):
  low, high = 0, len(arr) - 1
  while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
      return mid 
    if arr[low] <= arr[mid]: # left half is sorted
      if arr[low] <= target < arr[mid]: # target is in the left half
        high = mid - 1
      else: # target is in the right half
        low = mid + 1
    else: # right half is sorted
      if arr[mid] < target <= arr[high - 1]: # target is in the right half
        low = mid + 1
      else: # target is in the left half
        high = mid - 1
  return -1

