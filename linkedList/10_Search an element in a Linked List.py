# 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def searchElement(head, target):
    current = head 
    while current is not None:
        if current.data == target:
            return True
        current = current.next

    return False

if "__main__" == __name__:
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)

    target = 30
    found = searchElement(head, target)
    if found:
        print(f"Element {target} found in the linked list.")
    else:
        print(f"Element {target} not found in the linked list.")