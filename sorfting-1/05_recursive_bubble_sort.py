def recursive_bubble_sort(arr, n=None):
    if n is None:
        n = len(arr)

    if n == 1:
        return arr
    
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return recursive_bubble_sort(arr, n - 1)


if __name__ == "__main__":
    arr = [5, 1, 3, 4, 7, 2]
    print(recursive_bubble_sort(arr))