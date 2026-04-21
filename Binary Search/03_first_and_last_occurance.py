# First and Last Occurrence of an Element in a Sorted Array, LeetCode #34
# Time complexity: O(log n)
# Space complexity: O(1)
# Given a sorted array of distinct integers and a target value, return the index of the first and last occurrence of the target. If not found, return [-1, -1].

from ast import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def findFirst():
            left, right = 0, len(nums) - 1
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    ans = mid
                    right = mid - 1   # move left
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return ans

        def findLast():
            left, right = 0, len(nums) - 1
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    ans = mid
                    left = mid + 1   # move right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return ans

        return [findFirst(), findLast()]



