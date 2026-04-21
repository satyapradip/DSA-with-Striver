# Search in Rotated Sorted Array II
# Problem Statement: to find a target value in a rotated sorted array that may contain duplicates. The array is sorted in ascending order and then rotated at some pivot. The function should return true if the target is found in the array, and false otherwise.
# time complexity: O(log n) in the average case, but can degrade to O(n) in the worst case when there are many duplicates.
# space complexity: O(1) since we are using a constant amount of extra space.
def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return True

        # If we have duplicates, we can skip them
        if nums[left] == nums[mid] == nums[right]:
            left += 1
            right -= 1
        # Left half is sorted
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return False

if __name__ == "__main__":
    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 0
    print(search(nums, target))  # Output: True

    target = 3
    print(search(nums, target))  # Output: False