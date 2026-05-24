# Traversal of Singly Linked List (Iterative Approach)
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def traverseList(head):
  while head is not None:
    print(head.data, end="")
    if head.next is not None:
      print("-->", end = "")
  
    head = head.next

  print() # Move to the next line after traversal is complete

# Example Usage
if __name__ == "__main__":
  # Creating a linked list with 3 nodes
  head = Node(1)
  second = Node(2)
  third = Node(3)

  head.next = second
  second.next = third

  # Traversing the linked list
  print("Traversal of the linked list:")
  traverseList(head)


# Traversal of Singly Linked List (Recursive Approach)
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def traverseList(head):
  if head is None: # Base case: If the head is None, we have reached the end of the list. Just print a newline and return.
    print()
    return 
  print(head.data, end="") # Print the current node's data without moving to the next line.
  if head.next is not None: # If there is a next node, print the arrow before the recursive call.
    print("-->", end="")
  traverseList(head.next) # Recursive call to traverse the rest of the list starting from the next node.

if __name__ == "__main__":
  head = Node(10)
  head.next = Node(20)
  head.next.next = Node(30)
  head.next.next.next = Node(50)

  traverseList(head)

