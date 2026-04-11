# 118. Pascal's Triangle
# Given an integer numRows, return the first numRows of Pascal's triangle. 
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown: 

def generate(numRows):
    result = []

    for i in range(numRows):
        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = result[i - 1][j - 1] + result[i - 1][j]

        result.append(row)

    return result


# Approach 2: Return the Row 