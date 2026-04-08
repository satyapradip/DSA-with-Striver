# Count Subarray sum Equals K , 
# brute force approach, time complexity O(n^3) and space complexity O(1)
def count_subarray_sum(nums, k):
    count = 0
    for i in range(len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):           
            current_sum += nums[j]
            if current_sum == k:
                count += 1
    return count

# optimized approach using prefix sum and hash map, time complexity O(n) and space complexity O(n)
def count_subarray_sum_optimal(nums, k):
    count = 0
    prefix_sum = 0
    prefix_sum_count = {0: 1}  # Initialize with prefix sum 0 occurring once
    
    for num in nums:
        prefix_sum += num
        
        # Check if there is a prefix sum that equals current prefix sum - k
        if (prefix_sum - k) in prefix_sum_count:
            count += prefix_sum_count[prefix_sum - k]
        
        # Update the count of the current prefix sum in the hash map
        if prefix_sum in prefix_sum_count:
            prefix_sum_count[prefix_sum] += 1
        else:
            prefix_sum_count[prefix_sum] = 1
            
    return count
