class Node:
  # A class to represent an individual node in the linked list
  def __init__(self, data):
    self.data = data
    self.next = None

def insertAtSpecificPosition(head, position, data):
  # Function to insert a new node at a given 0-indexed position
  new_node = Node(data) # Step 1: Create the new node

  # Edge Case 1: Invalid negative position
  if position < 0:
    print("Invalid Position!")
    return head
  
  # Edge Case 2: Inserting exactly at the physical start (index 0)
  if position == 0:
    new_node.next = head # The new node points to the old head
    return new_node      # The new node becomes the new head
  
  current = head # Start traversing from the head
  
  # Step 2: Traverse to the node *just before* the insertion point 
  # We loop (position - 1) times because we need the node preceding the target index
  for i in range(position - 1):
    if current is None:
      # If we reach None before finishing the loop, the position is greater than the list length
      print("Position out of bounds!")
      return head
    current = current.next

  # Edge Case 3: If current is None after the loop, position is out of bounds
  if current is None:
    print("Position out of bounds!")
    return head

  # Step 3: Insert the node
  # First, point the new node's next to the node that currently occupies the target position
  new_node.next = current.next 
  
  # Then, update the previous node's next to point to our newly created node
  current.next = new_node

  return head # Head hasn't changed (since position > 0), return original head

def printList(head):
  # Function to visually print the linked list
  current = head
  while current is not None:
    print(current.data, end="")
    if current.next is not None:
      print("-->", end="")
    current = current.next
  print()

if __name__ == "__main__":
  # Initial list: 10 --> 20 --> 30
  head = Node(10)
  head.next = Node(20)
  head.next.next = Node(30)

  print("Original List:")
  printList(head)

  # Insert 15 at position 1 (between 10 and 20)
  # List becomes 10 --> 15 --> 20 --> 30
  head = insertAtSpecificPosition(head, 1, 15) 

  print("List after inserting at position 1:")
  printList(head)

  # Insert 5 at position 0 (at the beginning)
  # List becomes 5 --> 10 --> 15 --> 20 --> 30
  head = insertAtSpecificPosition(head, 0, 5) 

  print("List after inserting at position 0:")
  printList(head)

  # Insert 35 at position 5 (at the end of the current length of 5)
  # List becomes 5 --> 10 --> 15 --> 20 --> 30 --> 35
  head = insertAtSpecificPosition(head, 5, 35) 

  print("List after inserting at position 5:")
  printList(head)