class Node:
  """
  A class to represent a node in a singly linked list.
  """
  def __init__(self, data):
    self.data = data  # The data stored in the node
    self.next = None  # Reference to the next node in the list

def deleteFromBeginning(head):
  """
  Function to delete the first node of the linked list.
  Returns the new head of the linked list.
  """
  # If the list is empty, there is nothing to delete
  if head is None:
    return None
  
  # Store the current head to delete it later
  current = head 

  # Move the head pointer to the next node
  head = head.next

  # Remove the reference of the old head (optional in Python due to garbage collection, but good practice)
  current = None

  return head

def printList(head):
  """
  Function to print the elements of the linked list.
  """
  current = head
  while current is not None:
    print(current.data, end="")
    if current.next is not None:
      print("->", end="")
    current = current.next
  print()

if __name__ == "__main__":
  # Create a linked list: 10 -> 20 -> 30
  head = Node(10)
  head.next = Node(20)
  head.next.next = Node(30)

  print("Original List:")
  printList(head)

  # Delete the first node
  head = deleteFromBeginning(head)

  print("List after deleting from the beginning:")
  printList(head)