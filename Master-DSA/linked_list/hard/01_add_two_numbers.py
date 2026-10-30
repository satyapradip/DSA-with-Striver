# 📘 Linked List — Hard 01
# Topic: In-Place Manipulation — Add Two Numbers
# Approach: Simulate digit-by-digit addition with carry
# Time: O(max(n, m)) | Space: O(max(n, m))

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


def add_two_numbers(l1, l2):
    """
    Adds two numbers represented by linked lists.
    Each node contains a single digit, and digits are stored in reverse order.
    Returns the head of the sum linked list.
    """
    dummy = ListNode(0)
    tail = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10

        tail.next = ListNode(digit)
        tail = tail.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy.next


def add_two_numbers_brute(l1, l2):
    """
    Adds two numbers represented by linked lists using conversion to integers.
    """
    def linked_list_to_number(head):
        num = 0
        current = head
        while current:
            num = num * 10 + current.val
            current = current.next
        return num

    num1 = linked_list_to_number(l1)
    num2 = linked_list_to_number(l2)
    total = num1 + num2

    # Convert back to linked list
    if total == 0:
        return ListNode(0)

    dummy = ListNode(0)
    current = dummy
    for digit in str(total):
        current.next = ListNode(int(digit))
        current = current.next
    return dummy.next


if __name__ == "__main__":
    import unittest

    class TestAddTwoNumbers(unittest.TestCase):
        def test_basic(self):
            l1 = create_linked_list([2, 4, 3])  # 342
            l2 = create_linked_list([5, 6, 4])  # 465
            result = add_two_numbers(l1, l2)
            self.assertEqual(linked_list_to_array(result), [7, 0, 8])  # 807

        def test_with_carry(self):
            l1 = create_linked_list([9, 9, 9])  # 999
            l2 = create_linked_list([9, 9, 9])  # 999
            result = add_two_numbers(l1, l2)
            self.assertEqual(linked_list_to_array(result), [8, 9, 9, 1])  # 1998

        def test_different_lengths(self):
            l1 = create_linked_list([0])
            l2 = create_linked_list([0])
            result = add_two_numbers(l1, l2)
            self.assertEqual(linked_list_to_array(result), [0])

    # Demo
    l1 = create_linked_list([2, 4, 3])  # 342
    l2 = create_linked_list([5, 6, 4])  # 465
    print(f"Number 1: {linked_list_to_array(l1)} (342)")
    print(f"Number 2: {linked_list_to_array(l2)} (465)")
    result = add_two_numbers(l1, l2)
    print(f"Sum: {linked_list_to_array(result)} (807)")
    print("Running unit tests...")
    unittest.main(verbosity=0)
