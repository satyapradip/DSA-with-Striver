# Check if a LinkedList is Palindrome or Not
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def isPalindrome(head):
    if not head or not head.next:
        return True

    # Find the middle of the linked list
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half of the linked list
    prev = None
    current = slow

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    # Compare the first half with the reversed second half
    first_half = head
    second_half = prev

    while second_half:
        if first_half.data != second_half.data:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True

# Example usage
if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(2)
    head.next.next.next.next = Node(1)

    result = isPalindrome(head)
    print("Is the linked list a palindrome?", result)