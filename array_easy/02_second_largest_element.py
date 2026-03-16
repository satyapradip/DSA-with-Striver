def second_largest(arr):
    
    n = len(arr)


    largest = -1
    secondLargest = -1

    for i in range (n):
        if arr[i] > largest:
            secondLargest = largest
            largest = arr[i]
        elif arr[i] < largest and arr[i] > secondLargest:
            secondLargest  = arr[i]

    return secondLargest


if __name__ == "__main__":
    arr = [2, 4, 5, 7, 7, 6]
    print(second_largest(arr))