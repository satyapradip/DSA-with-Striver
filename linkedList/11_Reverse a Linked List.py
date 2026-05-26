#Using Iterative Method - O(n) Time and O(1) Space
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def reverseLinkedList(head):
    prev = None # Initialize previous pointer to None
    current = head # Start with the head of the list

    while current is not None:
        next_node = current.next # Store the next node
        current.next = prev # Reverse the current node's pointer
        prev = current # Move the previous pointer to the current node
        current = next_node # Move to the next node in the original list

    return prev # At the end, prev will be the new head of the reversed list

def printList(head):
    current = head
    while current is not None:
        print(current.data, end="")
        if current.next is not None:
            print("->", end="")
        current = current.next
    print()
if __name__ == "__main__":
    # Create a linked list: 10 -> 20 -> 30 -> 40
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)

    print("Original List:")
    printList(head)

    # Reverse the linked list
    head = reverseLinkedList(head)

    print("Reversed List:")
    printList(head)

#----------- Using Recursive Method - O(n) Time and O(n) Space------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseLinkedList(head):
    if head is None and head.next is None: 
        return head
    rest = reverseLinkedList(head.next) # Reverse the rest of the list and get the new head (rest will be the new head of the reversed list)
    head.next.next = head # Make the next node point back to the current node (reverse the link)
    head.next = None # Set the current node's next to None (it will become the new tail of the reversed list)
    return rest 

def printList(head):
    current = head
    while current is not None:
        print(current.data, end="")
        if current.next is not None:
            print("->", end="")
        current = current.next
    print()

if __name__ == "__main__":
    # Create a linked list: 10 -> 20 -> 30 -> 40
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)

    print("Original List:")
    printList(head)

    # Reverse the linked list
    head = reverseLinkedList(head)

    print("Reversed List:")
    printList(head)

# 