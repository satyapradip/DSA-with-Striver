# Operations in Singly Linked List
class Node:
  def __init__(self, data):
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None

  def insertAtBegining(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def inserAtEnd(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    current = self.head 
    while current.next:
      current = current.next
    current = new_node

  def insertAtPosition(self, position, data):
    if position < 0:
      print("Invalid Position!")
      return 
    new_node = Node(data)
    if position == 0:
      new_node.next = self.head
      self.head = new_node
      return
    current = self.head
    count = 0
    while current and count < position - 1:
      current = current.next
      count += 1
    if not current:
      print("position out of bounds!")
      return
    new_node.next = current.next
    current.next = new_node

  def printList(self):
    current = self.head
    while current:
      print(current.data, end="-->")
      current = current.next
    print("None")

if __name__ == "__main__":
  ll = LinkedList()
  ll.insertAtBegining(10)
  ll.insertAtBegining(20)
  ll.inserAtEnd(30)
  ll.insertAtPosition(1, 15)
  ll.printList()