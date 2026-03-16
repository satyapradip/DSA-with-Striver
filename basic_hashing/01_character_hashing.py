# Character Frequency Counter
# This program counts how many times each letter appears in a string,
# then answers queries about specific letters instantly.

# Step 1: Get the input string
text = input("Enter a string: ").strip()

# Step 2: Create a frequency array for all 26 lowercase letters
# Index 0 = 'a', Index 1 = 'b', ... Index 25 = 'z'
frequency = [0] * 26

# Step 3: Count each character in the string
# For each character, find its position (a=0, b=1, etc.) and increment that position
for character in text:
    letter_position = ord(character) - ord('a')
    frequency[letter_position] += 1

# Step 4: Answer queries
num_queries = int(input("How many letters do you want to check? "))

for _ in range(num_queries):
    query_char = input("Enter a letter to count: ").strip()
    query_position = ord(query_char) - ord('a')
    count = frequency[query_position]
    print(f"The letter '{query_char}' appears {count} times\n")