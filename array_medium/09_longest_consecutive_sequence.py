# Brute Forse . time complexity= ,space complexity= ,
def linear_search(arr, target):
    n = len(arr)
    for i in range(n):
        if arr[i] == target: 
            return True
    return False


def longest_consecutive_sequence(arr):
    n = len(arr)
    if n == 0:
        return 0
    
    max_length = 1
    
    for i in range(n):  
        x = arr[i]
        count = 1
        
        while linear_search(arr, x + 1):
            x += 1
            count += 1
        
        max_length = max(max_length, count)
    
    return max_length

if __name__ == "__main__":
    arr = [100, 4, 200, 1, 3, 2]
    print(longest_consecutive_sequence(arr))

# better approach

def longest_consecutive_sequence_better(arr):
    n = len(arr)
    if n == 0:
        return 0

    arr.sort()
    max_length = 1
    count = 1

    for i in range(1, n):
        if arr[i] == arr[i - 1]:
            continue
        elif arr[i] == arr[i - 1] + 1:
            count += 1
        else:
            max_length = max(max_length, count)
            count = 1

    max_length = max(max_length, count)

    return max_length

# optimal solution , 
def longest_consecutive_sequence_optimal(arr):
    if not arr:
        return 0
    nums = set(arr)
    longest_streak = 0
    for num in nums:
        if num - 1 not in nums:
            current_num = num
            current_streak = 1
            while current_num + 1 in nums:
                current_num += 1
                current_streak += 1
            longest_streak = max(longest_streak, current_streak)
    return longest_streak


if __name__ == "__main__":
    arr = [100, 4, 200, 1, 3, 2]
    print(longest_consecutive_sequence_optimal(arr))