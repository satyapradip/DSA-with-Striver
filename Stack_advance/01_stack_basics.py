"""
================================================================================
                    STACK BASICS - UNDERSTANDING LIFO
================================================================================

📌 WHAT IS A STACK?
   - A linear data structure that follows LIFO (Last In First Out) principle
   - Think of it like a stack of plates at a cafeteria:
     you can only add or remove plates from the TOP
   - The element added LAST is the element removed FIRST

📌 REAL-LIFE EXAMPLES:
   - Stack of plates in a cafeteria 🍽️
   - Undo/Redo in text editors (Ctrl+Z / Ctrl+Y) ↩️
   - Browser back/forward buttons 🌐
   - Call stack in programming (function calls) 📞
   - Expression evaluation (compilers use stack)

📌 BASIC OPERATIONS (Time Complexity: O(1)):
   - push(x)   → Add element x to the TOP
   - pop()     → Remove and return the TOP element
   - peek()    → View the top element without removing it
   - isEmpty() → Check if stack is empty
   - size()    → Get number of elements in stack

📌 STACK vs QUEUE (IMPORTANT!):
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
# STACK IMPLEMENTATION USING PYTHON LIST
# ==============================================================================

class Stack:
    """
    A simple stack implementation using Python's built-in list.

    Python lists have append() and pop() which work exactly like
    stack push/pop - they operate at the END of the list (O(1)).
    """

    def __init__(self):
        """Initialize an empty stack."""
        self.items = []

    def push(self, item):
        """
        Add an item to the top of the stack.
        Time Complexity: O(1) amortized

        Example:
            stack.push(5)  → stack: [5]
            stack.push(10) → stack: [5, 10]
        """
        self.items.append(item)
        print(f"  ✓ Pushed {item} → Stack (bottom → top): {self.items}")

    def pop(self):
        """
        Remove and return the top item from the stack.
        Time Complexity: O(1) amortized

        Returns:
            The top element, or None if stack is empty.

        Example:
            stack = [5, 10, 15]
            stack.pop() → returns 15, stack becomes [5, 10]
        """
        if self.is_empty():
            print("  ✗ Stack is empty! Cannot pop.")
            return None
        item = self.items.pop()
        print(f"  ✓ Popped {item} → Stack (bottom → top): {self.items}")
        return item
    def peek(self):
        """
        Return the top item WITHOUT removing it.
        Time Complexity: O(1)

        Returns:
            The top element, or None if stack is empty.

        Example:
            stack = [5, 10, 15]
            stack.peek() → returns 15, stack stays [5, 10, 15]
        """
        if self.is_empty():
            print("  ✗ Stack is empty! Nothing to peek.")
            return None
        print(f"  ✓ Top element is: {self.items[-1]}")
        return self.items[-1]

    def is_empty(self):
        """Check if the stack has no elements. Time Complexity: O(1)"""
        return len(self.items) == 0

    def size(self):
        """Return the number of elements in the stack. Time Complexity: O(1)"""
        return len(self.items)

    def display(self):
        """Display all elements in the stack from bottom to top."""
        print(f"\n📦 Current Stack (bottom → top): {self.items}")
        if self.is_empty():
            print("   (Stack is empty)")
        else:
            print(f"   📏 Size: {self.size()}")
            print(f"   🔝 Top: {self.items[-1]}")
# ==============================================================================
# INTERACTIVE DEMO - LEARN BY DOING
# ==============================================================================

def demo_basic_stack_operations():
    """Run this to see stack operations work step-by-step."""
    print("\n" + "=" * 60)
    print("🟢 STACK DEMO - Understanding LIFO (Last In First Out)")
    print("=" * 60)

    stack = Stack()

    print("\n📌 Step 1: Push elements onto the stack")
    print("   (Adding plates to the top of the pile)")
    print("-" * 40)
    for i in [10, 20, 30, 40, 50]:
        stack.push(i)

    print("\n📌 Step 2: Peek - See what's on top")
    print("   (Looking at the top plate without removing it)")
    print("-" * 40)
    stack.peek()

    print("\n📌 Step 3: Pop - Remove elements from top")
    print("   (Taking plates from the top of the pile)")
    print("-" * 40)
    print("\n   🔴 Notice: Last pushed (50) comes out FIRST!")
    print("   This is what LIFO means!\n")
    for _ in range(3):
        stack.pop()

    print("\n📌 Step 4: Check size and empty state")
    print("-" * 40)
    print(f"   📏 Stack size: {stack.size()}")
    print(f"   ❓ Is empty? {stack.is_empty()}")

    print("\n📌 Step 5: Pop remaining elements")
    print("-" * 40)
    while not stack.is_empty():
        stack.pop()

    print("\n📌 Step 6: Try to pop from empty stack")
    print("-" * 40)
    stack.pop()

    print("\n" + "=" * 60)
    print("✅ END OF DEMO")
    print("=" * 60)
    print()
    print("📝 KEY TAKEAWAY:")
    print("   • Stack follows LIFO: Last In, First Out")
    print("   • push() adds to the TOP")
    print("   • pop() removes from the TOP")
    print("   • All operations are O(1) - very fast!")
    print("   • Think of it like a stack of plates 🍽️")
# ==============================================================================
# MAIN FUNCTION
# ==============================================================================

if __name__ == "__main__":

    print("\n" + "█" * 60)
    print("██  STACK BASICS - Understanding LIFO")
    print("█" * 60)
    print()
    print("💡 Think of a stack like a stack of plates in a cafeteria:")
    print("   • You can only add a plate to the TOP")
    print("   • You can only remove a plate from the TOP")
    print("   • The last plate placed is the first one removed")
    print()
    print("   This is exactly how Stack works in programming!")

    demo_basic_stack_operations()

    print("\n🚀 NEXT: Run 02_stack_linked_list.py to implement the stack")
    print("   with alternative structures (fixed array + linked list)!")