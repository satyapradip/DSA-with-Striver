# Brute force O(n^4) time, O(k) space for results.
from ast import List


def four_sum_brute_force(nums, target):
  nums = sorted(nums)
  res = set()

  for i in range(len(nums) - 3):
    for j in range(i + 1, len(nums) - 2):
      for k in range(j + 1, len(nums) - 1):
        for l in range(k + 1, len(nums)):
          if nums[i] + nums[j] + nums[k] + nums[l] == target:
            res.add((nums[i], nums[j], nums[k], nums[l]))

  return list(res)

# Hashing approach: fix i, j, then solve 2Sum with a seen set.
# Time: O(n^3), Space: O(n) + result storage.
def four_sum_hashing(nums, target):
  nums = sorted(nums)
  res = set()

  for i in range(len(nums) - 3):  # we look for 4 numbers, so we need at least 3 more after i, hence -3
    for j in range(i + 1, len(nums) - 2):  # we look for 4 numbers, so we need at least 2 more after j, hence -2
      seen = set()
      for k in range(j + 1, len(nums)):
        complement = target - (nums[i] + nums[j] + nums[k])
        if complement in seen:
          res.add((nums[i], nums[j], complement, nums[k]))
        seen.add(nums[k])

  return list(res)

# Two pointers: after sorting, fix i, j and move pointers based on current sum.
# Time: O(n^3), Space: O(k) for result (O(1) extra excluding output).
def four_sum_two_pointers(nums, target):
  nums = sorted(nums)
  res = []

  for i in range(len(nums) - 3):
    if i > 0 and nums[i] == nums[i - 1]:
      continue
    for j in range(i + 1, len(nums) - 2):
      if j > i + 1 and nums[j] == nums[j - 1]:
        continue
      left = j + 1
      right = len(nums) - 1
      while left < right:
        current_sum = nums[i] + nums[j] + nums[left] + nums[right]
        if current_sum == target:
          res.append((nums[i], nums[j], nums[left], nums[right]))
          while left < right and nums[left] == nums[left + 1]:
            left += 1
          while left < right and nums[right] == nums[right - 1]:
            right -= 1
          left += 1
          right -= 1
        elif current_sum < target:
          left += 1
        else:
          right -= 1

  return res

#
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []
        nums.sort()
        n = len(nums)
        
        for i in range(n - 3):
            # Skip duplicated number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Check min
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break            
            # Check max
            if nums[i] + nums[-1] + nums[-2] + nums[-3] < target:
                continue

            for j in range(i + 1, n - 2):

                # Skip duplicated number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Check min
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break            
                # Check max
                if nums[i] + nums[j] + nums[-1] + nums[-2] < target:
                    continue
                
                sum_1_2 = nums[i] + nums[j]

                left = j + 1
                right = n - 1

                while left < right:
                    total = sum_1_2 + nums[left] + nums[right]

                    if total > target:
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        answer.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1    

                        left += 1
                        right -= 1
        
        return answer
                
                
                