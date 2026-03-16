# Brute Forse . time complexity = O(n), space complexity  = O(n)
from turtle import pos


def Rearrange_array_by_sign(arr):
    n = len(arr)
    positive = []
    negative = []
    for i in range(n):
        if arr[i] >= 0:
            positive.append(arr[i])
        else:
            negative.append(arr[i])
    
    for i in range(n//2):
        arr[2*i] = positive[i]
        arr[2*i+1] = negative[i]

    return arr

if __name__ == "__main__":
    arr = [-5, -2, 5, 2, 4, 7, -7, -3]
    print(Rearrange_array_by_sign(arr))

# Optimal Approach, Timne complexity = O(n), space complexity = O(n)
def Rearrange_array_by_sign2(arr):
    n = len(arr)
    ans = [0] * n
    pos_index = 0
    neg_index = 1
    for i in range(n):
        if arr[i] >= 0:
            ans[pos_index] = arr[i]
            pos_index += 2
        else:
            ans[neg_index] = arr[i]
            neg_index += 2
    return ans

if __name__ == "__main__":
    arr = [-5, -2, 5, 2, 4, 7, -7, -3]
    print(Rearrange_array_by_sign2(arr))

# if there number of negetive and positive elements are not same then.......
# Second varity
def Rearrange_array_by_sign_second_varity(arr):
    n = len(arr)
    pos = []
    neg = []
    for i in range(n):
        if arr[i] >= 0:
            pos.append(arr[i])
        else:
            neg.append(arr[i])
    if len(pos) > len(neg):
        for i in range(len(neg)):
            arr[2*i] = pos[i]
            arr[2*i+1] = neg[i]
        for i in range(len(neg), len(pos)):
            arr[n-1] = pos[i]
    else:
        for i in range(len(pos)):
            arr[2*i] = pos[i]
            arr[2*i+1] = neg[i]
        for i in range(len(pos), len(neg)):
            arr[n-1] = neg[i]
    return arr