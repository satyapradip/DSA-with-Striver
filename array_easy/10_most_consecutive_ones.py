def most_consecutive_ones(arr):
    n = len(arr)
    max_count = 0
    current_count = 0

    for i in range(n):
        if arr[i] == 1:
            current_count += 1
        else:
            max_count = max(max_count, current_count) # update the max count, if the current count is greater than the max count
            current_count = 0 # reset the current count to 0
    return max(max_count, current_count) # return the max count, if the current count is greater than the max count

if __name__ == "__main__":
    arr = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1]
    print(most_consecutive_ones(arr))