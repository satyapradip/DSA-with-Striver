def quick_sort(arr, low, high):
    
    if low < high :
        pivot_index = partion(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partion(arr, low, high):
    pivot = arr [high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    low =  0
    high = len(arr) - 1
    quick_sort(arr, low, high)
    print(arr)