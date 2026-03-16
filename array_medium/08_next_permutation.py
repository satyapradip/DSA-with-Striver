# time 
def next_permnuatation(arr):
    n = len(arr)
    indx = -1
    for i in range(n-2, -1, -1):
        if arr[i] < arr[i+1]:
            indx = i
            break
    #
    if indx == -1:
        arr.reverse()
        return arr
    #
    for i in range(n-1, indx, -1):
        if arr[i] > arr[indx]:
            arr[i], arr[indx] = arr[indx], arr[i]
            break
    #    
    arr[indx+1:] = reversed(arr[indx+1:])
    return arr