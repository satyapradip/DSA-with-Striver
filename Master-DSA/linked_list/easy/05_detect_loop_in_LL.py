# 📘 Linked List — Easy 05
# Topic: Fast & Slow Pointers — Detect Cycle in Linked List
# Approach: Floyd's Cycle Detection (tortoise and hare)
# Time: O(n) | Space: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list_with_loop(arr, pos):
    """
    Creates a linked list with a loop at position `pos`.
    If pos = -1, no loop is created.
    """
    if not arr:
        return None
    nodes = [ListNode(val) for val in arr]
    for i in range(len(arr) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1 and pos < len(arr):
        nodes[-1].next = nodes[pos]
    return nodes[0]


def has_cycle(head):
    """
    Returns True if there is a cycle in the linked list.
    Uses Floyd's Cycle Detection algorithm.
    """
    if not head or not head.next:
        return False
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def detect_cycle_start(head):
    """
    Returns the node where the cycle begins.
    Returns None if no cycle.
    """
    if not head or not head.next:
        return None

    slow = fast = head
    has_cycle = False

    # Phase 1: Detect cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break

    if not has_cycle:
        return None

    # Phase 2: Find cycle start
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


def get_cycle_length(head):
    """
    Returns the length of the cycle, or 0 if no cycle.
    """
    if not head or not head.next:
        return 0

    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # Count cycle length
            length = 1
            temp = slow.next
            while temp != slow:
                length += 1
                temp = temp.next
            return length
    return 0


if __name__ == "__main__":
    import unittest

    class TestCycleDetection(unittest.TestCase):
        def test_no_cycle(self):
            head = create_linked_list_with_loop([1, 2, 3, 4, 5], -1)
            self.assertFalse(has_cycle(head))

        def test_cycle_exists(self):
            head = create_linked_list_with_loop([1, 2, 3, 4, 5], 1)
            self.assertTrue(has_cycle(head))

        def test_cycle_at_start(self):
            head = create_linked_list_with_loop([1, 2, 3, 4, 5], 0)
            self.assertTrue(has_cycle(head))

        def test_cycle_start_position(self):
            head = create_linked_list_with_loop([3, 2, 0, -4], 1)
            cycle_start = detect_cycle_start(head)
            self.assertEqual(cycle_start.val, 2)

        def test_cycle_length(self):
            head = create_linked_list_with_loop([1, 2, 3, 4, 5], 1)
            self.assertEqual(get_cycle_length(head), 4)

    # Demo
    demo_arr = [1, 2, 3, 4, 5]
    demo_pos = 1
    head = create_linked_list_with_loop(demo_arr, demo_pos)
    print(f"Linked List: {demo_arr}, loop at pos {demo_pos}")
    print(f"Has cycle: {has_cycle(head)}")
    if has_cycle(head):
        print(f"Cycle starts at: {detect_cycle_start(head).val}")
        print(f"Cycle length: {get_cycle_length(head)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
