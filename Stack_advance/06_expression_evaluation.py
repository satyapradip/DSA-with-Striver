"""
================================================================================
                     EXPRESSION EVALUATION - COMPILER'S STACK ⭐⭐⭐
================================================================================
This is where stacks become POWERFUL. Compilers use stacks to:
  1. Convert infix expressions   (A+B*C)  → postfix (ABC*+)
  2. Evaluate postfix expressions (ABC*+) → result

WHY POSTFIX? Because it needs NO parentheses and NO look-ahead!
Computers evaluate postfix with a simple left-to-right scan + stack.

🧠 WHY DOES COMPILER SCIENCE USE STACKS?
  • Infix "A+B*C": the * must happen BEFORE the + (precedence!)
  • A stack remembers operators that must "wait" for their operands
  • Postfix "ABC*+": operand → push; operator → pop 2, compute, push

⬇️ NOTATION CONVERSIONS:
┌────────────┬───────────────────────┬───────────────────────────┐
│ Notation   │ Example               │ Human friendly            │
├────────────┼───────────────────────┼───────────────────────────┤
│ INFIX      │ A + B * C             │ What we write ✅          │
│ PREFIX     │ + A * B C             │ operator FIRST (Polish)   │
│ POSTFIX    │ A B C * +             │ operator LAST (Reverse)   │
└────────────┴───────────────────────┴───────────────────────────┘

OPERATOR PRECEDENCE (higher = computed first):
  ^ (exponent) : 3
  *, /         : 2
  +, -         : 1
"""

# ==============================================================================
# PROBLEM 1: INFIX TO POSTFIX  (Shunting Yard by Dijkstra) ⭐⭐⭐
# ==============================================================================
# Convert an infix expression like "A+B*C" → "ABC*+"
#
# Example:
#   "A+B*C"   → "ABC*+"
#   "(A+B)*C" → "AB+C*"
#
# ALGORITHM:
#   1. Scan left → right
#   2. Operand → append to output
#   3. '('     → push to stack
#   4. ')'     → pop to output until '(' is found (then discard '(')
#   5. Operator → pop higher/equal precedence operators to output,
#                 then push current operator
#   6. At the end, pop everything remaining to output
# ------------------------------------------------------------------------------

def infix_to_postfix(expression: str) -> str:
    """
    Convert infix expression to postfix using a stack.

    Time Complexity: O(n) - single scan + each char pushed/popped once
    Space Complexity: O(n)
    """
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
            print(f"   '(' → Push. Stack: {stack}")

        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Remove the '('
            print(f"   ')' → Pop till '(' → Output: {''.join(output)}, "
                  f"Stack: {stack}")

        else:  # Operator
            while (stack and stack[-1] != '(' and
                   precedence.get(stack[-1], 0) >= precedence.get(char, 0)):
                output.append(stack.pop())
            stack.append(char)
            print(f"   '{char}' is operator → Stack: {stack}, "
                  f"Output: {''.join(output)}")

    # Pop remaining operators from stack
    while stack:
        output.append(stack.pop())

    result = "".join(output)
    print(f"\n   ✅ Postfix: {result}")
    return result
# ==============================================================================
# PROBLEM 2: EVALUATE POSTFIX EXPRESSION  (LeetCode 150) ⭐⭐⭐
# ==============================================================================
# Evaluate a postfix expression like "23*54*+" = (2*3) + (5*4) = 26
#
# ALGORITHM:
#   1. Scan left → right
#   2. Operand → push onto stack
#   3. Operator → pop TWO operands (b = top, a = next), compute, push result
#   4. At the end, stack contains the single final result
#
# Note: this version supports multi-digit numbers and spaces ("10 2 +").
# ------------------------------------------------------------------------------

def evaluate_postfix(expression: str):
    """
    Evaluate a postfix expression using a stack.
    Supports multi-digit integers separated by spaces.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    stack = []
    tokens = expression.split()

    print(f"\n   Postfix Expression: {expression}")
    print(f"   {'-'*40}")

    for token in tokens:
        if token.lstrip('-').isdigit():
            stack.append(int(token))
            print(f"   Operand '{token}' → Push. Stack: {stack}")
        else:
            b = stack.pop()  # Second operand (top)
            a = stack.pop()  # First operand
            result = {
                '+': a + b,
                '-': a - b,
                '*': a * b,
                '/': int(a / b),  # truncate toward zero (LeetCode rule)
                '^': a ** b,
            }[token]
            stack.append(result)
            print(f"   Operator '{token}': {a} {token} {b} = {result} → "
                  f"Stack: {stack}")

    # Final result = only element left on the stack
    print(f"\n   ✅ Final Result: {stack[0]}")
    return stack[0]


# ==============================================================================
# VISUAL EXPLANATION 🧠
# ==============================================================================
"""
VISUALIZING EVALUATION:
=========================

Expression: "23*54*+"   →  2 3 * 5 4 * +

  Scan "2"  → push     Stack: [2]
  Scan "3"  → push     Stack: [2, 3]
  Scan "*"  → pop 3, pop 2 → 2*3 = 6 → push   Stack: [6]
  Scan "5"  → push     Stack: [6, 5]
  Scan "4"  → push     Stack: [6, 5, 4]
  Scan "*"  → pop 4, pop 5 → 5*4 = 20 → push  Stack: [6, 20]
  Scan "+"  → pop 20, pop 6 → 6+20 = 26 → push Stack: [26]

  FINAL: 26 ✅   (remember: b = top, a = next → a op b!)
"""
# ==============================================================================
# MAIN FUNCTION
# ==============================================================================

if __name__ == "__main__":

    print("\n" + "█" * 60)
    print("██  EXPRESSION EVALUATION - The Compiler's Stack")
    print("█" * 60)

    # ──────────────────────────────────────────────────────────────────────────
    # PROBLEM 1: Infix to Postfix
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 PROBLEM 1: INFIX → POSTFIX (Shunting Yard)")
    print("=" * 60)
    print()
    print("   🧠 MENTAL MODEL:")
    print("   • Operands go straight to output")
    print("   • Operators wait on the stack for higher-precedence friends")
    print("   • '(' blocks everything until its matching ')' arrives")

    infix_to_postfix("A+B*C")
    infix_to_postfix("(A+B)*C")
    infix_to_postfix("A+B*C-D/E")

    # ──────────────────────────────────────────────────────────────────────────
    # PROBLEM 2: Evaluate Postfix
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 PROBLEM 2: EVALUATE POSTFIX (LeetCode 150)")
    print("=" * 60)
    print()
    print("   🧠 MENTAL MODEL:")
    print("   • Operand → push")
    print("   • Operator → pop b, pop a, compute (a op b), push result")
    print("   • Final: exactly ONE value left on the stack")

    result = evaluate_postfix("2 3 * 5 4 * +")
    print(f"\n   ✅ 2*3 + 5*4 = {result}\n")

    # ──────────────────────────────────────────────────────────────────────────
    # BONUS: Full pipeline
    # ──────────────────────────────────────────────────────────────────────────
    print("=" * 60)
    print("📖 BONUS: THE FULL COMPILER PIPELINE")
    print("=" * 60)

    infix = "10+2*6"
    postfix = infix_to_postfix(infix)
    # Convert each char for the evaluator (no spaces version)
    spaced = " ".join(postfix)
    value = evaluate_postfix(spaced)
    print(f"\n   🔗 {infix} → {postfix} → {value}")
    print(f"   ✅ Verified! 10 + 2*6 = {10 + 2 * 6}")

    print("\n🚀 NEXT: Run 07_advanced_problems.py for the HARD problems")
    print("   (Largest Rectangle in Histogram + Trapping Rain Water)!")