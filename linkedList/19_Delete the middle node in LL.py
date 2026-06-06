# Delete middle node in a linked list
# Examples:
# Input: head = [1,2,3,4,5]
# Output: [1,2,4,5]
# Explanation: The middle node with value 3 is removed.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteMiddleNode(head):
    # Edge Case: If the list is empty or has only one node, return None
    if head is None or head.next is None:
        return None

    slow = head  # This will eventually point to the middle node
    fast = head  # This will move twice as fast as slow
    prev = None  # To keep track of the node before slow

    # Move fast pointer two steps and slow pointer one step until fast reaches the end
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    # Now, slow is at the middle node, and prev is the node before it
    prev.next = slow.next  # Skip the middle node

    return head  # Return the head of the modified list


if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    
    # Delete the middle node
    head = deleteMiddleNode(head)
    
