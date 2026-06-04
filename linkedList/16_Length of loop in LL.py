# Length of loop in Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def countNodesinLoop(head):
    slow = head
    fast = head

    while slow and fast and fast.next: # Check if slow and fast pointers are valid and fast has a next node
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            count = 1 # Start counting from the meeting point
            temp = slow # Use a temporary pointer to traverse the loop
            while temp.next != slow: # Traverse until we come back to the meeting point
                temp = temp.next  # Move to the next node in the loop
                count += 1
            return count

    return 0

# Example usage
if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = head.next  # Creating a loop

    loop_length = countNodesinLoop(head)
    print("Length of the loop in the linked list:", loop_length)
