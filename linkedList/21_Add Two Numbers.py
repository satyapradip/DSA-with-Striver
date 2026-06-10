class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a dummy node to act as the starting point of our result list.
        # This helps us avoid edge cases when the list is empty.
        dummy = ListNode()
        current = dummy  # 'current' will build the new list
        carry = 0        # 'carry' holds the overflow when sum >= 10
        
        # Keep looping as long as there are nodes in l1, nodes in l2, OR a carry leftover
        while l1 is not None or l2 is not None or carry > 0:
            # Get the values from the current nodes, or 0 if we've reached the end of a list
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            
            # Calculate the total sum for the current position
            total_sum = val1 + val2 + carry
            
            # The new carry is the tens digit of total_sum
            # e.g., if total_sum = 15, carry = 15 // 10 = 1
            carry = total_sum // 10
            
            # The value to store in the new node is the ones digit of total_sum
            # e.g., if total_sum = 15, value = 15 % 10 = 5
            new_node_val = total_sum % 10
            
            # Create a new node with this value and attach it to our result list
            current.next = ListNode(new_node_val)
            
            # Move our pointers forward for the next iteration
            current = current.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
                
        # The result list starts at dummy.next (skipping our initial dummy node)
        return dummy.next
