def rotate_by_k(arr, k):
    n = len(arr)
    k %= n
    temp = [0] * n

    for i in range(n):
        temp[(i + k) % n] = arr[i]

    for i in range(n):
        arr[i] = temp[i]

if __name__ == "__main__":
    arr = [1, 2, 3, 6, 7]
    k = 2
    rotate_by_k(arr, k)
    print(arr)