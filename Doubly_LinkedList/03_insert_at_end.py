class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def insert_at_end(head, data):
    new_node = Node(data)
    if head is None:
        head = new_node
    else:
        current = head
        while current.next is not None:
            current = current.next
        current.next = new_node
        new_node.prev = current
        return head
    
def print_list(head):
    current = head
    while current is not None:
        print(current.data, end=' ')
        current = current.next
    print()

# Example usage
if __name__ == "__main__":
    head = Node(10)
    head.next = Node(20)
    head.next.prev = head
    print("Original list:")
    print_list(head)
    head = insert_at_end(head, 30)
    print("List after inserting 30 at the end:")
    print_list(head)