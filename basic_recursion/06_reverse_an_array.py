# def reverse_an_array(arr, i):
#     if i == 0:
#         return 
#     print(arr[i-1])
#     reverse_an_array(arr, i-1)
    

# if __name__ == "__main__":
#     arr = [10, 20, 30, 40]
#     i = len(arr)
#     reverse_an_array(arr, i) 

# this not reversing array , it is printing the array reversely 

# the original method 
def reverse_array(arr):
    start = 0
    end = len(arr) - 1

    while end > start :
        arr[start] , arr[end] = arr[end] , arr[start]
        start += 1
        end -= 1

    return arr

if __name__ == "__main__" :
    arr = [10, 20, 30, 40, 50]
    print(reverse_array(arr))
