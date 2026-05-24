class Node:
  # A class to represent an individual node in the linked list
  def __init__(self, data):
    self.data = data # Store the actual data value
    self.next = None # Pointer to the next node, initialized to None (end of list)

def insertAtEnd(head, data):
  # Function to insert a new node at the tail/end of the linked list
  new_node = Node(data) # Step 1: Create the new node with the given data

  if head is None: 
    # Edge case: If the list is completely empty, the new node itself becomes the head
    return new_node
  
  current = head # Start our traversal from the head of the list
  
  # Step 2: Traverse the list until we reach the VERY LAST node
  # We check 'current.next is not None' because we want to STOP directly ON the last node, 
  # not fall off the edge of the list.
  while current.next is not None:
    current = current.next # Move to the next node
    
  # Step 3: Now 'current' is the last node. Point its 'next' property to our new node.
  current.next = new_node 
  
  return head # Return the original head of the list (which hasn't changed)

def printList(head):
  # Function to traverse and print all elements in the linked list
  current = head
  while current is not None:
    print(current.data, end="")
    if current.next is not None:
      print("-->", end="") # Print an arrow if there is another node ahead
    current = current.next # Advance to the next node
  print() # Move to the next line after the entire list is printed

if __name__ == "__main__":
  # Manually creating a linked list: 10 --> 20 --> 30
  head = Node(10)
  head.next = Node(20)
  head.next.next = Node(30)

  print("Original List:")
  printList(head)

  # Insert 40 at the end. We still catch the return value in 'head' just in case the list was empty.
  head = insertAtEnd(head, 40)

  print("List after inserting at the end:")
  printList(head)