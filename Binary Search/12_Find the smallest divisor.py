# Find the smallest divisor given a threshold
# Time complexity: O(n log m) where n is the length of nums and m is the maximum value in nums. We are performing a binary search on the range of possible divisors, which takes O(log m) time, and for each divisor, we are calculating the sum of the divisions, which takes O(n) time.
# Space complexity: O(1) since we are using a constant amount of extra space.
def smallest_divisor(nums, threshold):
  left, right = 1, max(nums)
  
  while left < right:
    mid = left + (right - left) // 2
    total = sum((num - 1) // mid + 1 for num in nums) # calculate the sum of the divisions using integer division
    
    if total > threshold:
      left = mid + 1
    else:
      right = mid
  
  return left

# Second Solution - Using math.ceil to calculate the sum of the divisions
import math
def smallest_divisor(nums, threshold):
  left, right = 1, max(nums)
  
  while left < right:
    mid = left + (right - left) // 2
    total = sum(math.ceil(num / mid) for num in nums) # calculate the sum of the divisions using math.ceil
    
    if total > threshold:
      left = mid + 1
    else:
      right = mid
  
  return left


# Third Solution - Using a helper function to calculate the sum of the divisions
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n=len(nums)
        if n>threshold:
            return -1
        low=1
        high=max(nums)
        while low<=high:
            mid=low + (high-low)//2
            if self.sumByD(nums,mid)<=threshold:
                high=mid-1
            else:
                low=mid+1
        return low
    def sumByD(self,arr,div):
        total = 0
        for x in arr:
            total += (x + div - 1) // div
        return total
        