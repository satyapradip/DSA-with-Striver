class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def detect_loop(head):
    """
    Detects if there is a cycle (loop) in a linked list using 
    Floyd's Cycle-Finding Algorithm (Tortoise and Hare algorithm).
    """
    slow = head  # Slow pointer moves one step at a time
    fast = head  # Fast pointer moves two steps at a time
    
    # Traverse the list until fast pointer reaches the end
    while fast and fast.next:
        slow = slow.next          # Move slow by 1 step
        fast = fast.next.next     # Move fast by 2 steps
        
        # If slow and fast pointers meet, there is a cycle
        if fast == slow:
            return True
            
    # If fast reaches Null, there's no cycle
    return False 

if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    # Test case 1: Linked list without a loop
    print("Loop detected:", detect_loop(head))  # Expected: False

    # Test case 2: Form a loop to test (5 -> 3)
    head.next.next.next.next.next = head.next.next
    
    # Check again after creating the loop
    print("Loop detected after modification:", detect_loop(head))  # Expected: True