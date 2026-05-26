class Node:
  def __init__(self, data):
    self.data = data  # The data stored in the node
    self.next = None  # Reference to the next node in the list

def deleteFromEnd(head):
# if the list is empty or has only one node, return None
  if head is None:
    return None
  # if the list has only one node, delete it and return None
  if head.next is None:
    return None
  
  second_last = head # Start from the head of the list
  # Traverse the list until the second last node is reached
  while second_last.next.next is not None:
    second_last = second_last.next
  # Remove the reference to the last node
  second_last.next = None

  return head

def printList(head):
  current = head
  while current is not None:
    print(current.data, end="")
    if current.next is not None:
      print("->", end="")
    current = current.next
  print()
