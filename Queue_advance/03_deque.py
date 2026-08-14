"""
================================================================================
                    DEQUE - DOUBLE ENDED QUEUE ⭐⭐
================================================================================
A deque allows insertion and deletion at BOTH ends!

Operations:            Time Complexity:
  append(x)            O(1)  - add to right/rear
  appendleft(x)        O(1)  - add to left/front
  pop()                O(1)  - remove from right/rear
  popleft()            O(1)  - remove from left/front

Uses:
  - Sliding window problems
  - Palindrome checking
  - BFS in graphs (can act as both stack and queue)
  - Undo/Redo operations with limited history
"""

from collections import deque


# ==============================================================================
# DEQUE DEMO
# ==============================================================================

def demo_deque():
    """
    Demonstrate the power of collections.deque.
    """
    print("\n" + "=" * 60)
    print("🟢 DEQUE DEMO - Add/Remove from BOTH ends in O(1)")
    print("=" * 60)
    
    dq = deque([1, 2, 3])
    print(f"\n   Initial deque: {list(dq)}")
    
    dq.append(4)
    print(f"   After append(4)    → {list(dq)}  (added to right)")
    
    dq.appendleft(0)
    print(f"   After appendleft(0) → {list(dq)}  (added to left)")
    
    dq.pop()
    print(f"   After pop()        → {list(dq)}  (removed from right)")
    
    dq.popleft()
    print(f"   After popleft()    → {list(dq)}  (removed from left)")
    
    print("\n   💡 KEY: deque supports BOTH stack (LIFO) and queue (FIFO) ops!")


# ==============================================================================
# PROBLEM: CHECK PALINDROME USING DEQUE  ⭐
# ==============================================================================
# A palindrome reads the same forward and backward.
# Using a deque, we can compare front and rear elements!
#
# Example:
#   "racecar" → True
#   "hello"   → False
# ------------------------------------------------------------------------------

def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome using a deque.
    
    LOGIC:
    1. Add all characters to a deque
    2. While deque has more than 1 element:
       - Compare front and rear
       - If they differ → not a palindrome
       - Remove both
    3. If we get through everything → palindrome!
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    dq = deque(s.lower().replace(" ", ""))
    
    print(f"\n   Checking palindrome: '{s}'")
    print(f"   Deque: {list(dq)}")
    
    while len(dq) > 1:
        front = dq.popleft()
        rear = dq.pop()
        print(f"   Compare '{front}' vs '{rear}'", end="")
        
        if front != rear:
            print(" → ✗ NOT a palindrome!")
            return False
        print(" → ✓ Match!")
    
    print("   ✅ It IS a palindrome!")
    return True


# ==============================================================================
# PROBLEM: REVEAL CARDS IN INCREASING ORDER  ⭐⭐⭐ (LeetCode 950)
# ==============================================================================
# You have a deck of cards. You reveal the top card, then move the next card
# to the bottom. Repeat until no cards remain. Return the order that reveals
# cards in increasing order.
#
# Example:
#   deck = [17, 13, 11, 2, 3, 5, 7]
#   Output: [2, 13, 3, 11, 5, 17, 7]
#
# LOGIC (Reverse simulation):
# 1. Sort the deck in REVERSE (largest first)
# 2. For each card (from largest to smallest):
#    - Move the last card to the front (reverse of "move to bottom")
#    - Place the current card at the front
# ------------------------------------------------------------------------------

def reveal_cards_in_increasing_order(deck):
    """
    Return the order that reveals cards in increasing order.
    
    Time Complexity: O(n log n) - due to sorting
    Space Complexity: O(n)
    """
    # Sort in reverse order (largest first)
    deck.sort(reverse=True)
    dq = deque()
    
    print(f"\n   Sorted deck (largest first): {deck}")
    print(f"   {'='*50}")
    
    for card in deck:
        # Reverse the "move to bottom" operation
        if dq:
            moved = dq.pop()
            dq.appendleft(moved)
            print(f"   Move last ({moved}) to front → {list(dq)}")
        
        # Place current card at front
        dq.appendleft(card)
        print(f"   Place {card} at front → {list(dq)}")
    
    result = list(dq)
    print(f"\n   ✅ Reveal order: {result}")
    return result


# ==============================================================================
# MAIN FUNCTION
# ==============================================================================

if __name__ == "__main__":
    
    print("\n" + "█" * 60)
    print("██  DEQUE - The Swiss Army Knife of Queues")
    print("█" * 60)
    
    demo_deque()
    
    print("\n" + "=" * 60)
    print("📖 PROBLEM 1: PALINDROME CHECK USING DEQUE")
    print("=" * 60)
    
    is_palindrome("racecar")
    is_palindrome("hello")
    is_palindrome("A man a plan a canal Panama")
    
    print("\n" + "=" * 60)
    print("📖 PROBLEM 2: REVEAL CARDS IN INCREASING ORDER")
    print("=" * 60)
    
    reveal_cards_in_increasing_order([17, 13, 11, 2, 3, 5, 7])
    
    print("\n🚀 NEXT: Run 04_queue_stack_conversions.py to learn how")
    print("   to convert between stacks and queues!")