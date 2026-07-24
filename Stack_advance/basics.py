"""
================================================================================
                        STACK DATA STRUCTURE - COMPLETE GUIDE
================================================================================

📌 WHAT IS A STACK?
   - A linear data structure that follows LIFO (Last In First Out) principle
   - Think of it like a stack of plates: you can only add/remove from the top
   - The last element added is the first one to be removed

📌 REAL-LIFE EXAMPLES:
   - Stack of plates in a cafeteria
   - Undo/Redo in text editors (Ctrl+Z / Ctrl+Y)
   - Browser back/forward buttons
   - Call stack in programming (function calls)
   - Expression evaluation (compilers use stack)

📌 BASIC OPERATIONS (Time Complexity: O(1) for all):
   - push(x)  → Add element x to the top
   - pop()    → Remove and return the top element
   - peek()   → View the top element without removing it
   - isEmpty()→ Check if stack is empty
   - size()   → Get number of elements in stack

📌 COMMON APPLICATIONS:
   - Function calls/Recursion
   - Expression evaluation (infix/postfix/prefix)
   - Parenthesis matching
   - Undo operations
   - Backtracking algorithms
   - DFS (Depth First Search) in graphs
"""

# ==============================================================================
# 1️⃣  STACK IMPLEMENTATION USING PYTHON LIST
# ==============================================================================

class Stack:
    """
    A simple stack implementation using Python's built-in list.
    
    Python lists already have append() and pop() which work exactly
    like stack push/pop - they operate at the end of the list (O(1)).
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
        print(f"  ✓ Pushed {item} → Stack: {self.items}")
    
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
        print(f"  ✓ Popped {item} → Stack: {self.items}")
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
        """
        Check if the stack has no elements.
        Time Complexity: O(1)
        
        Returns:
            True if stack is empty, False otherwise.
        """
        return len(self.items) == 0
    
    def size(self):
        """
        Return the number of elements in the stack.
        Time Complexity: O(1)
        
        Returns:
            Integer count of elements.
        """
        return len(self.items)
    
    def display(self):
        """
        Display all elements in the stack from bottom to top.
        """
        print(f"\n📦 Current Stack (bottom → top): {self.items}")
        if self.is_empty():
            print("   (Stack is empty)")
        else:
            print(f"   📏 Size: {self.size()}")
            print(f"   🔝 Top: {self.items[-1]}")


# ==============================================================================
# 2️⃣  INTERACTIVE DEMO - LEARN BY DOING
# ==============================================================================

def demo_basic_stack_operations():
    """
    Run this function to see how stack operations work step-by-step.
    """
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
    
    print(f"\n📌 Step 6: Try to pop from empty stack")
    print("-" * 40)
    stack.pop()
    
    print("\n" + "=" * 60)
    print("✅ END OF DEMO")
    print("=" * 60)
    print()
    print("📝 KEY TAKEAWAY:")
    print("   • Stack follows LIFO: Last In, First Out")
    print("   • push() adds to the top")
    print("   • pop() removes from the top")
    print("   • All operations are O(1) - very fast!")
    print("   • Think of it like a stack of plates 🍽️")


# ==============================================================================
# 3️⃣  COMMON STACK PROBLEMS (FROM EASY TO HARD)
# ==============================================================================

# ------------------------------------------------------------------------------
# PROBLEM 1: VALID PARENTHESES  (Very Common Interview Question) ⭐
# ------------------------------------------------------------------------------
# Given a string containing just '(', ')', '{', '}', '[' and ']', determine
# if the input string has valid parentheses.
#
# Example:
#   "()"     → True
#   "()[]{}" → True
#   "(]"     → False
#   "([)]"   → False
#   "{[]}"   → True
# ------------------------------------------------------------------------------

def is_valid_parentheses(s: str) -> bool:
    """
    Check if parentheses are valid using a stack.
    
    LOGIC:
    1. Create a mapping: closing → opening brackets
    2. Iterate through each character:
       - If it's an opening bracket → push to stack
       - If it's a closing bracket:
         * Check if stack is empty → invalid
         * Check if top matches corresponding opening → invalid
    3. At the end, stack should be empty
    
    Time Complexity: O(n) - we process each character once
    Space Complexity: O(n) - in worst case, all characters are opening brackets
    """
    # Mapping of closing to opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []
    
    print(f"\n   Input String: '{s}'")
    print(f"   Processing...")
    
    for i, char in enumerate(s):
        print(f"   Step {i+1}: Char = '{char}'", end="")
        
        if char in bracket_map:
            # It's a closing bracket
            # stack.pop() returns the top element, or '#' if empty
            top = stack.pop() if stack else '#'
            print(f" (closing) → Top of stack: '{top}'", end="")
            
            if top != bracket_map[char]:
                print(f" ✗ Mismatch! Expected '{bracket_map[char]}', got '{top}'")
                return False
            else:
                print(f" ✓ Match!")
        else:
            # It's an opening bracket - push to stack
            stack.append(char)
            print(f" (opening) → Pushed to stack. Stack: {stack}")
    
    # Stack should be empty at the end
    result = len(stack) == 0
    if not result:
        print(f"   ✗ Unmatched opening brackets remaining: {stack}")
    else:
        print(f"   ✓ All brackets matched!")
    
    return result


# ------------------------------------------------------------------------------
# PROBLEM 2: MIN STACK  (Classic Problem) ⭐⭐
# ------------------------------------------------------------------------------
# Design a stack that supports push, pop, top, and retrieving the minimum
# element in constant time O(1).
# ------------------------------------------------------------------------------

class MinStack:
    """
    Stack that can return the minimum element in O(1) time.
    
    TRICK: Keep TWO stacks:
    1. Main stack → stores all elements
    2. Min stack  → stores current minimum at each level
    
    When pushing:
      - Push x to main stack
      - Push min(x, current_min) to min stack
    
    When popping:
      - Pop from both stacks
    
    The top of min stack always gives the current minimum.
    """
    
    def __init__(self):
        self.stack = []    # Main stack
        self.min_stack = []  # Tracks minimum at each step
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        # The new minimum is min(val, current minimum)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))
        print(f"   Pushed {val} → Stack: {self.stack}, Min: {self.get_min()}")
    
    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            self.min_stack.pop()
            print(f"   Popped {val} → Stack: {self.stack}", end="")
            if self.stack:
                print(f", Min: {self.get_min()}")
            else:
                print(" (empty)")
    
    def top(self) -> int:
        return self.stack[-1] if self.stack else None
    
    def get_min(self) -> int:
        """Return the minimum element in O(1) time."""
        return self.min_stack[-1] if self.min_stack else None


# ------------------------------------------------------------------------------
# PROBLEM 3: NEXT GREATER ELEMENT  ⭐⭐
# ------------------------------------------------------------------------------
# Given an array, find the next greater element for each element.
# The next greater element is the first greater element to the right.
# If no greater element exists, return -1.
#
# Example:
#   arr = [4, 5, 2, 25]
#   Output: [5, 25, 25, -1]
#
#   Explanation:
#   - Next greater for 4  (index 0) = 5
#   - Next greater for 5  (index 1) = 25
#   - Next greater for 2  (index 2) = 25
#   - Next greater for 25 (index 3) = -1 (nothing greater to the right)
# ------------------------------------------------------------------------------

def next_greater_element(arr):
    """
    Find next greater element for each element using a stack.
    
    LOGIC (Monotonic Decreasing Stack):
    1. Iterate from left to right
    2. While stack is NOT empty AND current element > stack's top element:
       - Pop the index from stack
       - Current element is the next greater for that popped index
    3. Push current index to stack
    4. Elements still in stack at the end have no greater element → -1
    
    Time Complexity: O(n) - each element pushed/popped at most once
    Space Complexity: O(n) - for the stack and result array
    """
    n = len(arr)
    result = [-1] * n
    stack = []  # Will store indices
    
    print(f"\n   Array: {arr}")
    print(f"   {'-'*40}")
    
    for i in range(n):
        print(f"   Processing arr[{i}] = {arr[i]}")
        
        # While current element is greater than element at stack top
        while stack and arr[i] > arr[stack[-1]]:
            popped_idx = stack.pop()
            result[popped_idx] = arr[i]
            print(f"   → {arr[popped_idx]}'s next greater = {arr[i]}")
        
        stack.append(i)
        print(f"   Stack (indices): {stack} → values: {[arr[idx] for idx in stack]}")
    
    # Print elements with no next greater
    for idx in stack:
        print(f"   → {arr[idx]} has no next greater → -1")
    
    return result


# ------------------------------------------------------------------------------
# PROBLEM 4: STOCK SPAN PROBLEM  ⭐⭐
# ------------------------------------------------------------------------------
# The stock span is defined as the number of consecutive days before (including
# today) where the stock price was less than or equal to today's price.
#
# Example:
#   prices = [100, 80, 60, 70, 60, 75, 85]
#   spans  = [  1,  1,  1,  2,  1,  4,  6]
#
#   Explanation:
#   - Day 0 (100): No previous days → span = 1
#   - Day 1 (80):  Previous 100 > 80 → span = 1
#   - Day 2 (60):  Previous 80 > 60  → span = 1
#   - Day 3 (70):  60 <= 70, but 80 > 70 → span = 2 (days 2 & 3)
#   - Day 4 (60):  70 > 60 → span = 1
#   - Day 5 (75):  60 <= 75, 70 <= 75 → span = 4 (days 2, 3, 4, 5)
#   - Day 6 (85):  75 <= 85, 60 <= 85, 70 <= 85, 60 <= 85, 80 <= 85, 100 > 85
#                  → span = 6 (days 1 through 6)
# ------------------------------------------------------------------------------

def stock_span(prices):
    """
    Calculate stock span for each day using a stack.
    
    LOGIC:
    1. Stack stores indices of days with decreasing prices (monotonic)
    2. For each day i:
       - Pop while stack top has price <= current price
       - If stack is empty → all previous prices were less → span = i + 1
       - Else → span = i - stack[-1] (distance to nearest greater price)
       - Push current index to stack
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    n = len(prices)
    span = [0] * n
    stack = []  # Stores indices of decreasing prices
    
    print(f"\n   Prices: {prices}")
    print(f"   {'-'*50}")
    
    for i in range(n):
        # Pop until we find a day with price > current price
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()
        
        # Calculate span
        if not stack:
            span[i] = i + 1  # All previous days had lower prices
        else:
            span[i] = i - stack[-1]  # Distance to nearest greater price
        
        stack.append(i)
        print(f"   Day {i} (Price: {prices[i]}) → Span: {span[i]}")
        print(f"   Stack of decreasing prices (indices): {stack}")
        print()
    
    return span


# ------------------------------------------------------------------------------
# PROBLEM 5: INFIX TO POSTFIX CONVERSION  ⭐⭐⭐
# ------------------------------------------------------------------------------
# Convert an infix expression (e.g., "A+B*C") to postfix (e.g., "ABC*+").
#
# Operator Precedence (higher = evaluated first):
#   ^ (exponent) : 3
#   *, /         : 2
#   +, -         : 1
# ------------------------------------------------------------------------------

def infix_to_postfix(expression: str) -> str:
    """
    Convert infix expression to postfix using a stack.
    
    ALGORITHM (Shunting Yard Algorithm by Edsger Dijkstra):
    1. Scan the expression left to right
    2. If operand → add to output
    3. If '(' → push to stack
    4. If ')' → pop from stack to output until '(' is found
    5. If operator → pop higher/equal precedence operators, then push current
    6. Pop remaining operators from stack to output
    """
    # Precedence of operators
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    
    stack = []
    output = []
    
    print(f"\n   Infix Expression: {expression}")
    print(f"   {'-'*50}")
    
    for i, char in enumerate(expression):
        if char.isalnum():  # Operand (A-Z, 0-9)
            output.append(char)
            print(f"   '{char}' is operand → Output: {''.join(output)}")
        
        elif char == '(':
            stack.append(char)
            print(f"   '(' → Push to stack. Stack: {stack}")
        
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Remove the '('
            print(f"   ')' → Pop till '(' → Output: {''.join(output)}, Stack: {stack}")
        
        else:  # Operator
            while (stack and stack[-1] != '(' and 
                   precedence.get(stack[-1], 0) >= precedence.get(char, 0)):
                output.append(stack.pop())
            stack.append(char)
            print(f"   '{char}' is operator → Stack: {stack}, Output: {''.join(output)}")
    
    # Pop remaining operators from stack
    while stack:
        output.append(stack.pop())
    
    print(f"\n   Final Postfix: {''.join(output)}")
    return ''.join(output)


# ------------------------------------------------------------------------------
# PROBLEM 6: ADVANCED - EVALUATE POSTFIX EXPRESSION  ⭐⭐⭐
# ------------------------------------------------------------------------------
# Evaluate a postfix expression like "23*54*+"
# (Same as (2*3) + (5*4) = 6 + 20 = 26)
# ------------------------------------------------------------------------------

def evaluate_postfix(expression: str) -> int:
    """
    Evaluate a postfix expression using a stack.
    
    ALGORITHM:
    1. Scan left to right
    2. If operand → push to stack
    3. If operator → pop two operands, apply operator, push result
    4. At the end, stack contains the result
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    stack = []
    
    print(f"\n   Postfix Expression: {expression}")
    print(f"   {'-'*40}")
    
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
            print(f"   Operand '{char}' → Push. Stack: {stack}")
        else:
            b = stack.pop()  # Second operand (top)
            a = stack.pop()  # First operand
            result = 0
            
            if char == '+':
                result = a + b
            elif char == '-':
                result = a - b
            elif char == '*':
                result = a * b
            elif char == '/':
                result = a // b  # Integer division
            
            stack.append(result)
            print(f"   Operator '{char}': {a} {char} {b} = {result} → Stack: {stack}")
    
    print(f"\n   ✅ Final Result: {stack[0]}")
    return stack[0]


# ------------------------------------------------------------------------------
# PROBLEM 7: CHALLENGING - LARGEST RECTANGLE IN HISTOGRAM  ⭐⭐⭐⭐
# ------------------------------------------------------------------------------
# Given an array of heights representing a histogram, find the largest rectangle
# that can be formed.
#
# Example:
#   heights = [2, 1, 5, 6, 2, 3]
#   Output: 10 (The largest rectangle has area 5*2 = 10)
# ------------------------------------------------------------------------------

def largest_rectangle_in_histogram(heights):
    """
    Find the largest rectangle area in a histogram using a stack.
    
    LOGIC (Monotonic Increasing Stack):
    1. For each bar, find the first smaller bar to its left and right
    2. The width a bar can span is (right_smaller_index - left_smaller_index - 1)
    3. Area = height * width
    
    KEY INSIGHT: When we see a smaller bar, the previous bar's rectangle
    cannot extend further to the right.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    max_area = 0
    stack = []  # Stack of indices (increasing heights)
    n = len(heights)
    
    print(f"\n   Heights: {heights}")
    print(f"   {'='*50}")
    
    # Add a sentinel (0 height) at the end to process remaining bars
    for i in range(n + 1):
        current_height = heights[i] if i < n else 0
        print(f"\n   Bar {i}: height = {'∞' if i == n else current_height}")
        
        # While current height is less than height at stack top
        while stack and current_height < heights[stack[-1]]:
            height = heights[stack.pop()]
            
            # Width = current index - stack top index - 1
            # If stack is empty, the bar can extend to the beginning
            left_boundary = stack[-1] if stack else -1
            width = i - left_boundary - 1
            
            area = height * width
            print(f"   → Rect height={height}, width={width}, area={area}")
            
            max_area = max(max_area, area)
        
        stack.append(i)
        print(f"   Stack (indices): {stack} → heights: {[heights[idx] for idx in stack if idx < n]}")
    
    print(f"\n   ✅ Largest Rectangle Area: {max_area}")
    return max_area


# ==============================================================================
# 4️⃣  PRACTICE PROBLEMS (Start Here!)
# ==============================================================================
"""
📋 STACK PRACTICE ROADMAP (Beginner → Advanced)

🟢 LEVEL 1: BASIC (Start Here!)
   1. ✅ Implement stack using list (done above)
   2. ✅ Valid Parentheses (Problem 1 above)
   3. Implement stack using queue
   4. Reverse a string using stack
   5. Delete middle element from stack

🟡 LEVEL 2: INTERMEDIATE
   6. ✅ Min Stack (Problem 2 above)
   7. ✅ Next Greater Element (Problem 3 above)
   8. ✅ Stock Span Problem (Problem 4 above)
   9. Queue using two stacks
   10. Sort a stack using recursion

🔴 LEVEL 3: ADVANCED
   11. ✅ Infix to Postfix (Problem 5 above)
   12. ✅ Evaluate Postfix (Problem 6 above)
   13. ✅ Largest Rectangle in Histogram (Problem 7 above)
   14. Maximum area rectangle in binary matrix
   15. The Celebrity Problem
   16. Sliding Window Maximum (using deque)

⚫ LEVEL 4: CHALLENGING
   17. Longest Valid Parentheses
   18. Trapping Rain Water
   19. Remove K Digits (smallest number after removing k digits)
   20. Simplify Path (Unix-like file path)
"""


# ==============================================================================
# 5️⃣  MAIN FUNCTION - RUN EVERYTHING TOGETHER
# ==============================================================================

if __name__ == "__main__":
    
    print("\n" + "█" * 60)
    print("██  STACK DATA STRUCTURE - COMPLETE LEARNING MODULE")
    print("█" * 60)
    
    # ──────────────────────────────────────────────────────────────────────────
    # SECTION 1: Basic Stack Demo
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 SECTION 1: STACK BASICS - Understanding LIFO")
    print("=" * 60)
    print()
    print("💡 Think of a stack like a stack of plates in a cafeteria:")
    print("   • You can only add a plate to the TOP")
    print("   • You can only remove a plate from the TOP")
    print("   • The last plate placed is the first one removed")
    print()
    print("   This is exactly how Stack works in programming!")
    
    demo_basic_stack_operations()
    
    # ──────────────────────────────────────────────────────────────────────────
    # SECTION 2: Valid Parentheses
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 SECTION 2: PROBLEM 1 - VALID PARENTHESES")
    print("=" * 60)
    print()
    print("   Problem: Check if brackets are properly matched.")
    print("   This is the most common stack interview question!")
    
    test_cases = ["()", "()[]{}", "(]", "([)]", "{[]}"]
    for test in test_cases:
        result = is_valid_parentheses(test)
        print(f"   {'✅ Valid' if result else '❌ Invalid'}: '{test}'\n")
    
    # ──────────────────────────────────────────────────────────────────────────
    # SECTION 3: Min Stack
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 SECTION 3: PROBLEM 2 - MIN STACK")
    print("=" * 60)
    print()
    print("   Get minimum element in O(1) time!")
    
    ms = MinStack()
    print("\n   MinStack Demo:")
    for val in [3, 5, 2, 1, 4]:
        ms.push(val)
    ms.pop()
    ms.pop()
    print(f"   Current Min: {ms.get_min()}")
    
    # ──────────────────────────────────────────────────────────────────────────
    # SECTION 4: Next Greater Element
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 SECTION 4: PROBLEM 3 - NEXT GREATER ELEMENT")
    print("=" * 60)
    
    nge = next_greater_element([4, 5, 2, 25])
    print(f"\n   ✅ Result: {nge}\n")
    
    # ──────────────────────────────────────────────────────────────────────────
    # SECTION 5: Stock Span
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 SECTION 5: PROBLEM 4 - STOCK SPAN")
    print("=" * 60)
    
    spans = stock_span([100, 80, 60, 70, 60, 75, 85])
    print(f"\n   ✅ Spans: {spans}\n")
    
    # ──────────────────────────────────────────────────────────────────────────
    # SECTION 6: Infix to Postfix
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 SECTION 6: PROBLEM 5 - INFIX TO POSTFIX")
    print("=" * 60)
    
    postfix = infix_to_postfix("A+B*C")
    print(f"\n   ✅ Result: A+B*C → {postfix}\n")
    
    postfix2 = infix_to_postfix("(A+B)*C")
    print(f"\n   ✅ Result: (A+B)*C → {postfix2}\n")
    
    # ──────────────────────────────────────────────────────────────────────────
    # SECTION 7: Evaluate Postfix
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 SECTION 7: PROBLEM 6 - EVALUATE POSTFIX")
    print("=" * 60)
    
    result = evaluate_postfix("23*54*+")
    print(f"\n   ✅ 2*3 + 5*4 = {result}\n")
    
    # ──────────────────────────────────────────────────────────────────────────
    # SECTION 8: Largest Rectangle in Histogram
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 SECTION 8: PROBLEM 7 - LARGEST RECTANGLE IN HISTOGRAM")
    print("=" * 60)
    
    max_rect = largest_rectangle_in_histogram([2, 1, 5, 6, 2, 3])
    print(f"\n   ✅ Max Rectangle Area: {max_rect}\n")
    
    # ──────────────────────────────────────────────────────────────────────────
    # SUMMARY
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "█" * 60)
    print("📚  STACK MASTERY CHECKLIST")
    print("█" * 60)
    print()
    print("🟢 MUST KNOW (Fundamentals):")
    print("  ☐ Stack = LIFO (Last In First Out)")
    print("  ☐ push(), pop(), peek() are O(1)")
    print("  ☐ Valid Parentheses (😍 most asked)")
    print()
    print("🟡 GOOD TO KNOW (Intermediate):")
    print("  ☐ Next Greater Element (monotonic stack)")
    print("  ☐ Min Stack")
    print("  ☐ Stock Span Problem")
    print()
    print("🔴 ADVANCED LEVEL:")
    print("  ☐ Infix/Postfix Conversion")
    print("  ☐ Largest Rectangle in Histogram")
    print("  ☐ Longest Valid Parentheses")
    print()
    print("💪 TIPS FOR MASTERING STACK:")
    print("  1. Always draw the stack on paper when solving problems")
    print("  2. Remember: Stack is your 'memory' of previous elements")
    print("  3. Monotonic stacks are powerful for 'next greater/smaller' problems")
    print("  4. If you see parentheses in a problem → THINK STACK!")
    print("  5. Practice daily - even 15 minutes helps build intuition")
    print()
    print("🚀 NEXT STEPS:")
    print("  • Try to code each problem WITHOUT looking at the solution")
    print("  • Solve 'Valid Parentheses' on LeetCode (free account)")
    print("  • Explore the problems listed in the PRACTICE ROADMAP above")
    print("  • Come back and modify the code to test your understanding")
    print()
    print("🔥 KEEP GOING! Every expert was once a beginner!")
    print("=" * 60)