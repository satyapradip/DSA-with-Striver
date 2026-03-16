def move_zeros_to_end(arr):
    n = len(arr)
    insert_pos = 0

    for i in range(n):
        if arr[i] != 0:
            arr[insert_pos] = arr[i]
            insert_pos += 1

    for i in range(insert_pos, n):
        arr[i] = 0

if __name__ == "__main__":
    arr = [1, 0, 0, 3, 0, 12 ]
    move_zeros_to_end(arr)
    print(arr)