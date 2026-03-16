# Brute Forse Approach, Time Complexity: O(n^2) , Space Complexity: O(1)
def majority_element_1(arr):
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1
        if count > len(arr) / 2:
            return arr[i]
    return -1

if __name__ == "__main__":
    arr = [1, 1, 1, 1, 2, 3, 4]
    print(majority_element_1(arr))

# optimal approach using hash map, Time Complexity: O(n) , Space Complexity: O(n)
def majority_element_1_optimal(arr):
    hash_map = {}
    for i in range(len(arr)):
        if arr[i] in hash_map:
            hash_map[arr[i]] += 1
        else:
            hash_map[arr[i]] = 1
    for key, value in hash_map.items():
        if value > len(arr) / 2:
            return key
    return -1

if __name__ == "__main__":
    arr = [1, 1, 1, 1, 2, 3, 4]
    print(majority_element_1_optimal(arr))
    
# optimal approach using moore's voting algorithm, Time Complexity: O(n) , Space Complexity: O(1)
def majority_element_1_moore_voting(arr):
    candidate = None
    count = 0
    for i in range(1, len(arr)):
        if count == 0:
            candidate = arr[i]
            count = 1
        elif arr[i] == candidate:
            count += 1
        else:
            count -= 1

    if arr.count(candidate) > len(arr) / 2:
        return candidate
    return -1

if __name__ == "__main__":
    arr = [1, 1, 1, 1, 2, 3, 4, 1]
    print(majority_element_1_moore_voting(arr))