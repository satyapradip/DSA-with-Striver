# 📘 Linked List — Easy 02
# Topic: Singly Linked List — Traversal
# Approach: Iterative and recursive traversal

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


def print_linked_list_recursive(head):
    """
    Prints the linked list using recursion.
    """
    if not head:
        return
    print(head.val, end=" -> " if head.next else "\n")
    print_linked_list_recursive(head.next)


def iterate_linked_list(head):
    """
    Iteratively prints all node values.
    """
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next


def count_nodes_recursive(head):
    """
    Returns the count of nodes using recursion.
    """
    if not head:
        return 0
    return 1 + count_nodes_recursive(head.next)


def count_nodes_iterative(head):
    """
    Returns the count of nodes using iteration.
    """
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count


def sum_of_values(head):
    """
    Returns the sum of all node values.
    """
    total = 0
    current = head
    while current:
        total += current.val
        current = current.next
    return total


def print_reversed_recursive(head):
    """
    Prints the linked list in reverse order using recursion.
    """
    if not head:
        return
    print_reversed_recursive(head.next)
    print(head.val, end=" -> " if head.next else "\n")


if __name__ == "__main__":
    import unittest

    class TestLinkedListTraversal(unittest.TestCase):
        def test_iterative_traversal(self):
            head = create_linked_list([1, 2, 3, 4, 5])
            result = linked_list_to_array(head)
            self.assertEqual(result, [1, 2, 3, 4, 5])

        def test_recursive_traversal(self):
            import io
            from contextlib import redirect_stdout
            head = create_linked_list([1, 2, 3])
            buf = io.StringIO()
            with redirect_stdout(buf):
                print_linked_list_recursive(head)
            output = buf.getvalue().strip()
            self.assertIn("1 -> 2 -> 3", output)

        def test_count_nodes(self):
            head = create_linked_list([1, 2, 3, 4])
            self.assertEqual(count_nodes_iterative(head), 4)
            self.assertEqual(count_nodes_recursive(head), 4)

        def test_sum_of_values(self):
            head = create_linked_list([1, 2, 3, 4])
            self.assertEqual(sum_of_values(head), 10)

    # Demo
    demo = [1, 2, 3, 4, 5]
    head = create_linked_list(demo)
    print(f"Linked List: {linked_list_to_array(head)}")
    print("Iterative traversal:")
    iterate_linked_list(head)
    print("\nRecursive traversal:")
    print_linked_list_recursive(head)
    print(f"\nNumber of nodes: {count_nodes_iterative(head)}")
    print(f"Sum of values: {sum_of_values(head)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
