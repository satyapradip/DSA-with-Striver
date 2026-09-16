"""
================================================================================
                     BASIC STACK PROBLEMS ⭐
================================================================================
Three classic beginner problems to build your stack intuition:

1. Valid Parentheses — the MOST ASKED stack question in interviews
2. Min Stack — design a stack that returns min in O(1)
3. Reverse a String — simplest possible stack application

Each problem demonstrates a DIFFERENT stack technique:
  1. Stack as "matcher" (push open brackets, match with close brackets)
  2. Stack of "history" (a second stack tracking min at each level)
  3. Stack as "reverser" (LIFO naturally reverses order!)
"""


# ==============================================================================
# PROBLEM 1: VALID PARENTHESES  (LeetCode 20) ⭐ THE MOST ASKED!
# ==============================================================================
# Given a string containing just '(', ')', '{', '}', '[' and ']', determine
# if the input string has valid parentheses.
#
# Example:
#   "()"     → True
#   "()[]{}" → True
#   "(]"     → False
#   "([)]"   → False
#   "{[]}"   → True
#
# LOGIC:
#   1. Map each closing bracket to its matching opening bracket
#   2. Iterate through each character:
#      - Opening bracket → push onto stack
#      - Closing bracket → check if stack's top matches!
#   3. At the end, stack should be EMPTY (every opener was matched)
#
# Visual:
#   "{[]}"
#   '{' → push    Stack: ['{']
#   '[' → push    Stack: ['{', '[']
#   ']' → top is '[' ✅ match → pop    Stack: ['{']
#   '}' → top is '{' ✅ match → pop    Stack: []
#   Stack empty → ✅ Valid!
# ------------------------------------------------------------------------------

def is_valid_parentheses(s: str) -> bool:
    """
    Check if parentheses are valid using a stack.

    Time Complexity: O(n) - we process each character once
    Space Complexity: O(n) - in worst case, all characters are opening brackets
    """
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []

    print(f"\n   Input String: '{s}'")
    print(f"   Processing...")

    for i, char in enumerate(s):
        if char in bracket_map:
            # It's a closing bracket
            top = stack.pop() if stack else '#'
            if top != bracket_map[char]:
                print(f"   Step {i+1}: '{char}' → ✗ Mismatch! "
                      f"Expected '{bracket_map[char]}', got '{top}'")
                return False
            print(f"   Step {i+1}: '{char}' → ✓ Matches '{top}' → Stack: {stack}")
        else:
            # It's an opening bracket - push to stack
            stack.append(char)
            print(f"   Step {i+1}: '{char}' → pushed → Stack: {stack}")

    if stack:
        print(f"   ✗ Unmatched opening brackets remaining: {stack}")
        return False
    print("   ✅ All brackets matched! Stack is empty.")
    return True
# ==============================================================================
# PROBLEM 2: MIN STACK  (LeetCode 155) ⭐⭐
# ==============================================================================
# Design a stack that supports push, pop, top, and retrieving the MINIMUM
# element in constant time O(1).
#
# LOGIC (TWO STACKS):
#   • Main stack  → stores every pushed element
#   • Min stack   → stores the MINIMUM AT EACH LEVEL
#
# Visual:
#   Push 3:  main=[3]     min=[3]      (min so far: 3)
#   Push 5:  main=[3,5]   min=[3,3]    (min so far: 3)
#   Push 2:  main=[3,5,2] min=[3,3,2]  (min so far: 2)
#   Pop  :   main=[3,5]   min=[3,3]    (min restored!)
# ------------------------------------------------------------------------------

class MinStack:
    """
    Stack that can return the minimum element in O(1) time.
    Uses TWO stacks: main + min-history.
    """

    def __init__(self):
        self.stack = []       # Main stack - all elements
        self.min_stack = []   # Tracks running minimum at each level

    def push(self, val: int) -> None:
        """Push value. O(1)"""
        self.stack.append(val)
        # New minimum = min(val, current minimum)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))
        print(f"   Pushed {val:>3} → Stack: {self.stack}, "
              f"Min: {self.get_min()}")

    def pop(self) -> None:
        """Pop top value. O(1)"""
        if self.stack:
            val = self.stack.pop()
            self.min_stack.pop()
            print(f"   Popped {val:>3} → Stack: {self.stack}", end="")
            if self.stack:
                print(f", Min: {self.get_min()}")
            else:
                print(" (empty)")

    def top(self) -> int:
        """View top value. O(1)"""
        return self.stack[-1] if self.stack else None

    def get_min(self) -> int:
        """Return minimum element in O(1)."""
        return self.min_stack[-1] if self.min_stack else None


# ==============================================================================
# PROBLEM 3: REVERSE A STRING USING STACK  ⭐
# ==============================================================================
# Reverse a string using a stack. Why? Because LIFO naturally REVERSES order!
#
# Example:
#   "hello" → push h,e,l,l,o then pop → "olleh"
# ==============================================================================
# MAIN FUNCTION
# Visual:
#   String:  h  e  l  l  o
#   Push:    h, e, l, l, o
#   Stack:   [h, e, l, l, o]   (o on top)
#   Pop:     o, l, l, e, h → "olleh" ✅ REVERSED!
# ------------------------------------------------------------------------------

def reverse_string_using_stack(s: str) -> str:
    """
    Reverse a string using a stack.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    stack = []
    print(f"\n   Original string: '{s}'")
    print(f"   {'-'*50}")

    # Step 1: Push every character
    for ch in s:
        stack.append(ch)
    print(f"   After pushing: stack = {stack}")

    # Step 2: Pop every character (LIFO order = reversed!)
    reversed_chars = []
    while stack:
        ch = stack.pop()
        reversed_chars.append(ch)
        print(f"   Popped '{ch}' → building: '{''.join(reversed_chars)}'")

    result = "".join(reversed_chars)
    print(f"   ✅ Reversed string: '{result}'")
    return result

    print("   ✅ All brackets matched! Stack is empty.")
    return True# ==============================================================================

if __name__ == "__main__":

    print("\n" + "█" * 60)
    print("██  BASIC STACK PROBLEMS - Build Your Intuition")
    print("█" * 60)

    # ──────────────────────────────────────────────────────────────────────────
    # PROBLEM 1: Valid Parentheses
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 PROBLEM 1: VALID PARENTHESES (THE MOST ASKED!)")
    print("=" * 60)
    print()
    print("   🧠 MENTAL MODEL:")
    print("   • Opening bracket → push (waiting for its pair)")
    print("   • Closing bracket → check the TOP matches")
    print("   • Empty stack at the end = valid!")

    test_cases = ["()", "()[]{}", "(]", "([)]", "{[]}", ")"]
    for test in test_cases:
        result = is_valid_parentheses(test)
        print(f"   {'✅ Valid' if result else '❌ Invalid'}: '{test}'\n")

    # ──────────────────────────────────────────────────────────────────────────
    # PROBLEM 2: Min Stack
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 PROBLEM 2: MIN STACK - O(1) minimum retrieval")
    print("=" * 60)
    print()
    print("   🧠 MENTAL MODEL:")
    print("   • Two stacks: normal + 'minimum so far'")
    print("   • Every push stores min(val, current_min)")
    print("   • Pop removes from BOTH stacks together")

    ms = MinStack()
    print("\n   Demo: push 3, 5, 2, 1, 4")
    print("   " + "-" * 45)
    for val in [3, 5, 2, 1, 4]:
        ms.push(val)
    print(f"   Current Min: {ms.get_min()}")
    ms.pop()
    ms.pop()
    print(f"   After 2 pops → Min: {ms.get_min()}\n")

    # ──────────────────────────────────────────────────────────────────────────
    # PROBLEM 3: Reverse a String
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 PROBLEM 3: REVERSE A STRING USING STACK")
    print("=" * 60)
    print()
    print("   🧠 MENTAL MODEL:")
    print("   • Push all characters")
    print("   • Pop all characters → they come out REVERSED (LIFO!)")

    reverse_string_using_stack("hello")
    reverse_string_using_stack("DSA")

    print("\n🚀 NEXT: Run 04_stack_queue_conversions.py to learn how to")
    print("   convert between stacks and queues (LeetCode 225 & 232)!")
#
