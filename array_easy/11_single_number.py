def single_number(nums):
    #brute force approach using nested loops
    #time complexity: O(n^2)
    #space complexity: O(1)
    for i in range(len(nums)):
        num = nums[i]
        count = 0
        for j in range(len(nums)):
            if num == nums[j]:
                count += 1
        if count == 1:
            return num
    return -1

#optimised approach using hash map
#time complexity: O(n)
#space complexity: O(n)
def single_number_optimised(nums):
    n = len(nums)
    hash_arr = [0] * (n + 1)
    for num in nums:
        hash_arr[num] += 1
    for i in range(n + 1):
        if hash_arr[i] == 1:
            return i
    return -1 #if no single number is found, return -1

#most optimised approach using xor operator
#time complexity: O(n)
#space complexity: O(1)
def single_number_most_optimised(nums):
    result = 0
    for num in nums:
        result ^= num  # xor of the number with the result will give the single number
    return result

#example usage
if __name__ == "__main__":
    nums = [2, 2, 1, 1, 3]
    print(single_number(nums))
    print(single_number_optimised(nums))
    print(single_number_most_optimised(nums))