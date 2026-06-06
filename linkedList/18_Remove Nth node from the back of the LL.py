# Remove Nth node from the end of the linked list
# 
# Examples:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Explanation: The 2nd node from the end is 4.
#
# Input: head = [1], n = 1
# Output: []
#
# Input: head = [1,2], n = 1
# Output: [1]
#
# Approach (Two Pointers):
# 1. Use a dummy node pointing to the head to handle edge cases easily (e.g., when the head itself needs to be removed).
# 2. Use two pointers, `first` and `second`, both initialized to point to the dummy node.
# 3. Advance the `second` pointer by n + 1 steps to create a gap of n nodes between `first` and `second`.
# 4. Move both `first` and `second` at the same pace. When `second` reaches the end (`None`),
#    `first` will rest on the node immediately preceding the one to be deleted.
# 5. Delete the target node by changing the `next` pointer of `first` to skip it.
# 6. Return `dummy.next` as the updated head of the list.
#
# Time Complexity: O(L) where L is the number of nodes (one pass solution).
# Space Complexity: O(1) constant extra space.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # ── Dummy node: safety wrapper to handle edge cases ────────
        # Allows us to treat "delete first node" same as "delete any node"
        dummy = ListNode(0, head)

        # ── Create gap of n nodes between two pointers ─────────────
        first  = dummy
        second = dummy

        # Move second pointer n+1 steps ahead
        # This creates a gap of exactly n nodes
        for i in range(n + 1):
            second = second.next

        # ── Move both pointers until second reaches the end ────────
        while second:
            first  = first.next
            second = second.next

        # ── Delete the target node ─────────────────────────────────
        # first now points to the node BEFORE the target
        first.next = first.next.next

        return dummy.next