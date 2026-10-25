# 📘 Array Patterns — Easy 06
# Topic: Two Pointers — Union of Two Sorted Arrays
# Approach: Two-pointer merge + dedup
# Time: O(n + m) | Space: O(n + m)

def union_of_two_sorted(arr1, arr2):
    """
    Returns union of two sorted arrays (sorted, without duplicates).
    """
    i, j = 0, 0
    n, m = len(arr1), len(arr2)
    result = []

    while i < n and j < m:
        if arr1[i] < arr2[j]:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            if not result or result[-1] != arr2[j]:
                result.append(arr2[j])
            j += 1
        else:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
            j += 1

    # Remaining elements
    while i < n:
        if not result or result[-1] != arr1[i]:
            result.append(arr1[i])
        i += 1

    while j < m:
        if not result or result[-1] != arr2[j]:
            result.append(arr2[j])
        j += 1

    return result


def union_of_two_sorted_brute(arr1, arr2):
    """
    Brute force: concatenate + set + sort.
    """
    return sorted(set(arr1 + arr2))


if __name__ == "__main__":
    import unittest

    class TestUnionSorted(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(union_of_two_sorted([1, 2, 3, 4, 5], [1, 2, 3, 6]),
                             [1, 2, 3, 4, 5, 6])

        def test_with_duplicates(self):
            self.assertEqual(union_of_two_sorted([2, 2, 3], [2, 4]),
                             [2, 3, 4])

        def test_empty(self):
            self.assertEqual(union_of_two_sorted([], [1, 2]), [1, 2])

    # Demo
    demo1 = [1, 2, 3, 4, 5]
    demo2 = [1, 2, 3, 6]
    print(f"Input: {demo1} U {demo2}")
    print(f"Union: {union_of_two_sorted(demo1, demo2)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
