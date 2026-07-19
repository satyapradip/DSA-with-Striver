# Check if string is palindrome using recursion (two-pointer approach)
def is_palindrome(s, left, right):
    # Base case: all characters checked
    if left >= right:
        return True
    # Mismatch found
    if s[left] != s[right]:
        return False
    # Recursive call with updated pointers
    return is_palindrome(s, left + 1, right - 1)


# Alternative: single pointer approach (more compact)
def is_palindrome_single_ptr(s, i=0):
    n = len(s)
    # Base case: reached middle
    if i >= n // 2:
        return True
    # Compare symmetric characters
    if s[i] != s[n - 1 - i]:
        return False
    return is_palindrome_single_ptr(s, i + 1)


if __name__ == "__main__":
    test_cases = ["racecar", "hello", "madam", "a", ""]
    for word in test_cases:
        result = is_palindrome_single_ptr(word, 0)
        print(f"'{word}' -> {result}")