class Node:
  # A class to represent an individual node in the linked list
  def __init__(self, data):
    self.data = data # Store the data inside the node
    self.next = None # Initialize the next pointer to None (meaning it doesn't point to anything yet)

def insertAtBeginning(head, data):
  # Function to insert a new node at the start of the linked list
  new_node = Node(data) # Step 1: Create a new node object with the given data
  new_node.next = head  # Step 2: Make the new node's next pointer point to the current head of the list
  return new_node       # Step 3: Return the new node so it becomes the new head of the list

def printList(head):
  # Function to traverse and print all elements in the linked list
  current = head # Start our traversal from the head node
  while current is not None: # Loop until we reach the end of the list (where current becomes None)
    print(current.data, end="") # Print the current node's data, keeping it on the same line
    
    if current.next is not None: # Check if there is another node after this one
      print("-->", end="")       # If so, print an arrow to connect them visually
      
    current = current.next # MOVE THIS OUTSIDE THE IF: Advance to the next node regardless of whether an arrow was printed
  
  print() # Move to the next line after the entire list is printed

if __name__ == "__main__":
  # Manually creating a linked list: 10 --> 20 --> 30
  head = Node(10)
  head.next = Node(20)
  head.next.next = Node(30)

  print("Original List:")
  printList(head) # Call printList to show the original state

  # Insert 5 at the beginning. We must reassign 'head' to the value returned by the function!
  head = insertAtBeginning(head, 5)

  print("List after inserting at the beginning:")
  printList(head) # Call printList to show the updated state