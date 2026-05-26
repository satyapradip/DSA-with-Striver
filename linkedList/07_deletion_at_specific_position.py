# Single Traversal Deletion - O(n) Time and O(1) Space

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
def deleteAtSpecificPosition(head, position):
  # Function to delete a node at a given 0-indexed position
  # Edge Case 1: Invalid negative position
  if position < 0:
    print("Invalid Position!")
    return head
  
  # Edge Case 2: Deleting the head node (position 0)
  if position == 0:
    return head.next # The new head is the next node
  
  current = head # Start traversing from the head
  
  # Step 1: Traverse to the node *just before* the deletion point 
  for i in range(position - 1):
    if current is None:
      # If we reach None before finishing the loop, the position is greater than the list length
      print("Position out of bounds!")
      return head
    current = current.next 

  # Edge Case 3: If current is None after the loop, position is out of bounds
  if current is None or current.next is None:
    print("Position out of bounds!")
    return head

  # Step 2: Delete the node
  # We skip over the node at 'position' by pointing current's next to the node after it
  current.next = current.next.next 

  return head # Return the (possibly unchanged) head of the list


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

  # Delete node at position 2 (0-indexed, which is the node with value 30)
  head = deleteAtSpecificPosition(head, 2)

  print("List after deleting node at position 2:")
  printList(head)