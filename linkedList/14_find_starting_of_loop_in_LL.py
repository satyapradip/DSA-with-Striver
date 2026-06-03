class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def find_start_of_loop(head):
    """
    Finds the starting node of a loop in a linked list using 
    Floyd's Cycle-Finding Algorithm (Tortoise and Hare algorithm).
    """
    slow = head  # Slow pointer moves one step at a time
    fast = head  # Fast pointer moves two steps at a time
    
    # First, detect if there is a loop
    while fast and fast.next:
        slow = slow.next          # Move slow by 1 step
        fast = fast.next.next     # Move fast by 2 steps
        
        if fast == slow:          # Loop detected
            break
            
    # If no loop is detected, return None
    if not fast or not fast.next:
        return None
    
    # Move one pointer to the head and keep the other at the meeting point
    slow = head
    while slow != fast:
        slow = slow.next          # Move both pointers by 1 step
        fast = fast.next
        
    return slow  # Both pointers meet at the start of the loop\

def detect_cycle2(head):
    current = head
    seen = set()
    while current:
        if current in seen:
            return True
        seen.add(current)
        current = current.next

    return None

if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    # Create a loop: 5 -> 2 (pointing to the second node)
    head.next.next.next.next.next = head.next 
    # Find the starting node of the loop
    loop_start = find_start_of_loop(head)
    if loop_start:
        print("Starting node of the loop is:", loop_start.data)  # Expected: 2
    else:
        print("No loop detected.")