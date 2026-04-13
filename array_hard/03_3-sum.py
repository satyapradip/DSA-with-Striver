"""Different approaches to solve the 3Sum problem.

Given an integer array nums, return all unique triplets [a, b, c]
such that a + b + c == 0.
"""


# Brute force: try every possible triplet.
# Time: O(n^3), Space: O(k) for storing unique results.
def three_sum_brute_force(nums):
  nums = sorted(nums)
  res = set()

  for i in range(len(nums) - 2):
    for j in range(i + 1, len(nums) - 1):
      for k in range(j + 1, len(nums)):
        if nums[i] + nums[j] + nums[k] == 0:
          res.add((nums[i], nums[j], nums[k]))

  return sorted(res)


# Hashing approach: fix i, then solve 2Sum with a seen set.
# Time: O(n^2), Space: O(n) + result storage.
def three_sum_hashing(nums):
  nums = sorted(nums)
  res = set()

  for i in range(len(nums) - 2):
    seen = set()
    for j in range(i + 1, len(nums)):
      complement = -(nums[i] + nums[j])
      if complement in seen:
        res.add((nums[i], complement, nums[j]))
      seen.add(nums[j])

  return sorted(res)


# Two pointers: after sorting, move pointers based on current sum.
# Time: O(n^2), Space: O(k) for result (O(1) extra excluding output).
def three_sum_two_pointers(nums):
  nums = sorted(nums)
  res = []

  for i in range(len(nums) - 2):
    if i > 0 and nums[i] == nums[i - 1]:
      continue

    left, right = i + 1, len(nums) - 1

    while left < right:
      total = nums[i] + nums[left] + nums[right]

      if total == 0:
        res.append((nums[i], nums[left], nums[right]))
        left += 1
        right -= 1

        while left < right and nums[left] == nums[left - 1]:
          left += 1
        while left < right and nums[right] == nums[right + 1]:
          right -= 1
      elif total < 0:
        left += 1
      else:
        right -= 1

  return res


# This is the standard optimal solution for 3Sum.
# Time: O(n^2) (sorting O(n log n) + two pointers O(n^2)),
# overall O(n^2). Space: O(k) for result.
def three_sum_optimal(nums):
  return three_sum_two_pointers(nums)


# Demo
arr = [-1, 0, 1, 2, -1, -4]
print("brute force:", three_sum_brute_force(arr))
print("hashing:", three_sum_hashing(arr))
print("two pointers:", three_sum_two_pointers(arr))
print("optimal:", three_sum_optimal(arr))