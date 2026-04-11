# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
# The algorithm should run in linear time and in O(1) space.
def majority_Element2(nums):
    count = {} # Hash map to count the occurrences of each element
    for num in nums: 
        if num in count: # If the number is already in the count dictionary, increment its count
            count[num] += 1
        else:
            count[num] = 1 # If the number is not in the count dictionary, add it with a count of 1

    result = []
    for key, value in count.items():  # Iterate through the count dictionary and check if the count of each element is greater than n/3
        if value > len(nums) // 3:   # If the count of the element is greater than n/3, add it to the result list
            result.append(key)

    return result

# Approach 2: Boyer-Moore Voting Algorithm
def majority_Element2(nums):
    if not nums:
        return []

    # Step 1: Find potential candidates
    candidate1, candidate2 = None, None
    count1, count2 = 0, 0

    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1

    # Step 2: Verify the candidates
    count1, count2 = 0, 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1

    result = []
    if count1 > len(nums) // 3:
        result.append(candidate1)
    if count2 > len(nums) // 3:
        result.append(candidate2)

    return result

