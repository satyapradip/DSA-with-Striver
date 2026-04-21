# Upper Bound and Lower Bound,

def lower_bound(arr, target):
  left, right = 0, len(arr)
  while left < right:
    mid = (left + right) // 2
    if arr[mid] < target:
      left = mid + 1
    else:
      right = mid
  return left

def upper_bound(arr, target):
  left, right = 0, len(arr)
  while left < right:
    mid = (left + right) // 2
    if arr[mid] <= target:
      left = mid + 1
    else:
      right = mid
  return left

print(lower_bound([1, 2, 2, 2, 3], 2)) # 1
print(upper_bound([1, 2, 2, 2, 3], 2)) # 4