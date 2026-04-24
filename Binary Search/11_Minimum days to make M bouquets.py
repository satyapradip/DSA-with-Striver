# Minimum days to make M bouquets
# Given an integer array bloomDay, an integer m and an integer k. We need to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden. The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] day. We need to return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.
# time complexity: O(log(max(bloomDay)) * n) where max(bloomDay) is the maximum number of days for a flower to bloom and n is the number of flowers.
# space complexity: O(1) since we are using a constant amount of extra space.

def min_days(bloomDay, m, k):
  if m * k > len(bloomDay): # if the total number of flowers needed is greater than the number of flowers available, it's impossible to make m bouquets
    return -1
  
  left, right = 1, max(bloomDay)
  
  while left < right:
    mid = left + (right - left) // 2
    bouquets = 0
    flowers = 0
    
    for day in bloomDay:
      if day <= mid:
        flowers += 1
        if flowers == k:
          bouquets += 1
          flowers = 0
      else:
        flowers = 0
    
    if bouquets >= m:
      right = mid
    else:
      left = mid + 1
  
  return left