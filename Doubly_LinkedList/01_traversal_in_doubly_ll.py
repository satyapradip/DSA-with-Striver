class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def traverse_forward(head):
    current = head
    while current is not None:
        print(current.data, end=' ')
        current = current.next
    print()

def traverse_forward_recursive(head):
    if head is None:
        return
    print(head.data, end=' ')
    traverse_forward_recursive(head.next)

def traverse_backward(tail):
    current = tail
    while current is not None:
        print(current.data, end=" ")
        current = current.prev
    print()

def traverse_backward_recursive(tail):
    if tail is None:
        return 
    print(tail.data, end=' ')
    traverse_backward_recursive(tail.prev)

# Example usage
if __name__ == "__main__":
    # Create nodes
    head = Node(10)
    second = Node(20)
    third = Node(30)

    head.next = second
    second.prev = head
    second.next = third
    third.prev = second
    print("\nForward Traversal (Iterative):")
    traverse_forward(head)
    print("\nForward Traversal (Recursive):")
    traverse_forward_recursive(head)
    print("\nBackward Traversal (Iterative):")
    traverse_backward(third)
    print("\nBackward Traversal (Recursive):")
    traverse_backward_recursive(third)
