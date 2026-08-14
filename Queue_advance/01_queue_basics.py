"""
================================================================================
                    QUEUE BASICS - UNDERSTANDING FIFO
================================================================================

📌 WHAT IS A QUEUE?
   - A linear data structure that follows FIFO (First In First Out) principle
   - Think of it like a queue of people at a ticket counter:
     the first person to arrive is the first one served
   - The element added FIRST is the element removed FIRST

📌 REAL-LIFE EXAMPLES:
   - Queue of people at a ticket counter / ATM 🏦
   - Printer job queue (first document sent prints first) 🖨️
   - Customer service call waiting lines ☎️
   - Operating system process scheduling (FCFS)
   - Breadth First Search (BFS) in graphs & trees
   - Message queues in distributed systems (RabbitMQ, Kafka)

📌 BASIC OPERATIONS (Time Complexity: O(1)):
   - enqueue(x) → Add element x to the REAR (back) of the queue
   - dequeue()  → Remove and return the element from the FRONT
   - front()    → View the front element without removing it (peek)
   - rear()     → View the last element in the queue
   - isEmpty()  → Check if queue is empty
   - size()     → Get number of elements in queue

📌 QUEUE vs STACK (IMPORTANT!):
   ┌────────────┬────────────────────┬────────────────────┐
   │            │      STACK         │      QUEUE         │
   ├────────────┼────────────────────┼────────────────────┤
   │ Principle  │ LIFO               │ FIFO               │
   │ Insert     │ push() at top      │ enqueue() at rear │
   │ Remove     │ pop() from top     │ dequeue() at front│
   │ Real life  │ Stack of plates    │ Queue of people   │
   │ Uses       │ DFS, recursion     │ BFS, scheduling   │
   └────────────┴────────────────────┴────────────────────┘
"""

# ==============================================================================
# QUEUE IMPLEMENTATION USING PYTHON LIST (Simple but Inefficient)
# ==============================================================================

class Queue:
    """
    A simple queue implementation using Python's built-in list.
    
    ⚠️ IMPORTANT DRAWBACK:
       Using list.pop(0) to dequeue is O(n) because all elements
       must shift left by one position. We'll fix this with a
       Circular Queue in the next file!
    """
    
    def __init__(self):
        """Initialize an empty queue."""
        self.items = []
    
    def enqueue(self, item):
        """
        Add an item to the REAR (back) of the queue.
        Time Complexity: O(1)
        
        Example:
            queue.enqueue(5)  → queue: [5]
            queue.enqueue(10) → queue: [5, 10]
        """
        self.items.append(item)
        print(f"  ✓ Enqueued {item} → Queue (front → rear): {self.items}")
    
    def dequeue(self):
        """
        Remove and return the FRONT item from the queue.
        Time Complexity: O(n) - all elements shift left! ⚠️
        
        Returns:
            The front element, or None if queue is empty.
        
        Example:
            queue = [5, 10, 15]
            queue.dequeue() → returns 5, queue becomes [10, 15]
        """
        if self.is_empty():
            print("  ✗ Queue is empty! Cannot dequeue.")
            return None
        item = self.items.pop(0)  # O(n) - expensive!
        print(f"  ✓ Dequeued {item} → Queue (front → rear): {self.items}")
        return item
    
    def front(self):
        """
        Return the FRONT item WITHOUT removing it.
        Time Complexity: O(1)
        
        Returns:
            The front element, or None if queue is empty.
        """
        if self.is_empty():
            print("  ✗ Queue is empty! Nothing at front.")
            return None
        print(f"  ✓ Front element is: {self.items[0]}")
        return self.items[0]
    
    def rear(self):
        """
        Return the REAR (last) item WITHOUT removing it.
        Time Complexity: O(1)
        
        Returns:
            The rear element, or None if queue is empty.
        """
        if self.is_empty():
            print("  ✗ Queue is empty! Nothing at rear.")
            return None
        print(f"  ✓ Rear element is: {self.items[-1]}")
        return self.items[-1]
    
    def is_empty(self):
        """Check if the queue has no elements. Time Complexity: O(1)"""
        return len(self.items) == 0
    
    def size(self):
        """Return the number of elements in the queue. Time Complexity: O(1)"""
        return len(self.items)
    
    def display(self):
        """Display all elements in the queue from front to rear."""
        print(f"\n📦 Current Queue (front → rear): {self.items}")
        if self.is_empty():
            print("   (Queue is empty)")
        else:
            print(f"   📏 Size: {self.size()}")
            print(f"   🚪 Front: {self.items[0]}")
            print(f"   🔚 Rear: {self.items[-1]}")


# ==============================================================================
# INTERACTIVE DEMO - LEARN BY DOING
# ==============================================================================

def demo_basic_queue_operations():
    """
    Run this function to see how queue operations work step-by-step.
    """
    print("\n" + "=" * 60)
    print("🟢 QUEUE DEMO - Understanding FIFO (First In First Out)")
    print("=" * 60)
    
    q = Queue()
    
    print("\n📌 Step 1: Enqueue elements onto the queue")
    print("   (People joining the ticket line)")
    print("-" * 40)
    for i in [10, 20, 30, 40, 50]:
        q.enqueue(i)
    
    print("\n📌 Step 2: Front & Rear - See the ends")
    print("   (First person in line & last person in line)")
    print("-" * 40)
    q.front()
    q.rear()
    
    print("\n📌 Step 3: Dequeue - Remove elements from front")
    print("   (First person in line gets served FIRST)")
    print("-" * 40)
    print("\n   🔴 Notice: First pushed (10) comes out FIRST!")
    print("   This is what FIFO means!\n")
    
    for _ in range(3):
        q.dequeue()
    
    print("\n📌 Step 4: Check size and empty state")
    print("-" * 40)
    print(f"   📏 Queue size: {q.size()}")
    print(f"   ❓ Is empty? {q.is_empty()}")
    
    print("\n📌 Step 5: Dequeue remaining elements")
    print("-" * 40)
    while not q.is_empty():
        q.dequeue()
    
    print(f"\n📌 Step 6: Try to dequeue from empty queue")
    print("-" * 40)
    q.dequeue()
    
    print("\n" + "=" * 60)
    print("✅ END OF DEMO")
    print("=" * 60)
    print()
    print("📝 KEY TAKEAWAY:")
    print("   • Queue follows FIFO: First In, First Out")
    print("   • enqueue() adds to the REAR")
    print("   • dequeue() removes from the FRONT")
    print("   • Simple list implementation has O(n) dequeue ⚠️")
    print("   • Use CircularQueue or deque for O(1) operations")
    print("   • Think of it like a queue of people 🧍🧍🧍")


# ==============================================================================
# MAIN FUNCTION
# ==============================================================================

if __name__ == "__main__":
    
    print("\n" + "█" * 60)
    print("██  QUEUE BASICS - Understanding FIFO")
    print("█" * 60)
    print()
    print("💡 Think of a queue like people lining up at a ticket counter:")
    print("   • People join the line at the BACK (rear)")
    print("   • The FIRST person in line is served FIRST")
    print("   • Then the second, third, and so on")
    print()
    print("   This is exactly how Queue works in programming!")
    
    demo_basic_queue_operations()
    
    print("\n🚀 NEXT: Run 02_circular_queue.py to learn the EFFICIENT queue!")