# 📘 Linked List (Easy 08)
# Topic: Reorder Linked List
# Approach: Find middle → Reverse second half → Merge
# Time: O(n) | Space: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorder_list(head):
    """
    Reorder List: 1->2->3->4->5 becomes 1->5->2->4->3.
    """
    if not head or not head.next:
        return head

    # Find middle using slow and fast pointers
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    second = slow.next
    slow.next = None  # Break the link
    prev = None
    while second:
        next_node = second.next
        second.next = prev
        prev = second
        second = next_node
    second = prev

    # Merge first half and second half
    first = head
    while second:
        next_first = first.next
        next_second = second.next

        first.next = second
        second.next = next_first

        first = next_first
        second = next_second

    return head


def reorder_list_brute(head):
    """
    Brute force: O(n) space, O(n) time.
    Collect all nodes in array, then reorder.
    """
    if not head or not head.next:
        return head

    nodes = []
    curr = head
    while curr:
        nodes.append(curr)
        curr = curr.next

    # Reorder: 0->n-1, 1->n-2, 2->n-3, ...
    left = 0
    right = len(nodes) - 1
    while left < right:
        nodes[left].next = nodes[right]
        left += 1
        if left < right:
            nodes[right].next = nodes[left]
            right -= 1

    nodes[left].next = None
    return nodes[0]


if __name__ == "__main__":
    import unittest

    class TestReorderList(unittest.TestCase):
        def test_reorder_list(self):
            # 1->2->3->4->5
            head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
            reorder_list(head)
            self.assertEqual(head.val, 1)
            self.assertEqual(head.next.val, 5)
            self.assertEqual(head.next.next.val, 2)
            self.assertEqual(head.next.next.next.val, 4)
            self.assertEqual(head.next.next.next.next.val, 3)

        def test_reorder_list_4(self):
            # 1->2->3->4
            head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
            reorder_list(head)
            self.assertEqual(head.val, 1)
            self.assertEqual(head.next.val, 4)
            self.assertEqual(head.next.next.val, 2)
            self.assertEqual(head.next.next.next.val, 3)

    # Demo
    demo = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print("Original: 1->2->3->4->5")
    reorder_list(demo)
    print("Reordered: ", end="")
    curr = demo
    while curr:
        print(curr.val, end="->")
        curr = curr.next
    print("None")
    print("Running unit tests...")
    unittest.main(verbosity=0)