def longest_subarray_with_sum0(arr, k):
    n = len(arr)
    maxLen = 0
    sum = 0
    prefixSum = {} #initialize the prefix sum map
    prefixSum[0] = -1 #initialize the prefix sum map with 0 at index -1
    for i in range(n):
        sum += arr[i]
        if sum in prefixSum: #check if the sum is in the prefix sum map
            maxLen = max(maxLen, i - prefixSum[sum]) #update the maximum length of the subarray if the sum is in the prefix sum map
        else:
            prefixSum[sum] = i # add the sum to the prefix sum map
    return maxLen #return the maximum length of the subarray

if __name__ == "__main__":
    arr = [1, -1, 3, 2, -2, -8, 1, 7, 10, 23]
    k = 0
    print(longest_subarray_with_sum0(arr, k))