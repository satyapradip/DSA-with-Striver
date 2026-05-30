class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def insert_at_position(head, data, position):
    new_node = Node(data)
    if position == 0:
        new_node.next = head
        if head is not None:
            head.prev = new_node
        head = new_node
        return head
    
    current = head
    for _ in range(position - 1):
        if current is None:
            raise IndexError("Position out of bounds")
        current = current.next
    if current is None:
        raise IndexError("Position out of bounds")
    new_node.next = current.next # Set the next pointer of the new node to the next node of the current node
    new_node.prev = current # Set the previous pointer of the new node to the current node
    if current.next is not None: # If the current node is not the last node, set the previous pointer of the next node to the new node
        current.next.prev = new_node # Set the next pointer of the current node to the new node
    current.next = new_node # Set the next pointer of the current node to the new node
    return head # Return the head of the list after insertion

def print_list(head):
    current = head
    while current is not None:
        print(current.data, end=' ')
        current = current.next
    print()

# Example usage
if __name__ == "__main__":
    head = Node(10)
    head.next = Node(30)
    head.next.prev = head
    print("Original list:")
    print_list(head)
    head = insert_at_position(head, 20, 1)
    print("List after inserting 20 at position 1:")
    print_list(head)