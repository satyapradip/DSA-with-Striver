# Sort a Linked List
# Example 1:
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
# Example 2:
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]

# Approach : Merge Sort

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def sortLinkedList(head):
    if head is None or head.next is None:
        return head

    # Split the linked list into halves
    def split(head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow.next
        slow.next = None  # Split the linked list into two halves
        return head, middle

    # Merge two sorted linked lists
    def merge(left, right):
        dummy = Node(0) # Dummy node to help with merging
        tail = dummy # Tail pointer to build the merged list21
        while left and right:
            if left.data < right.data:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        tail.next = left or right  # Append the remaining nodes
        return dummy.next

    # Recursively split and merge the linked list
    left_half, right_half = split(head)
    left_sorted = sortLinkedList(left_half)
    right_sorted = sortLinkedList(right_half)
    return merge(left_sorted, right_sorted)

if __name__ == "__main__":
    # Create a linked list: 4 -> 2 -> 1 -> 3
    head = Node(4)
    head.next = Node(2)
    head.next.next = Node(1)
    head.next.next.next = Node(3)

    # Sort the linked list
    sorted_head = sortLinkedList(head)

    # Print the sorted linked list
    current = sorted_head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()  # Output: 1 2 3 4
