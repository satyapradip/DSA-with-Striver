"""
================================================================================
                        QUEUE DATA STRUCTURE - COMPLETE GUIDE
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

📌 COMMON APPLICATIONS:
   - BFS (Breadth First Search) in graphs and trees
   - CPU/Task scheduling (First Come First Served)
   - Cache implementation (LRU cache uses queue-like structure)
   - Handling asynchronous data (producer-consumer problem)
   - Spooling (print jobs in OS)
   - Sliding window problems (with deques)
"""

# ==============================================================================
# 1️⃣  QUEUE IMPLEMENTATION USING PYTHON LIST (Simple but Inefficient)
# ==============================================================================

class Queue:
    """
    A simple queue implementation using Python's built-in list.
    
    ⚠️ IMPORTANT DRAWBACK:
       Using list.pop(0) to dequeue is O(n) because all elements
       must shift left by one position. We'll fix this with a
       Circular Queue later!
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
        
        Example:
            queue = [5, 10, 15]
            queue.front() → returns 5, queue stays [5, 10, 15]
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
# 2️⃣  CIRCULAR QUEUE (Efficient Implementation using Array) ⭐
# ==============================================================================
# The simple list-based queue wastes space when we dequeue. A circular queue
# reuses the freed space by wrapping around!
#
# Visual:
#   Indices:   [0] [1] [2] [3] [4]
#              ↑              ↑
#             front          rear
#
#   After dequeuing from [0]:
#   Indices:   [0] [1] [2] [3] [4]
#                    ↑              ↑
#                   front          rear
#
#   When rear reaches the end, it wraps to index 0 (circular!)
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
# 3️⃣  DEQUE - DOUBLE ENDED QUEUE (Python's collections.deque) ⭐⭐
# ==============================================================================
# A deque allows insertion and deletion at BOTH ends!
#
# Operations:            Time Complexity:
#   append(x)            O(1)  - add to right/rear
#   appendleft(x)        O(1)  - add to left/front
#   pop()                O(1)  - remove from right/rear
#   popleft()            O(1)  - remove from left/front
#
# Uses:
#   - Sliding window problems
#   - Palindrome checking
#   - BFS in graphs (can act as both stack and queue)
#   - Undo/Redo operations with limited history
# ==============================================================================

from collections import deque

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
# 4️⃣  IMPLEMENT QUEUE USING TWO STACKS  ⭐⭐ (Classic Interview Question)
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
# 5️⃣  IMPLEMENT STACK USING TWO QUEUES  ⭐⭐
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
# 6️⃣  BASIC PROBLEMS
# ==============================================================================

# ------------------------------------------------------------------------------
# PROBLEM 1: GENERATE BINARY NUMBERS FROM 1 TO N  ⭐
# ------------------------------------------------------------------------------
# Given a number N, generate binary numbers from 1 to N using a queue.
#
# Example:
#   N = 5 → ["1", "10", "11", "100", "101"]
#
# LOGIC:
#   1. Start with "1" in the queue
#   2. Dequeue front, output it
#   3. Append "0" and "1" to create children: front + "0", front + "1"
#   4. Enqueue both children
#   5. Repeat N times
#
# Visual:
#   Queue: ["1"]
#   Dequeue "1" → output "1", enqueue "10", "11"
#   Queue: ["10", "11"]
#   Dequeue "10" → output "10", enqueue "100", "101"
#   Queue: ["11", "100", "101"]
#   ...
# ------------------------------------------------------------------------------

def generate_binary_numbers(n):
    """
    Generate binary numbers from 1 to N using a queue.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    result = []
    q = deque(["1"])
    
    print(f"\n   Generating binary numbers 1 to {n}:")
    print(f"   {'-'*50}")
    
    for _ in range(n):
        # Dequeue the front
        current = q.popleft()
        result.append(current)
        print(f"   Dequeued '{current}' → Output: {result}")
        
        # Enqueue children (append 0 and 1)
        q.append(current + "0")
        q.append(current + "1")
        print(f"   Enqueued '{current}0', '{current}1' → Queue: {list(q)}")
    
    return result


# ------------------------------------------------------------------------------
# PROBLEM 2: FIRST NEGATIVE INTEGER IN EVERY WINDOW OF SIZE K  ⭐⭐
# ------------------------------------------------------------------------------
# Given an array and window size K, find the first negative number in each
# window. If no negative exists, output 0 (or indicate none).
#
# Example:
#   arr = [12, -1, -7, 8, -15, 30, 16, 28]
#   K = 3
#
#   Window 1: [12, -1, -7]  → first negative = -1
#   Window 2: [-1, -7, 8]   → first negative = -1
#   Window 3: [-7, 8, -15]  → first negative = -7
#   Window 4: [8, -15, 30]  → first negative = -15
#   Window 5: [-15, 30, 16] → first negative = -15
#   Window 6: [30, 16, 28]  → no negative → 0
#
# LOGIC: Use a queue to store INDICES of negative numbers. For each window,
# remove indices outside the window, then the front is the answer.
# ------------------------------------------------------------------------------

def first_negative_in_window(arr, k):
    """
    Find first negative integer in every window of size K.
    
    Time Complexity: O(n) - each element processed once
    Space Complexity: O(k) - queue stores at most k indices
    """
    n = len(arr)
    result = []
    q = deque()  # Queue to store indices of negative numbers
    
    print(f"\n   Array: {arr}")
    print(f"   Window size K = {k}")
    print(f"   {'='*60}")
    
    # Process first window separately
    for i in range(min(k, n)):
        if arr[i] < 0:
            q.append(i)
    
    # Process sliding windows
    for i in range(k, n + 1):
        # Front of queue is the first negative in current window (if exists)
        if q:
            result.append(arr[q[0]])
        else:
            result.append(0)  # No negative in window
        
        # Print current window
        window = arr[max(0, i-k):i] if i <= n else arr[max(0, i-k):n]
        print(f"   Window {list(window)} → First negative: {result[-1]}")
        
        # Remove elements that are out of the next window
        while q and q[0] <= i - k:
            q.popleft()
        
        # Add new element (if within bounds) to queue
        if i < n and arr[i] < 0:
            q.append(i)
    
    return result


# ------------------------------------------------------------------------------
# PROBLEM 3: REVERSE FIRST K ELEMENTS OF QUEUE  ⭐⭐
# ------------------------------------------------------------------------------
# Given a queue and number K, reverse the order of the first K elements.
#
# Example:
#   Queue: [1, 2, 3, 4, 5], K = 3
#   Result: [3, 2, 1, 4, 5]
#
# LOGIC:
#   1. Pop first K elements into a stack (this reverses them)
#   2. Pop from stack back into queue (now reversed at front)
#   3. Rotate remaining (n - k) elements to the back
# ------------------------------------------------------------------------------

def reverse_first_k(queue, k):
    """
    Reverse first K elements of a queue.
    
    Time Complexity: O(n)
    Space Complexity: O(k) for the stack
    """
    q = deque(queue)
    stack = []
    
    print(f"\n   Original Queue: {list(q)}, K = {k}")
    print(f"   {'-'*50}")
    
    # Step 1: Move first K elements to stack (reverses them)
    for _ in range(k):
        item = q.popleft()
        stack.append(item)
        print(f"   Dequeued {item} → Pushed to stack: {stack}")
    
    # Step 2: Move them back from stack to front of queue
    while stack:
        q.append(stack.pop())
    print(f"   After re-inserting: {list(q)}")
    
    # Step 3: Rotate remaining (n - k) elements to the back
    for _ in range(len(q) - k):
        q.append(q.popleft())
    
    print(f"   ✅ Final Queue: {list(q)}")
    return list(q)


# ==============================================================================
# 7️⃣  ADVANCED PATTERN: MONOTONIC QUEUE (Deque) ⭐⭐⭐
# ==============================================================================
# A monotonic queue maintains elements in either increasing or decreasing order.
# It's a DEQUE where we only keep "useful" elements.
#
# 💡 KEY INSIGHT: A monotonic queue is the QUEUE version of a monotonic stack!
#
# We maintain a DECREASING deque:
#   - When adding new element: remove ALL smaller elements from the back first
#   - This keeps the deque sorted (largest at front)
#   - The front always has the MAXIMUM in the current window

# ------------------------------------------------------------------------------
# PROBLEM 4: SLIDING WINDOW MAXIMUM  ⭐⭐⭐ (Very Famous!)
# ------------------------------------------------------------------------------
# Given an array and window size K, find the maximum in each sliding window.
#
# Example:
#   arr = [1, 3, -1, -3, 5, 3, 6, 7], K = 3
#   Output: [3, 3, 5, 5, 6, 7]
#
#   Window 1: [1, 3, -1] → max = 3
#   Window 2: [3, -1, -3] → max = 3
#   Window 3: [-1, -3, 5] → max = 5
#   Window 4: [-3, 5, 3] → max = 5
#   Window 5: [5, 3, 6] → max = 6
#   Window 6: [3, 6, 7] → max = 7
#
# NAIVE APPROACH: For each window, scan K elements → O(n*k)
# OPTIMAL: Use monotonic deque → O(n)
# ------------------------------------------------------------------------------

def sliding_window_maximum(nums, k):
    """
    Find maximum in every sliding window of size K.
    
    LOGIC (Monotonic Decreasing Deque):
    1. Store INDICES in a deque, maintaining decreasing order of values
    2. For each new element:
       a. Remove indices outside current window (from front)
       b. Remove indices whose values are <= current value (from back)
          — they can never be the max for any future window!
       c. Add current index to the back
       d. Front of deque = index of maximum for current window
    3. Only start outputting when we have a complete window (i >= k-1)
    
    Time Complexity: O(n) - each index added/removed at most once
    Space Complexity: O(k) - deque size at most k
    
    WHY IT WORKS:
    If a bigger element comes after a smaller one, the smaller one becomes
    "useless" — it will never be the maximum of any window that includes
    the bigger one. So we remove it!
    """
    from collections import deque
    
    n = len(nums)
    result = []
    dq = deque()  # Will store INDICES, maintaining decreasing values
    
    print(f"\n   Array: {nums}")
    print(f"   Window size K = {k}")
    print(f"   ⚡ Using MONOTONIC DEQUE - O(n) solution!")
    print(f"   {'='*60}")
    
    for i in range(n):
        # Step 1: Remove indices outside current window
        # (front indices that are too old)
        while dq and dq[0] <= i - k:
            removed = dq.popleft()
            print(f"   Index {removed} (value {nums[removed]}) left the window → removed")
        
        # Step 2: Remove smaller elements from back
        # (they're useless since current element is larger AND newer)
        while dq and nums[dq[-1]] <= nums[i]:
            removed = dq.pop()
            print(f"   {nums[removed]} ≤ {nums[i]} → {nums[removed]} can never be max → removed")
        
        # Step 3: Add current index
        dq.append(i)
        print(f"   Added index {i} (value {nums[i]}) → Deque values: "
              f"{[nums[idx] for idx in dq]}")
        
        # Step 4: Record max when we have a complete window
        if i >= k - 1:
            result.append(nums[dq[0]])
            print(f"   ✅ Window ending at {i}: {nums[i-k+1:i+1]} → Max = {nums[dq[0]]}")
        
        print()
    
    return result


# ------------------------------------------------------------------------------
# PROBLEM 5: ROTTEN ORANGES  ⭐⭐⭐ (BFS with Queue — Striver Classic!)
# ------------------------------------------------------------------------------
# In a grid, 0 = empty cell, 1 = fresh orange, 2 = rotten orange.
# Every minute, any fresh orange adjacent (4-directionally) to a rotten orange
# becomes rotten. Return the minimum minutes until all oranges rot,
# or -1 if impossible.
#
# Example:
#   grid = [[2,1,1],
#           [1,1,0],
#           [0,1,1]]
#   Output: 4
#
# LOGIC (Multi-source BFS):
#   1. Find ALL initially rotten oranges → push into queue (multi-source!)
#   2. BFS level by level, tracking time
#   3. Each neighbor that is fresh becomes rotten and joins queue
#   4. After BFS, check if any fresh orange remains → -1
# ------------------------------------------------------------------------------

def rotten_oranges(grid):
    """
    Find minimum time for all oranges to rot using BFS.
    
    Time Complexity: O(m*n) - visit each cell once
    Space Complexity: O(m*n) - queue size
    """
    from collections import deque
    
    rows, cols = len(grid), len(grid[0])
    q = deque()
    fresh_count = 0
    time = 0
    
    print(f"\n   Grid: {grid}")
    print(f"   {'='*60}")
    
    # Step 1: Find all rotten oranges (multi-source) and count fresh
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.append((r, c, 0))  # (row, col, time_rotten)
            elif grid[r][c] == 1:
                fresh_count += 1
    
    print(f"   Initial rotten sources: {list(q)}")
    print(f"   Fresh oranges: {fresh_count}")
    
    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Step 2: BFS
    while q:
        r, c, t = q.popleft()
        time = max(time, t)
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            # If neighbor is fresh, it becomes rotten
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh_count -= 1
                q.append((nr, nc, t + 1))
                print(f"   Minute {t+1}: Orange at ({nr}, {nc}) became rotten!")
    
    # Step 3: Check if any fresh oranges remain
    if fresh_count > 0:
        print(f"   ✗ {fresh_count} fresh orange(s) unreachable → Return -1")
        return -1
    
    print(f"   ✅ All oranges rotten in {time} minutes!")
    return time


# ------------------------------------------------------------------------------
# PROBLEM 6: IMPLEMENT STACK USING QUEUES (LeetCode 225)  ⭐⭐
# ------------------------------------------------------------------------------
# Already implemented above as StackUsingQueues class!

# ------------------------------------------------------------------------------
# PROBLEM 7: TASK SCHEDULER  ⭐⭐⭐ (Hot Interview Problem)
# ------------------------------------------------------------------------------
# Given tasks (A-Z) and a cooldown n, find the minimum time to finish all tasks.
# Same tasks must be separated by at least n units of time.
#
# Example:
#   tasks = ['A','A','A','B','B','B'], n = 2
#   Output: 8
#   Schedule: A → B → idle → A → B → idle → A → B
# ------------------------------------------------------------------------------

def task_scheduler(tasks, n):
    """
    Find minimum intervals needed to complete all tasks.
    
    LOGIC:
    1. Count frequency of each task
    2. The MOST frequent task dictates the schedule
    3. Formula: (max_freq - 1) * (n + 1) + count_of_max_freq_tasks
    4. Answer is max(formula, len(tasks))
    
    Time Complexity: O(tasks)
    Space Complexity: O(1) - at most 26 letters
    """
    from collections import Counter
    
    # Count frequency of each task
    task_counts = Counter(tasks)
    max_freq = max(task_counts.values())
    
    # Count how many tasks have the max frequency
    max_count = sum(1 for count in task_counts.values() if count == max_freq)
    
    # Formula
    intervals = (max_freq - 1) * (n + 1) + max_count
    
    # Answer must be at least the number of tasks
    result = max(intervals, len(tasks))
    
    print(f"\n   Tasks: {tasks}")
    print(f"   Cooldown: {n}")
    print(f"   Frequencies: {dict(task_counts)}")
    print(f"   Max frequency: {max_freq} (appears {max_count} time(s))")
    print(f"   Formula: ({max_freq}-1) × ({n}+1) + {max_count} = {intervals}")
    print(f"   Max with len(tasks)={len(tasks)} → Answer: {result}")
    
    return result


# ==============================================================================
# 8️⃣  MASTER-LEVEL PROBLEM
# ==============================================================================

# ------------------------------------------------------------------------------
# PROBLEM 8: SLIDING WINDOW MINIMUM (Mirror of Maximum) ⭐⭐⭐
# ------------------------------------------------------------------------------
# Same as sliding window max, but find the MINIMUM in each window.
# Uses a MONOTONIC INCREASING deque.
#
# Example:
#   arr = [1, 3, -1, -3, 5, 3, 6, 7], K = 3
#   Output: [-1, -3, -3, -3, 3, 3]
# ------------------------------------------------------------------------------

def sliding_window_minimum(nums, k):
    """
    Find minimum in every sliding window of size K.
    Uses monotonic INCREASING deque (smallest at front).
    
    Time Complexity: O(n)
    Space Complexity: O(k)
    """
    n = len(nums)
    result = []
    dq = deque()  # Monotonic increasing: front = smallest
    
    print(f"\n   Array: {nums}, Window size K = {k}")
    print(f"   ⚡ Monotonic INCREASING deque (smallest at front)")
    print(f"   {'='*60}")
    
    for i in range(n):
        # Remove indices outside window
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        # Remove LARGER elements (they can never be minimum)
        while dq and nums[dq[-1]] >= nums[i]:
            dq.pop()
        
        dq.append(i)
        
        if i >= k - 1:
            result.append(nums[dq[0]])
            print(f"   Window {nums[i-k+1:i+1]} → Min = {nums[dq[0]]}")
    
    return result


# ==============================================================================
# 9️⃣  INTERACTIVE DEMO - LEARN BY DOING
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


# ==============================================================================
# 🔟  PRACTICE PROBLEMS ROADMAP (Clear this checklist as you grow!)
# ==============================================================================
"""
📋 QUEUE PRACTICE ROADMAP (Beginner → Advanced)

🟢 LEVEL 1: BASIC (Master the fundamentals)
   1. ✅ Implement queue using list (done above)
   2. ✅ Implement circular queue (done above)
   3. ✅ Implement queue using two stacks (done above)
   4. ✅ Implement stack using two queues (done above)
   5. ✅ Generate binary numbers (Problem 1 above)
   6. ✅ Reverse first K elements of queue (Problem 3 above)
   7. Implement queue using linked list
   8. Design a deque using circular array

🟡 LEVEL 2: INTERMEDIATE (Build patterns)
   9.  ✅ First negative in every window (Problem 2 above)
   10. ✅ Sliding Window Maximum (Problem 4 above) — MONOTONIC DEQUE! 💡
   11. ✅ Sliding Window Minimum (Problem 8 above)
   12. ✅ Rotten Oranges (Problem 5 above) — BFS
   13. ✅ Task Scheduler (Problem 7 above)
   14. Implement Queues using stacks (polish the amortized analysis)
   15. Reversing a queue using recursion
   16. Distance of nearest cell having 1 (BFS)
   17. Zero-One Matrix (01 matrix BFS)
   18. Perfect Squares (BFS on numbers)

🔴 LEVEL 3: ADVANCED (Interview-ready)
   19. Sum of minimum & maximum in all subarrays of size K
   20. Longest valid parentheses (can be done with stack)
   21. Shortest path in binary matrix (BFS)
   22. Redundant connection (BFS/union-find)
   23. Design Snake Game (deque usage)
   24. Reveal cards in increasing order (deque simulation)

⚫ LEVEL 4: CHALLENGING (For the brave!)
   25. Shortest bridge (multi-source BFS)
   26. Minimum knight moves (BFS on chessboard)
   27. Word Ladder (famous BFS problem!)
   28. Open the Lock (BFS with states)
   29. Maximum of all subarrays with duplicates
   30. Moving Average from Data Stream (queue application)
"""


# ==============================================================================
# MAIN FUNCTION - RUN EVERYTHING TOGETHER
# ==============================================================================

if __name__ == "__main__":
    
    print("\n" + "█" * 60)
    print("██  QUEUE DATA STRUCTURE - COMPLETE LEARNING MODULE")
    print("█" * 60)
    
    # ──────────────────────────────────────────────────────────────────────────
    # SECTION 1: Queue Basics Demo
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 SECTION 1: QUEUE BASICS - Understanding FIFO")
    print("=" * 60)
    print()
    print("💡 Think of a queue like people lining up at a ticket counter:")
    print("   • People join the line at the BACK (rear)")
    print("   • The FIRST person in line is served FIRST")
    print("   • Then the second, third, and so on")
    print()
    print("   This is exactly how Queue works in programming!")
    
    demo_basic_queue_operations()
    
    # ──────────────────────────────────────────────────────────────────────────
    # SECTION 2: Circular Queue
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 SECTION 2: CIRCULAR QUEUE - No wasted space")
    print("=" * 60)
    print()
    print("   Problem with simple queue: dequeue leaves empty space at front")
    print("   Solution: Circular queue WRAPS AROUND to reuse that space!")
    
    demo_circular_queue()
    
    # ──────────────────────────────────────────────────────────────────────────
    # SECTION 3: Deque Demo
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 SECTION 3: DEQUE - The Swiss Army Knife")
    print("=" * 60)
    
    demo_deque()
    
    # ──────────────────────────────────────────────────────────────────────────
    # SECTION 4: Queue Using Stacks
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 SECTION 4: QUEUE USING TWO STACKS")
    print("=" * 60)
    print()
    print("   🧠 MENTAL MODEL:")
    print("   • Input stack: new elements arrive here")
    print("   • Output stack: elements wait to be served here")
    print("   • When output is empty, dump input into output (reverses order!)")
    
    demo_queue_using_stacks()
    
    # ──────────────────────────────────────────────────────────────────────────
    # SECTION 5: Generate Binary Numbers
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 SECTION 5: PROBLEM 1 - GENERATE BINARY NUMBERS")
    print("=" * 60)
    
    binaries = generate_binary_numbers(5)
    print(f"\n   ✅ Binary numbers: {binaries}\n")
    
    # ──────────────────────────────────────────────────────────────────────────
    # SECTION 6: First Negative in Window
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 SECTION 6: PROBLEM 2 - FIRST NEGATIVE IN WINDOW")
    print("=" * 60)
    
    fnw = first_negative_in_window([12, -1, -7, 8, -15, 30, 16, 28], 3)
    print(f"\n   ✅ Result: {fnw}\n")
    
    # ──────────────────────────────────────────────────────────────────────────
    # SECTION 7: Monotonic Queue - Sliding Window Maximum ⭐ STAR OF THE SHOW
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 SECTION 7: PROBLEM 4 - SLIDING WINDOW MAXIMUM")
    print("=" * 60)
    print()
    print("   ⭐ THIS IS THE MOST IMPORTANT QUEUE INTERVIEW PROBLEM! ⭐")
    print("   It introduces the MONOTONIC DEQUE pattern (Striver's favorite!)")
    
    swm = sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3)
    print(f"\n   ✅ Sliding Window Maximum: {swm}\n")
    
    # ──────────────────────────────────────────────────────────────────────────
    # SECTION 8: Rotten Oranges (BFS)
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 SECTION 8: PROBLEM 5 - ROTTEN ORANGES (BFS)")
    print("=" * 60)
    print()
    print("   🧠 MENTAL MODEL:")
    print("   • Multiple oranges rot at the SAME TIME (multi-source BFS)")
    print("   • Queue processes oranges in waves: minute 0, 1, 2...")
    print("   • This is EXACTLY how BFS works on grids!")
    
    orange_grid = [[2,1,1],[1,1,0],[0,1,1]]
    time_needed = rotten_oranges(orange_grid)
    print(f"\n   ✅ Minimum time: {time_needed} minutes\n")
    
    # ──────────────────────────────────────────────────────────────────────────
    # SECTION 9: Task Scheduler
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 SECTION 9: PROBLEM 7 - TASK SCHEDULER")
    print("=" * 60)
    
    time_taken = task_scheduler(['A','A','A','B','B','B'], 2)
    print(f"\n   ✅ Minimum intervals: {time_taken}\n")
    
    # ──────────────────────────────────────────────────────────────────────────
    # SECTION 10: Stack Using Queues
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 SECTION 10: STACK USING TWO QUEUES")
    print("=" * 60)
    
    sq = StackUsingQueues()
    print("\n   Stack using queues demo:")
    sq.push(1)
    sq.push(2)
    sq.push(3)
    sq.pop()
    sq.push(4)
    sq.pop()
    print(f"   Current top: {sq.top()}\n")
    
    # ──────────────────────────────────────────────────────────────────────────
    # SECTION 11: Sliding Window Minimum
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 SECTION 11: SLIDING WINDOW MINIMUM (Mirror Pattern)")
    print("=" * 60)
    
    swm_min = sliding_window_minimum([1, 3, -1, -3, 5, 3, 6, 7], 3)
    print(f"\n   ✅ Result: {swm_min}\n")
    
    # ──────────────────────────────────────────────────────────────────────────
    # SUMMARY
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "█" * 60)
    print("📚  QUEUE MASTERY CHECKLIST")
    print("█" * 60)
    print()
    print("🟢 MUST KNOW (Fundamentals):")
    print("  ☐ Queue = FIFO (First In First Out)")
    print("  ☐ enqueue at REAR, dequeue from FRONT")
    print("  ☐ Simple list queue has O(n) dequeue - use deque!")
    print("  ☐ Circular Queue reuses space with % (modulo)")
    print("  ☐ collections.deque = O(1) operations at both ends")
    print()
    print("🟡 GOOD TO KNOW (Intermediate):")
    print("  ☐ Queue using two stacks (amortized O(1))")
    print("  ☐ Stack using two queues")
    print("  ☐ Generate binary numbers using queue")
    print("  ☐ First negative in window of size K")
    print()
    print("🔴 ADVANCED LEVEL (Interview Gold!):")
    print("  ☐ Sliding Window Maximum — MONOTONIC DEQUE ⭐")
    print("  ☐ Rotten Oranges — Multi-source BFS")
    print("  ☐ Task Scheduler — Greedy formula")
    print("  ☐ Word Ladder — BFS on words")
    print("  ☐ Zero-One Matrix — Multi-source BFS")
    print()
    print("💪 TIPS FOR MASTERING QUEUES:")
    print("  1. Always draw the queue on paper - front and rear arrows!")
    print("  2. Remember: Queue = BFS. When you see 'shortest path' → think queue")
    print("  3. Sliding window problems → think DEQUE (monotonic queue)")
    print("  4. 'First come first serve' / 'scheduling' → think queue")
    print("  5. Multi-source BFS → push ALL starting points into queue first!")
    print("  6. BFS is level-by-level - the level = distance from source")
    print("  7. Practice the Sliding Window Maximum problem at least 5 times!")
    print()
    print("🚀 HOW TO TRANSITION FROM STACK TO QUEUE MINDSET:")
    print("  • Stack = LIFO = 'remember what was recent' (DFS)")
    print("  • Queue = FIFO = 'process in order' (BFS)")
    print("  • Stack = depth-first exploration")
    print("  • Queue = level-by-level / breadth-first exploration")
    print("  • Both are your 'memory' - choose based on order needed!")
    print()
    print("🔥 KEEP GOING! You already mastered arrays, recursion and stacks!")
    print("   Queue + BFS will unlock an ENTIRE new world of problems!")
    print("=" * 60)
