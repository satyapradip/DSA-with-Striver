# Better Approach, Time Complexity: O(n) , Space Complexity: O(1)
def sort_array_of_0_and_1(arr):
    count_0 = 0
    count_1 = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            count_0 += 1
        else:
            count_1 += 1
    for i in range(count_0):
        arr[i] = 0
    for i in range(count_0, count_0 + count_1):
        arr[i] = 1

    return arr

if __name__ == "__main__":
    arr = [0, 1, 0, 1, 0, 1]
    print(sort_array_of_0_and_1(arr))

# Optimal approach using two pointers, Time Complexity: O(n) , Space Complexity: O(1)
def sort_array_of_0_and_1_two_pointers(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] == 0:
            left += 1
        elif arr[right] == 1:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return arr

if __name__ == "__main__":
    arr = [0, 1, 0, 1, 0, 1]
    print(sort_array_of_0_and_1_two_pointers(arr))


# dutch national flag algorithm, Time Complexity: O(n) , Space Complexity: O(1)
def sort_array_of_0_and_1_and_2_dutch_national_flag(arr):
    low = 0
    mid = 0
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

if __name__ == "__main__":
    arr = [0, 1, 0, 1, 0, 1, 2, 0, 1, 2, 0, 1, 2]
    print(sort_array_of_0_and_1_and_2_dutch_national_flag(arr))