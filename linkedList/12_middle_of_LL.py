class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_middle(head):
    if head is None:
        return None
    slow = head
    fast = head 

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data

# Example usage
if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    print(find_middle(head))