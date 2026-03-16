# Number of elements in array
size = int(input("Enter number of elements: "))

# Input array elements
arr = list(map(int, input("Enter elements separated by space: ").split()))

# Create hash array (assuming values are between 0 and 12)
hash_arr = [0] * 13

# Precompute frequency
for num in arr:
    if 0 <= num < 13:   # safety check
        hash_arr[num] += 1
    else:
        print(f"Warning: {num} is out of supported range (0-12)")

# Number of queries
queries_count = int(input("Enter number of queries: "))

# Take all queries in one line (better practice)
queries = list(map(int, input("Enter query numbers: ").split()))

# Process queries
for number in queries:
    if 0 <= number < 13:
        print(f"Frequency of {number}:", hash_arr[number])
    else:
        print(f"{number} is out of range")
