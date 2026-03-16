# Brute Forse , time complexity = O(n^3), spaace complexity = O(1)
def maximaum_subarray_sum(arr):
    n = len(arr)
    max_sum = float('-inf') # smallest possible integer

    for i in range(n):
        for j in range(i, n):
            current_sum = 0
            for k in range(i, j+1):
                current_sum += arr[k]
            max_sum = max(max_sum, current_sum)

    return max_sum

if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maximaum_subarray_sum(arr))


# better solution , time complexity = O(n^2), space complexity = O(1)
def maximaum_subarray_sum_better(arr):
    n = len(arr)
    max_sum = float('-inf') # smallest possible integer

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            max_sum = max(max_sum, current_sum)

    return max_sum

if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maximaum_subarray_sum_better(arr))


# optimal solution(using Kadane's algorithm), time complexity = , space complexity =
def maximaum_subarray_sum_optimal(arr):
    n = len(arr)
    max_sum = float('-inf') # smallest possible integer
    current_sum = 0
    for i in range(n):
        current_sum += arr[i]
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0         

    return max_sum

if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maximaum_subarray_sum_optimal(arr))