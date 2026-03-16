def longest_subarray(arr, k):
    n = len(arr)

    maxLen = 0

    left = 0
    right = 0

    sum = arr[0] #initialize the sum with the first element of the array

    while right < n : 
        while sum > k and left <= right:  #check if the sum is greater than the target and the left is less than or equal to the right
            sum -= arr[left]    #subtract the left element from the sum
            left += 1 # move the left pointer to the right
        if sum == k:  #check if the sum is equal to the target
            maxLen = max(maxLen, right - left + 1) #update the maximum length of the subarray
        right += 1
        if right < n:  #check if the right is less than the length of the array
            sum += arr[right] #add the right element to the sum

    return maxLen #return the maximum length of the subarray


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    k = 10
    print(longest_subarray(arr, k))