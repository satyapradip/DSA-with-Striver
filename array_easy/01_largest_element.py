def largest_element(arr):
    n = len(arr)
    max = arr[0]

    for i in range (1, n):
        if arr[i] > max:
            max = arr[i]

    return max

if __name__ == "__main__":
    arr = [3, 2, 5, 7, 1, 4]
    print(largest_element(arr))
