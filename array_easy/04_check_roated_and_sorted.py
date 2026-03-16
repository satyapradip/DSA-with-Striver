def isSortedandRoated(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        if arr[i] > arr[(i+1) % n]:
            count += 1

    return count <= 1

if __name__ == "__main__":
    arr = [3,4,5,1,2]
    print(isSortedandRoated(arr))

    arr2 = [1, 2, 3, 4, 5]
    print(isSortedandRoated(arr2)) 