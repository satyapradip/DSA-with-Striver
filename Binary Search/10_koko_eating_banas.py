# Koko Eating Bananas
# Problem Statement: Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. Koko wants to eat all the bananas within h hours.
# time complexity: O(log(max(piles)) * n) where max(piles) is the maximum number of bananas in a pile and n is the number of piles.
# space complexity: O(1) since we are using a constant amount of extra space.

def min_eating_speed(piles, h):
  left, right = 1, max(piles)
  while left < right:
    mid = left + (right - left) // 2
    # Calculate the total hours needed to eat all bananas at speed mid
    total_hours = sum((pile + mid - 1) // mid for pile in piles)
    if total_hours <= h:
      # If Koko can finish within h hours, try a slower speed
      right = mid
    else:
      # If Koko cannot finish within h hours, try a faster speed
      left = mid + 1
  return left

# Example usage:
piles = [3, 6, 7, 11]
h = 8
print(min_eating_speed(piles, h))  # Output: 4