"""
================================================================================
                    QUEUE ↔ STACK CONVERSIONS ⭐⭐
================================================================================
Two classic interview questions:
1. Implement a QUEUE using TWO STACKS (LeetCode 232)
2. Implement a STACK using TWO QUEUES (LeetCode 225)

KEY INSIGHT: Using LIFO + LIFO we can achieve FIFO!
             Using FIFO + FIFO we can achieve LIFO!
"""

from collections import deque


# ==============================================================================
# 1️⃣  QUEUE USING TWO STACKS  (LeetCode 232) ⭐⭐
# ==============================================================================
# The trick: Use two stacks to simulate FIFO behavior.
#
# Visual:
#   Stack 1 (input):  [3, 2, 1]  ← push new elements here
#                     (1 is on top)
#
#   Stack 2 (output): []         ← pop from here
#
#   When output is empty, transfer ALL from input to output:
#   Stack 1: []  
#   Stack 2: [1, 2, 3]  (3 is on top → first element in = first out!)
#
# Time Complexity:
#   enqueue: O(1)
#   dequeue: Amortized O(1) - each element moved at most twice
# ==============================================================================

class QueueUsingStacks:
    """
    Implement a queue using two stacks.
    Uses LIFO + LIFO to achieve FIFO!
    """
    
    def __init__(self):
        self.input_stack = []   # For enqueue
        self.output_stack = []  # For dequeue
    
    def enqueue(self, item):
        """Add item to queue. O(1)"""
        self.input_stack.append(item)
        print(f"  ✓ Enqueued {item} → Input stack: {self.input_stack}")
    
    def dequeue(self):
        """
        Remove front item from queue.
        Time Complexity: Amortized O(1)
        """
        # If output stack is empty, transfer everything from input stack
        if not self.output_stack:
            print(f"  🔄 Transferring: input {self.input_stack} → output", end="")
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
            print(f" {self.output_stack}")
        
        if not self.output_stack:
            print("  ✗ Queue is empty!")
            return None
        
        item = self.output_stack.pop()
        print(f"  ✓ Dequeued {item} → Output stack: {self.output_stack}")
        return item
    
    def front(self):
        """View front element. O(1) amortized"""
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        return self.output_stack[-1] if self.output_stack else None
    
    def is_empty(self):
        return not self.input_stack and not self.output_stack


# ==============================================================================
# 2️⃣  STACK USING TWO QUEUES  (LeetCode 225) ⭐⭐
# ==============================================================================
# Similarly, we can use queues to implement a stack (LIFO using FIFOs!)
#
# Approach: On push, move all existing elements behind the new one.
#   Queue: [1, 2]  → push(3):
#   1. Add 3: [1, 2, 3]
#   2. Rotate: dequeue 1, enqueue 1 → [2, 3, 1]
#   3. Rotate: dequeue 2, enqueue 2 → [3, 1, 2]
#   Now front = 3 (most recent pushed) → top of stack!
# ==============================================================================

class StackUsingQueues:
    """
    Implement a stack using two queues.
    Uses FIFO + FIFO to achieve LIFO!
    """
    
    def __init__(self):
        self.q1 = deque()  # Main queue
        self.q2 = deque()  # Helper queue
    
    def push(self, item):
        """
        Push item onto stack.
        Time Complexity: O(n)
        """
        # Add new item to q2
        self.q2.append(item)
        
        # Move ALL elements from q1 to q2 (behind the new item)
        while self.q1:
            self.q2.append(self.q1.popleft())
        
        # Swap q1 and q2 (q1 now has new item at FRONT)
        self.q1, self.q2 = self.q2, self.q1
        print(f"  ✓ Pushed {item} → Stack (top → bottom): {list(self.q1)}")
    
    def pop(self):
        """Pop top item from stack. O(1)"""
        if not self.q1:
            print("  ✗ Stack is empty!")
            return None
        item = self.q1.popleft()
        print(f"  ✓ Popped {item} → Stack (top → bottom): {list(self.q1)}")
        return item
    
    def top(self):
        """View top of stack without removing. O(1)"""
        return self.q1[0] if self.q1 else None
    
    def is_empty(self):
        return not self.q1


# ==============================================================================
# 3️⃣  AMORTIZED ANALYSIS EXPLAINED 🧠
# ==============================================================================
"""
WHAT DOES "AMORTIZED O(1)" MEAN?
=================================

Imagine a bank account 🏦:
  • Every enqueue puts $1 in (cost = 1 unit)
  • Every dequeue spends $1 (cost = 1 unit)
  
But sometimes dequeue costs MORE:
  • When output_stack is empty, transferring n elements costs n units
  • However! Those n elements were ALREADY "paid for" during enqueue

KEY IDEA: Each element is moved AT MOST TWICE:
  1. Once from input → output (during transfer)
  2. Once from output → popped (during dequeue)

So for n operations:
  • n enqueues: O(n) total
  • n dequeues: O(n) total transfer + O(n) pops = O(n) total
  
Average cost per operation = O(n) / n = O(1) → "Amortized O(1)!"

The "amortized" (average) cost is O(1), even though individual
operations might occasionally be O(n).
"""


# ==============================================================================
# DEMO FUNCTIONS
# ==============================================================================

def demo_queue_using_stacks():
    """
    Demonstrate the stack-based queue implementation.
    """
    print("\n" + "=" * 60)
    print("🟢 QUEUE USING STACKS DEMO")
    print("=" * 60)
    
    q = QueueUsingStacks()
    
    print("\n📌 Enqueue 1, 2, 3:")
    print("-" * 40)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    
    print("\n📌 Dequeue (1 should come out first - FIFO!):")
    print("-" * 40)
    q.dequeue()
    
    print("\n📌 Enqueue 4, then dequeue:")
    print("-" * 40)
    q.enqueue(4)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    
    print("\n✅ The two stacks together behave like a queue!")


def demo_stack_using_queues():
    """
    Demonstrate the queue-based stack implementation.
    """
    print("\n" + "=" * 60)
    print("🟢 STACK USING QUEUES DEMO")
    print("=" * 60)
    
    s = StackUsingQueues()
    
    print("\n📌 Push 1, 2, 3:")
    print("-" * 40)
    s.push(1)
    s.push(2)
    s.push(3)
    
    print("\n📌 Pop (3 should come out first - LIFO!):")
    print("-" * 40)
    s.pop()
    
    print("\n📌 Push 4, then pop:")
    print("-" * 40)
    s.push(4)
    s.pop()
    s.pop()
    s.pop()
    
    print("\n✅ The two queues together behave like a stack!")


# ==============================================================================
# MAIN FUNCTION
# ==============================================================================

if __name__ == "__main__":
    
    print("\n" + "█" * 60)
    print("██  QUEUE ↔ STACK CONVERSIONS")
    print("█" * 60)
    
    print("\n" + "=" * 60)
    print("📖 SECTION 1: QUEUE USING TWO STACKS")
    print("=" * 60)
    print()
    print("   🧠 MENTAL MODEL:")
    print("   • Input stack: new elements arrive here")
    print("   • Output stack: elements wait to be served here")
    print("   • When output is empty, dump input into output (reverses order!)")
    
    demo_queue_using_stacks()
    
    print("\n" + "=" * 60)
    print("📖 SECTION 2: STACK USING TWO QUEUES")
    print("=" * 60)
    print()
    print("   🧠 MENTAL MODEL:")
    print("   • On push, rotate all old elements behind the new one")
    print("   • The NEW element becomes the FRONT of the queue")
    print("   • Popping from front = popping from top of stack!")
    
    demo_stack_using_queues()
    
    print("\n" + "=" * 60)
    print("📖 SECTION 3: AMORTIZED ANALYSIS")
    print("=" * 60)
    print()
    print("   Each element moved at most TWICE:")
    print("   1. input → output (during transfer)")
    print("   2. output → popped (during dequeue)")
    print()
    print("   Average = O(1) per operation → 'Amortized O(1)'!")
    
    print("\n🚀 NEXT: Run 05_basic_problems.py to solve classic queue problems!")