# 📘 Linked List (Easy 07)
# Topic: Two pointers, k-group reversal
# Approach: Recursive k-group reversal
# Time: O(n) | Space: O(n/k) recursion stack

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_k_group(head, k):
    """
    Reverse nodes in k-group. If remainder is less than k, leave as is.
    """
    # Check if there are at least k nodes left
    curr = head
    for _ in range(k):
        if not curr:
            return head
        curr = curr.next

    # Reverse k nodes
    prev = None
    curr = head
    for _ in range(k):
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    # Recursively reverse the next k-group and connect
    if curr:
        head.next = reverse_k_group(curr, k)

    return prev


def reverse_k_group_iterative(head, k):
    """
    Reverse nodes in k-group using iterative approach.
    """
    if not head or k == 1:
        return head

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    while True:
        # Check if there are k nodes remaining
        kth = prev
        for _ in range(k):
            kth = kth.next
            if not kth:
                return dummy.next

        # Reverse k nodes
        curr = kth.next
        prev.next = reverse_sublist(prev.next, curr)

        # Move prev to end of reversed sublist
        for _ in range(k):
            prev = prev.next

    return dummy.next


def reverse_sublist(start, end):
    """
    Reverse sublist from start to end (exclusive).
    """
    prev = end
    curr = start
    while curr != end:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


def reverse_k_group_brute(head, k):
    """
    Brute force: O(n*k) time, O(1) space.
    """
    if not head or k == 1:
        return head

    # Count total nodes
    count = 0
    curr = head
    while curr:
        count += 1
        curr = curr.next

    dummy = ListNode(0, head)
    prev = dummy

    while count >= k:
        curr = prev.next
        for _ in range(k - 1):
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = prev.next
        prev = curr
        count -= k

    return dummy.next


if __name__ == "__main__":
    import unittest

    class TestReverseKGroup(unittest.TestCase):
        def test_reverse_k_group(self):
            # 1->2->3->4->5, k=2
            # Expected: 2->1->4->3->5
            head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
            result = reverse_k_group(head, 2)
            self.assertEqual(result.val, 2)
            self.assertEqual(result.next.val, 1)
            self.assertEqual(result.next.next.val, 4)

        def test_reverse_k_group_3(self):
            # 1->2->3->4->5, k=3
            # Expected: 3->2->1->4->5
            head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
            result = reverse_k_group(head, 3)
            self.assertEqual(result.val, 3)
            self.assertEqual(result.next.val, 2)
            self.assertEqual(result.next.next.val, 1)
            self.assertEqual(result.next.next.next.val, 4)

    # Demo
    demo = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print("Original: 1->2->3->4->5")
    print("k=2:", end=" ")
    result = reverse_k_group(demo, 2)
    curr = result
    while curr:
        print(curr.val, end="->")
        curr = curr.next
    print("None")
    print("Running unit tests...")
    unittest.main(verbosity=0)