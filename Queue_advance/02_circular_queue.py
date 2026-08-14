"""
================================================================================
                    CIRCULAR QUEUE - EFFICIENT IMPLEMENTATION ⭐
================================================================================
The simple list-based queue wastes space when we dequeue. A circular queue
reuses the freed space by wrapping around!

Visual:
  Indices:   [0] [1] [2] [3] [4]
             ↑              ↑
            front          rear

  After dequeuing from [0]:
  Indices:   [0] [1] [2] [3] [4]
                   ↑              ↑
                  front          rear

  When rear reaches the end, it wraps to index 0 (circular!)
"""

# ==============================================================================
# CIRCULAR QUEUE USING FIXED-SIZE ARRAY
# ==============================================================================

class CircularQueue:
    """
    A circular queue using a fixed-size array.
    
    KEY INSIGHTS:
    1. We use front and rear pointers (indices)
    2. (rear + 1) % capacity gives the next position (wraps around!)
    3. The queue is FULL when (rear + 1) % capacity == front
    4. The queue is EMPTY when front == -1 or front == rear
    
    All operations: O(1) time! 🚀
    """
    
    def __init__(self, capacity):
        """Initialize circular queue with given capacity."""
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1  # Points to front element
        self.rear = -1   # Points to rear element
    
    def is_empty(self):
        """Check if queue is empty. O(1)"""
        return self.front == -1
    
    def is_full(self):
        """Check if queue is full. O(1)"""
        # If rear is just before front (wrapping around), queue is full
        return (self.rear + 1) % self.capacity == self.front
    
    def enqueue(self, item):
        """
        Add an item to the rear of the circular queue.
        Time Complexity: O(1)
        """
        if self.is_full():
            print(f"  ✗ Queue is FULL! Cannot enqueue {item}.")
            return False
        
        # If adding the FIRST element, set front to 0
        if self.front == -1:
            self.front = 0
        
        # Move rear forward (wrapping around with %)
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        print(f"  ✓ Enqueued {item} at index {self.rear} → {self._show_state()}")
        return True
    
    def dequeue(self):
        """
        Remove and return the front item from the circular queue.
        Time Complexity: O(1)
        """
        if self.is_empty():
            print("  ✗ Queue is empty! Cannot dequeue.")
            return None
        
        item = self.queue[self.front]
        
        # If this was the ONLY element, reset the queue
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            # Move front forward (wrapping around)
            self.front = (self.front + 1) % self.capacity
        
        print(f"  ✓ Dequeued {item} → {self._show_state()}")
        return item
    
    def peek(self):
        """View the front element without removing it. O(1)"""
        if self.is_empty():
            print("  ✗ Queue is empty! Nothing to peek.")
            return None
        print(f"  ✓ Front element: {self.queue[self.front]}")
        return self.queue[self.front]
    
    def _show_state(self):
        """Helper to visualize current queue state."""
        if self.is_empty():
            return "Queue: []"
        # Build circular order starting from front
        result = []
        i = self.front
        while True:
            result.append(self.queue[i])
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        return f"Queue: {result} (front={self.front}, rear={self.rear})"


# ==============================================================================
# INTERACTIVE DEMO
# ==============================================================================

def demo_circular_queue():
    """
    See how the circular queue efficiently reuses space.
    """
    print("\n" + "=" * 60)
    print("🟢 CIRCULAR QUEUE DEMO - No wasted space!")
    print("=" * 60)
    
    print("""
   Visual: A queue of size 5
   
   Initial:          [ _ ][ _ ][ _ ][ _ ][ _ ]
                     f/r
   
   Enqueue 1-4:      [ 1 ][ 2 ][ 3 ][ 4 ][ _ ]
                     ↑                 ↑
                    front             rear
   
   Dequeue 1:        [ 1 ][ 2 ][ 3 ][ 4 ][ _ ]
                           ↑              ↑
                          front          rear
   
   Enqueue 5:        [ 1 ][ 2 ][ 3 ][ 4 ][ 5 ]
                           ↑              ↑
                          front          rear
   
   Enqueue 6 (WRAPS!): [ 6 ][ 2 ][ 3 ][ 4 ][ 5 ]
                              ↑              ↑
                             rear          front
   """)
    
    cq = CircularQueue(5)
    
    print("\n📌 Filling the circular queue:")
    print("-" * 40)
    for i in [1, 2, 3, 4, 5]:
        cq.enqueue(i)
    
    print("\n📌 Queue is now full:")
    print("-" * 40)
    print(f"   Is full? {cq.is_full()}")
    cq.enqueue(99)  # Should fail
    
    print("\n📌 Dequeue two elements (space freed at front):")
    print("-" * 40)
    cq.dequeue()
    cq.dequeue()
    
    print("\n📌 Enqueue more (wraps around!):")
    print("-" * 40)
    cq.enqueue(6)
    cq.enqueue(7)
    
    print("\n📌 Queue fully reused - NO wasted space!")
    print("-" * 40)
    print(f"   Is full? {cq.is_full()}")
    
    print("\n📌 Dequeue everything:")
    print("-" * 40)
    while not cq.is_empty():
        cq.dequeue()
    
    print("\n📌 Queue is empty now - try dequeue:")
    print("-" * 40)
    cq.dequeue()


# ==============================================================================
# MAIN FUNCTION
# ==============================================================================

if __name__ == "__main__":
    
    print("\n" + "█" * 60)
    print("██  CIRCULAR QUEUE - Efficient O(1) Operations")
    print("█" * 60)
    print()
    print("   Problem with simple queue: dequeue leaves empty space at front")
    print("   Solution: Circular queue WRAPS AROUND to reuse that space!")
    
    demo_circular_queue()
    
    print("\n🚀 NEXT: Run 03_deque.py to learn Python's built-in super queue!")