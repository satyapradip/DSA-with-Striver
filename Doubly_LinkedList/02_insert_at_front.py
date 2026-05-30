class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

def insert_at_front(head, data):
  new_node = Node(data)
  new_node.next = head
  if head is not None: # If the list is not empty, set the previous pointer of the old head to the new node
    head.prev = new_node
  return new_node

def print_list(head):
  current = head
  while current is not None:
    print(current.data, end=' ')
    current = current.next
  print()

# Example usage
if __name__ == "__main__":
  head = Node(20)
  head.next = Node(30)
  head.next.prev = head
  print("Original list:")
  print_list(head)
  head = insert_at_front(head, 10)
  print("List after inserting 10 at the front:")
  print_list(head)