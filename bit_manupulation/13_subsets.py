# 78. Subsets
# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# ---------------------------------------------------------------------------
# Problem: Given an array of unique integers, generate all possible subsets.
# The total number of subsets for an array of size n is 2^n.
# Example: nums = [1, 2, 3]
# Output: [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Approach 1: Cascading / Iterative (Build subsets one element at a time)
# ---------------------------------------------------------------------------
# Intuition:
# - Start with an empty subset [[]].
# - For each number in the array, take all existing subsets and add the current
#   number to each of them to form new subsets.
# - Append these new subsets to the result list.
#
# Example walkthrough with nums = [1, 2, 3]:
#   Start: result = [[]]
#   num = 1: result = [[], [1]]
#   num = 2: result = [[], [1], [2], [1,2]]
#   num = 3: result = [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
#
# Time Complexity: O(n * 2^n) — For each of the n elements, we iterate over
#                   the current result list which can grow up to size 2^n.
# Space Complexity: O(n * 2^n) — Storing all subsets.
# ---------------------------------------------------------------------------
def subsets_cascading(arr):
    """
    Generate all subsets using the iterative cascading approach.
    
    Args:
        arr: List of unique integers
        
    Returns:
        List of lists, where each inner list is a subset
    """
    # Start with the empty subset
    result = [[]]

    # Iterate through each number in the input array
    for num in arr:
        # For each existing subset, create a new subset by adding the current number
        # List comprehension: take every 'curr' in 'result', append 'num' to it
        new_subsets = [curr + [num] for curr in result]
        # Extend the result with the newly formed subsets
        result += new_subsets

    return result


# ---------------------------------------------------------------------------
# Approach 2: Backtracking / Recursion (Pick / Not-Pick decision)
# ---------------------------------------------------------------------------
# Intuition:
# - For each element, we have two choices: include it in the current subset or
#   exclude it. This forms a recursion tree of depth n.
# - We traverse the array with an index. At each step:
#     * Option 1: Exclude the current element (just move to next index).
#     * Option 2: Include the current element in the subset and move to next.
# - When we reach the end of the array (index == n), we add the current
#   subset to the result.
#
# Example recursion tree for nums = [1, 2]:
#                              []
#                           /      \
#                        []        [1]
#                       /   \     /    \
#                     []   [2]  [1]   [1,2]
#   Leaves:          []   [2]  [1]   [1,2]
#
# Time Complexity: O(n * 2^n) — 2^n subsets, and each takes O(n) to copy.
# Space Complexity: O(n) — Recursion stack depth (not counting output space).
# ---------------------------------------------------------------------------
def subsets_backtracking(arr):
    """
    Generate all subsets using backtracking (pick / not-pick recursion).
    
    Args:
        arr: List of unique integers
        
    Returns:
        List of lists, where each inner list is a subset
    """
    result = []      # Stores all subsets
    current = []     # Stores the current subset being built

    def backtrack(index):
        """
        Recursive helper function.
        
        Args:
            index: Current position in the array being considered
        """
        # Base case: processed all elements → add current subset to result
        if index == len(arr):
            # Append a copy of 'current' because 'current' will be mutated
            result.append(current[:])
            return

        # --- Decision 1: EXCLUDE the current element ---
        # Simply move to the next index without adding arr[index] to current
        backtrack(index + 1)

        # --- Decision 2: INCLUDE the current element ---
        # Add arr[index] to the current subset
        current.append(arr[index])
        # Move to the next index
        backtrack(index + 1)

        # Backtrack: remove the last added element to restore previous state
        # This is crucial — without this, the 'current' list would keep growing
        # and produce incorrect results for other branches of the recursion tree.
        current.pop()

    # Start recursion from index 0
    backtrack(0)
    return result


# ---------------------------------------------------------------------------
# Approach 3: Bit Manipulation (Using binary representation)
# ---------------------------------------------------------------------------
# Intuition:
# - For an array of size n, there are 2^n subsets.
# - Each subset can be represented by a binary number of n bits:
#     * 0 at bit i → exclude arr[i]
#     * 1 at bit i → include arr[i]
# - Example: nums = [1, 2, 3], n = 3
#     Binary 000 → []           Binary 100 → [1]
#     Binary 001 → [3]          Binary 101 → [1, 3]
#     Binary 010 → [2]          Binary 110 → [1, 2]
#     Binary 011 → [2, 3]       Binary 111 → [1, 2, 3]
#
# Time Complexity: O(n * 2^n) — For each of the 2^n subsets, we iterate over
#                   n bits to decide inclusion/exclusion.
# Space Complexity: O(n * 2^n) — Storing all subsets.
# ---------------------------------------------------------------------------
def subsets_bit_manipulation(arr):
    """
    Generate all subsets using bit manipulation.
    Each subset is mapped to a binary number where bit i indicates
    whether arr[i] is included.
    
    Args:
        arr: List of unique integers
        
    Returns:
        List of lists, where each inner list is a subset
    """
    n = len(arr)
    total_subsets = 1 << n  # 2^n (bitwise left shift: 2 raised to power n)
    result = []

    # Iterate over all possible bitmasks from 0 to 2^n - 1
    for mask in range(total_subsets):
        current_subset = []
        # Check each bit position to decide which elements to include
        for i in range(n):
            # If the i-th bit in 'mask' is 1, include arr[i]
            # (mask >> i) shifts the i-th bit to the least significant position
            # & 1 checks if that bit is 1
            if (mask >> i) & 1:
                current_subset.append(arr[i])
        result.append(current_subset)

    return result


# ---------------------------------------------------------------------------
# Summary of Approaches:
# ---------------------------------------------------------------------------
# Approach            | Time Complexity  | Space Complexity | Key Idea
# --------------------|------------------|------------------|------------------
# Cascading (Iter.)   | O(n * 2^n)       | O(n * 2^n)       | Build subsets by
#                     |                  |                  | appending each
#                     |                  |                  | element to existing
#                     |                  |                  | subsets
# Backtracking (Rec.) | O(n * 2^n)       | O(n) [stack]     | Include/Exclude
#                     |                  |                  | each element via
#                     |                  |                  | recursion
# Bit Manipulation    | O(n * 2^n)       | O(n * 2^n)       | Map each subset
#                     |                  |                  | to a binary mask
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Example Usage
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    nums = [1, 2, 3]

    print("Array:", nums)
    print()

    print("Approach 1 (Cascading):")
    res1 = subsets_cascading(nums)
    print(res1)

    print("\nApproach 2 (Backtracking):")
    res2 = subsets_backtracking(nums)
    print(res2)

    print("\nApproach 3 (Bit Manipulation):")
    res3 = subsets_bit_manipulation(nums)
    print(res3)

    print()
    # Verify all approaches produce the same number of subsets
    expected_count = 1 << len(nums)  # 2^n
    print(f"Total subsets (expected): {expected_count}")
    print(f"Cascading count:     {len(res1)}")
    print(f"Backtracking count:  {len(res2)}")
    print(f"Bit Manip. count:    {len(res3)}")