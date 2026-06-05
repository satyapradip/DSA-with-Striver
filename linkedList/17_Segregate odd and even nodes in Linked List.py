# Odd Even Linked List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def segregateOddEven(head):
    if not head or not head.next:
        return head
    odd = head
    even = head.next
    even_head = even
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = even_head
    return head

if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> None
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Original linked list:")
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

    # Segregate odd and even nodes
    head = segregateOddEven(head)

    print("Linked list after segregating odd and even nodes:")
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")