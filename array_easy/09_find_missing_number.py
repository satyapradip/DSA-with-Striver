def findMissingNUm(arr):
    n = len(arr) + 1
    total_sum = n * (n + 1) // 2
    arr_sum = sum(arr)
    return total_sum - arr_sum

# Example usage:
if __name__ == "__main__":
    arr = [1, 2, 4, 5]
    print(findMissingNUm(arr))  # Output: 3