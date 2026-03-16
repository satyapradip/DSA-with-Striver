def maxFrequency(k, nums):
    nums.sort()
    left = right = res = total = 0
    while right < len(nums):
        total += nums[right]
        while nums[right] * (right - left + 1) > total + k:
            total -= nums[left]
            left += 1
        
        res = max(res, right - left + 1)
        right += 1
    
    return res

if __name__ == "main":
 # The line `arr = [1,2,3,4]` is creating a list named `arr` with elements 1, 2, 3, and 4. This list
 # is then passed as an argument to the `maxFrequency` function with `k` value of 3.
    arr = [1,2,3,4]
    print(maxFrequency(3, arr))