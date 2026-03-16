size = 5
arr = [1, 3, 2, 1, 3]

hash_arr = [0] * 13

for num in arr:
    hash_arr[num] += 1

queries = [1, 4, 2, 3, 12]

for number in queries:
    print(hash_arr[number])
