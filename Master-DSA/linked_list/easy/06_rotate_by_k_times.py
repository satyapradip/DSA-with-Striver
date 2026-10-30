# 📘 Linked List — Easy 06
# Topic: Singly Linked List — Rotate by K Times
# Approach: Rotation using tail-to-head linking
# Time: O(n) | Space: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_array(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


def rotate_linked_list(head, k):
    """
    Rotates the linked list to the right by k places.
    Returns the new head.
    """
    if not head or not head.next or k == 0:
        return head

    # Find length and tail
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    # Connect tail to head to make it circular
    tail.next = head

    # Find new tail (length - k % length - 1 steps from head)
    k = k % length
    new_tail_position = length - k
    new_tail = head
    for _ in range(new_tail_position - 1):
        new_tail = new_tail.next

    # New head is new_tail.next
    new_head = new_tail.next
    new_tail.next = None  # Break the cycle

    return new_head


def rotate_left_by_k(head, k):
    """
    Rotates the linked list to the left by k places.
    Returns the new head.
    """
    if not head or not head.next or k == 0:
        return head

    # Find length and tail
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    # Make it circular
    tail.next = head

    # Find new tail (k % length - 1 steps)
    k = k % length
    new_tail = head
    for _ in range(k - 1):
        new_tail = new_tail.next

    # New head is new_tail.next
    new_head = new_tail.next
    new_tail.next = None

    return new_head


if __name__ == "__main__":
    import unittest

    class TestRotateLL(unittest.TestCase):
        def test_rotate_right(self):
            head = create_linked_list([1, 2, 3, 4, 5])
            new_head = rotate_linked_list(head, 2)
            self.assertEqual(linked_list_to_array(new_head), [4, 5, 1, 2, 3])

        def test_rotate_left(self):
            head = create_linked_list([1, 2, 3, 4, 5])
            new_head = rotate_left_by_k(head, 2)
            self.assertEqual(linked_list_to_array(new_head), [3, 4, 5, 1, 2])

        def test_rotate_by_length(self):
            head = create_linked_list([1, 2, 3])
            new_head = rotate_linked_list(head, 3)
            self.assertEqual(linked_list_to_array(new_head), [1, 2, 3])

        def test_rotate_by_multiple_of_length(self):
            head = create_linked_list([1, 2, 3])
            new_head = rotate_linked_list(head, 5)  # 5 % 3 = 2
            self.assertEqual(linked_list_to_array(new_head), [2, 3, 1])

    # Demo
    demo = [1, 2, 3, 4, 5]
    k = 2
    head = create_linked_list(demo)
    print(f"Original: {linked_list_to_array(head)}")
    print(f"Rotated right by {k}: {linked_list_to_array(rotate_linked_list(head, k))}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
