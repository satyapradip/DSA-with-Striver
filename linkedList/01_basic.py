# Singly Linked List Implementation

class Node:
  """
  A Node represents a single element/building block in the linked list.
  It contains the actual data and a reference (pointer) to the next node.
  """
  def __init__(self, data):
    self.data = data  # The value stored in this node
    self.next = None  # Pointer to the next node (None by default)

class LinkedList:
  """
  The LinkedList class manages all the nodes.
  It keeps track of the 'head' (the very first node in the sequence).
  """
  def __init__(self):
    self.head = None  # Initially, the list is empty, so head is None
    
  def print_list(self):
    """
    Traverses the linked list starting from the head
    and prints each node's data in order.
    """
    current = self.head  # Start walking from the first node
    while current:       # Keep going as long as the current node exists (not None)
      print(current.data, end ="-->")
      current = current.next  # Move the pointer to the next node
    print("None")        # Indicate the end of the list

if __name__ == "__main__":
  # 1. Create an empty Linked List
  my_list = LinkedList()

  # 2. Create independent nodes with data
  my_list.head = Node(1)  # Create the first node and make it the head
  second = Node(2)        # Create the second node
  third = Node(3)         # Create the third node

  # 3. Link the nodes together
  my_list.head.next = second  # Link the first node to the second node
  second.next = third         # Link the second node to the third node

  # 4. Print the resulting linked list
  my_list.print_list()