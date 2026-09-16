"""
================================================================================
                STACK IMPLEMENTATIONS - ARRAY & LINKED LIST ⭐
================================================================================
The simple list-based stack (01) is already O(1), but let's understand HOW a
stack REALLY works under the hood by building it two other ways:

1️⃣ FIXED-SIZE ARRAY STACK  → classic C-style implementation
   - Pre-allocates 'capacity' slots, uses a 'top' pointer
   - Shows OVERFLOW (stack full) and UNDERFLOW (stack empty) conditions

2️⃣ LINKED LIST STACK       → dynamic memory implementation
   - Each element is a Node pointing to the next one
   - push/pop happen at the HEAD → O(1) always
   - Memory grows/shrinks as needed - no wasted space

Visual - Array stack of size 5:
   Indices:   [0] [1] [2] [3] [4]
              (bottom)      ↑
                          top (points to last pushed element)

Visual - Linked list stack:
   push(10):  top → [10 | None]
   push(20):  top → [20 | ] → [10 | None]
   push(30):  top → [30 | ] → [20 | ] → [10 | None]
   pop():     returns 30, top moves to 20
"""

# ==============================================================================
# 1️⃣  STACK USING FIXED-SIZE ARRAY
# ==============================================================================

class ArrayStack:
    """
    A stack using a fixed-size array (classic C-style approach).

    KEY INSIGHTS:
    1. 'capacity' is fixed at creation time
    2. 'top' starts at -1 and points to the last pushed element
    3. Stack is FULL  when top == capacity - 1
    4. Stack is EMPTY when top == -1

    All operations: O(1) time 🚀
    """

    def __init__(self, capacity):
        """Initialize a stack with fixed capacity."""
        self.capacity = capacity
        self.arr = [None] * capacity
        self.top = -1  # -1 means empty

    def push(self, item):
        """
        Add an item to the top of the stack.
        Time Complexity: O(1)
        """
        if self.is_full():
            print(f"  ✗ OVERFLOW! Stack is FULL. Cannot push {item}.")
            return False
        self.top += 1
        self.arr[self.top] = item
        print(f"  ✓ Pushed {item} at index {self.top} → Array: {self._state()}")
        return True

    def pop(self):
        """
        Remove and return the top item.
        Time Complexity: O(1)
        """
        if self.is_empty():
            print("  ✗ UNDERFLOW! Stack is empty. Cannot pop.")
            return None
        item = self.arr[self.top]
        self.arr[self.top] = None  # optional cleanup
        self.top -= 1
        print(f"  ✓ Popped {item} → Array: {self._state()}")
        return item

    def peek(self):
        """View the top item without removing it. O(1)"""
        if self.is_empty():
            print("  ✗ Stack is empty! Nothing to peek.")
            return None
        print(f"  ✓ Top element: {self.arr[self.top]}")
        return self.arr[self.top]

    def is_empty(self):
        """Check if stack is empty. O(1)"""
        return self.top == -1

    def is_full(self):
        """Check if stack is full. O(1)"""
        return self.top == self.capacity - 1
    def _state(self):
        """Helper to visualize current array state."""
        return f"{self.arr} (top={self.top})"


# ==============================================================================
# 2️⃣  STACK USING LINKED LIST
# ==============================================================================

class Node:
    """A single node in the linked list stack."""

    def __init__(self, data):
        self.data = data
        self.next = None  # pointer to the node below


class LinkedListStack:
    """
    A stack using a singly linked list.

    KEY INSIGHTS:
    1. The HEAD of the list = TOP of the stack
    2. push  → insert a new node at the head  → O(1)
    3. pop   → remove the head node           → O(1)
    4. Memory grows/shrinks dynamically - NO fixed capacity!

    All operations: O(1) time 🚀
    """

    def __init__(self):
        """Initialize an empty linked-list stack."""
        self.top = None   # points to the top node
        self.count = 0    # number of elements

    def push(self, item):
        """
        Add an item to the top of the stack.
        Time Complexity: O(1)
        """
        new_node = Node(item)
        new_node.next = self.top  # link new node to current top
        self.top = new_node        # new node becomes the top
        self.count += 1
        print(f"  ✓ Pushed {item} → Stack (top → bottom): {self._state()}")

    def pop(self):
        """
        Remove and return the top item.
        Time Complexity: O(1)
        """
        if self.is_empty():
            print("  ✗ Stack is empty! Cannot pop.")
            return None
        item = self.top.data
        self.top = self.top.next   # move top down one node
        self.count -= 1
        print(f"  ✓ Popped {item} → Stack (top → bottom): {self._state()}")
        return item

    def peek(self):
        """View the top item without removing it. O(1)"""
        if self.is_empty():
            print("  ✗ Stack is empty! Nothing to peek.")
            return None
        print(f"  ✓ Top element: {self.top.data}")
        return self.top.data

    def is_empty(self):
        """Check if stack is empty. O(1)"""
        return self.top is None

    def size(self):
        """Return number of elements. O(1)"""
        return self.count
    def _state(self):
        """Helper to visualize the chain top → bottom."""
        values = []
        current = self.top
        while current:
            values.append(current.data)
            current = current.next
        return values
# ==============================================================================
# COMPARISON TABLE
# ==============================================================================
"""
HOW DO WE CHOOSE?
┌──────────────────────┬───────────────────────┬──────────────────────────┐
│                      │ Python List           │ Linked List              │
├──────────────────────┼───────────────────────┼──────────────────────────┤
│ Memory               │ Contiguous block      │ Scattered nodes + links  │
│ Capacity             │ Grows automatically   │ Grows automatically      │
│ Overflow risk        │ None (memory limit)   │ None (heap memory)       │
│ Cache friendliness   │ Great (contiguous) ⚡ │ Poor (pointer chasing)   │
│ Node overhead        │ None                  │ 1 pointer per element    │
│ Insert at top        │ O(1) amortized        │ O(1)                     │
│ Random access        │ O(1) via index ✅     │ Not supported ❌         │
│ Best for             │ Most interview code   │ Low-level / embedded     │
└──────────────────────┴───────────────────────┴──────────────────────────┘
"""


# ==============================================================================
# INTERACTIVE DEMOS
# ==============================================================================

def demo_array_stack():
    """Demonstrate the fixed-size array stack (overflow!)."""
    print("\n" + "=" * 60)
    print("🟢 ARRAY STACK DEMO - Fixed Capacity & OVERFLOW")
    print("=" * 60)

    print("""
   Visual: A stack of capacity 3
   Indices:   [ _ ][ _ ][ _ ]
              top = -1 (empty)

   Push 10 →   [ 10 ][ _ ][ _ ]   top = 0
   Push 20 →   [ 10 ][ 20 ][ _ ]  top = 1
   ... when top reaches 2 → FULL!
   """)

    s = ArrayStack(3)

    print("\n📌 Filling the stack (capacity = 3):")
    print("-" * 40)
    for i in [10, 20, 30]:
        s.push(i)

    print("\n📌 Stack is now full - try pushing more:")
    print("-" * 40)
    s.push(40)  # Should overflow

    print("\n📌 Pop two elements:")
    print("-" * 40)
    s.pop()
    s.pop()

    print("\n📌 Push again (space available!):")
    print("-" * 40)
    s.push(99)

    print("\n📌 Pop everything:")
    print("-" * 40)
    while not s.is_empty():
        s.pop()

    print("\n📌 Stack is empty - try popping more:")
    print("-" * 40)
    s.pop()  # Should underflow
def demo_linked_list_stack():
    """Demonstrate the linked list stack (dynamic growth!)."""
    print("\n" + "=" * 60)
    print("🟢 LINKED LIST STACK DEMO - Dynamic Memory, No Wasted Space")
    print("=" * 60)

    print("""
   Visual: Each push creates a New Node at the TOP:
   push(10):  top → [10]
   push(20):  top → [20] → [10]
   push(30):  top → [30] → [20] → [10]
   pop():     returns 30 → top → [20] → [10]
   """)

    s = LinkedListStack()

    print("\n📌 Push elements (chain grows downward):")
    print("-" * 40)
    for i in [10, 20, 30, 40]:
        s.push(i)

    print("\n📌 Peek at the top:")
    print("-" * 40)
    s.peek()
    print(f"   📏 Size: {s.size()}")

    print("\n📌 Pop all elements (LIFO order):")
    print("-" * 40)
    while not s.is_empty():
        s.pop()

    print("\n✅ The linked list stack NEVER overflows - memory is dynamic!")


# ==============================================================================
# MAIN FUNCTION
# ==============================================================================

if __name__ == "__main__":

    print("\n" + "█" * 60)
    print("██  STACK IMPLEMENTATIONS - ARRAY & LINKED LIST")
    print("█" * 60)
    print()
    print("   ✅ 01 used Python's list (built-in)")
    print("   🎯 02 rebuilds the stack manually to UNDERSTAND it deep")
    print()

    demo_array_stack()
    demo_linked_list_stack()

    print("\n🚀 NEXT: Run 03_basic_problems.py to solve the most common")
    print("   stack interview problems (Valid Parentheses, Min Stack, etc.)!")