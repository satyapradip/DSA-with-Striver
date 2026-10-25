# 📘 Array Patterns — Easy 05
# Topic: Traversal & Basic Ops — Move Zeros to End
# Approach: Write pointer (two pointers)
# Time: O(n) | Space: O(1)

def move_zeros_to_end(arr):
    """
    Moves all zeros to the end while maintaining order of non-zero elements.
    In-place, O(1) extra space.
    """
    insert_pos = 0
    for num in arr:
        if num != 0:
            arr[insert_pos] = num
            insert_pos += 1

    while insert_pos < len(arr):
        arr[insert_pos] = 0
        insert_pos += 1

    return arr


def move_zeros_to_end_brute(arr):
    """
    Brute force: collect non-zeros, pad with zeros.
    """
    non_zeros = [num for num in arr if num != 0]
    zeros = [0] * (len(arr) - len(non_zeros))
    return non_zeros + zeros


if __name__ == "__main__":
    import unittest

    class TestMoveZeros(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(move_zeros_to_end([0, 1, 0, 3, 12]),
                             [1, 3, 12, 0, 0])

        def test_no_zeros(self):
            self.assertEqual(move_zeros_to_end([1, 2, 3]), [1, 2, 3])

        def test_all_zeros(self):
            self.assertEqual(move_zeros_to_end([0, 0, 0]), [0, 0, 0])

    # Demo
    demo = [0, 1, 0, 3, 12]
    print(f"Input: {demo}")
    print(f"After moving zeros: {move_zeros_to_end(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
