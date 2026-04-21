# Find Minimum in Rotated Sorted Array
# Problem Statement: to find the minimum element in a rotated sorted array. The array is sorted in ascending order and then rotated at some pivot. The function should return the minimum element in the array.
# time complexity: O(log n) in the average case, but can degrade to O(n) in the worst case when there are many duplicates.
# space complexity: O(1) since we are using a constant amount of extra space.

def find_min(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]