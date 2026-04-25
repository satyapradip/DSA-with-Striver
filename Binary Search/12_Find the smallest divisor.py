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