# Operations in Singly Linked List

class Node:
  """
  A Node is a single block of memory in the linked list. 
  It holds the data and points to the next node.
  """
  def __init__(self, data):
    self.data = data  # The value we want to store
    self.next = None  # FIXED BUG: You had 'self.next = next'. 'next' is a Python keyword. It should default to None.

class LinkedList:
  """
  The LinkedList class manages the nodes. It supports operations like 
  inserting at the beginning, end, or a specific position.
  """
  def __init__(self):
    self.head = None  # List starts initially empty

  def insertAtBeginning(self, data):
    """
    Inserts a new node at the very beginning (index 0). 
    Time Complexity: O(1) - Very fast because we don't have to traverse the list.
    """
    new_node = Node(data)      # Step 1: Create the new node
    new_node.next = self.head  # Step 2: The new node points to the current head (old first node)
    self.head = new_node       # Step 3: Update the head to be the new node

  def insertAtEnd(self, data):
    """
    Inserts a new node at the very end of the list.
    Time Complexity: O(N) - We have to travel through the whole list to find the end.
    """
    new_node = Node(data)      # Step 1: Create the new node
    
    # Special Case: If the list is empty, just make the new node the head
    if self.head is None:
      self.head = new_node
      return
      
    # Normal Case: Travel down the list to find the last node
    current = self.head 
    while current.next:        # Stop when 'current.next' is None (meaning 'current' is the last node)
      current = current.next
      
    # Step 2: We are now at the last node. Point its 'next' to the new_node.
    current.next = new_node    # FIXED BUG: You had 'current = new_node', which only updated a local variable.

  def insertAtPosition(self, position, data):
    """
    Inserts a new node at a specific index (0-based position).
    Time Complexity: O(N) - We have to travel to reach the specific position.
    """
    if position < 0:
      print("Invalid Position!")
      return 
      
    new_node = Node(data)
    
    # Inserting at position 0 is exactly the same as insertAtBeginning
    if position == 0:
      new_node.next = self.head
      self.head = new_node
      return
      
    current = self.head
    count = 0
    
    # Travel until we reach the node right BEFORE our target position (position - 1)
    while current and count < position - 1:
      current = current.next
      count += 1
      
    # If we reached the end of the list before finding the position
    if not current:
      print("Position out of bounds!")
      return
      
    # Step 1: Connect our new node to the node that is currently sitting at our target position
    new_node.next = current.next
    
    # Step 2: Connect the previous node to our new node
    current.next = new_node

  def printList(self):
    """
    Travels through the entire list and prints every node's data.
    """
    current = self.head
    while current:
      print(current.data, end="-->")
      current = current.next
    print("None")

if __name__ == "__main__":
  ll = LinkedList()
  ll.insertAtBeginning(10)   # List: 10-->None
  ll.insertAtBeginning(20)   # List: 20-->10-->None
  ll.insertAtEnd(30)         # List: 20-->10-->30-->None (note: updated typo inserAtEnd -> insertAtEnd)
  ll.insertAtPosition(1, 15) # List: 20-->15-->10-->30-->None
  ll.printList()             # Output: 20-->15-->10-->30-->None