# Brute Forse Approach , Time Complexity: O(n^2)
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range( i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

print(two_sum([2, 7, 11, 15], 9))

# better approach using hashmap , Time Complexity: O(n) , Space Complexity: O(n)
def two_sum_hashmap(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap: 
            return [hashmap[complement], i]
        hashmap[nums[i]] = i
    return []

print(two_sum_hashmap([2, 7, 11, 15], 9))

# optimal approach using two pointers , Time Complexity: O(n) , Space Complexity: O(1)
def two_sum_two_pointers(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        if nums[left] + nums[right] == target:
            return [left, right] # or return yes 
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1
    return []  # or return no 