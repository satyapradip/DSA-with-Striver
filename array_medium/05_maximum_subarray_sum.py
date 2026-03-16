# return the subarray that has the maximum subarray sum
class Solution:
    def max_subarray_sum(self, nums):

    # maximum sum
        maxi = float('-inf') 
        
        # current sum of subarray
        sum = 0 
        
        # starting index of current subarray
        start = 0 
        
        # indices of the maximum sum subarray
        ansStart = -1
        ansEnd = -1
        
        # Iterate through the array
        for i in range(len(nums)):
            
            # update starting index if sum is reset
            if sum == 0:
                start = i
            
            # add current element to the sum
            sum += nums[i] 
            
            """ Update maxi and subarray indices
            if current sum is greater """
            if sum > maxi:
                maxi = sum
                ansStart = start
                ansEnd = i
            
            # Reset sum to 0 if it becomes negative
            if sum < 0:
                sum = 0
        
        # Printing the subarray
        print("The subarray is: [", end="")
        for i in range(ansStart, ansEnd + 1):
            print(nums[i], end=" ")
        print("]")

        # Return the maximum subarray sum found
        return maxi

if __name__ == "__main__":
    arr = [ -2, 1, -3, 4, -1, 2, 1, -5, 4 ]

    # Create an instance of Solution class
    sol = Solution()

    maxSum = sol.max_subarray_sum(arr)

    # Print the max subarray sum
    print(f"The maximum subarray sum is: {maxSum}")