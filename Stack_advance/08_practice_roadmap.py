"""
================================================================================
                     STACK PRACTICE ROADMAP 📚
================================================================================
Your complete learning path from beginner to advanced!

HOW TO USE THIS FILE:
  1. Work through each level IN ORDER
  2. Check off items as you complete them
  3. Revisit Level 1-2 periodically (spaced repetition)
  4. Move to the next level only when comfortable
"""

# ==============================================================================
# STACK PRACTICE ROADMAP (Beginner → Advanced)
# ==============================================================================

print("""
================================================================================
📋 STACK MASTERY CHECKLIST
================================================================================

🟢 LEVEL 1: BASIC (Master the fundamentals)
   ☐ Stack = LIFO (Last In First Out)
   ☐ push at TOP, pop from TOP
   ☐ Implement stack using list (01_stack_basics.py ✅)
   ☐ Implement stack using fixed array (02_stack_linked_list.py ✅)
   ☐ Implement stack using linked list (02_stack_linked_list.py ✅)
   ☐ Valid Parentheses (03_basic_problems.py ✅)
   ☐ Reverse a string using stack (03_basic_problems.py ✅)
   ☐ Delete middle element of stack (YOUR TURN!)
   ☐ Implement stack using queue (04_stack_queue_conversions.py ✅)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🟡 LEVEL 2: INTERMEDIATE (Build patterns)
   ☐ Min Stack - O(1) min (03_basic_problems.py ✅)
   ☐ Queue using two stacks (04_stack_queue_conversions.py ✅)
   ☐ Understand amortized analysis (04_stack_queue_conversions.py ✅)
   ☐ Next Greater Element - MONOTONIC STACK! (05_monotonic_stack.py ✅)
   ☐ Next Greater Element II - circular (05_monotonic_stack.py ✅)
   ☐ Stock Span Problem (05_monotonic_stack.py ✅)
   ☐ Sort a stack using recursion (YOUR TURN!)
   ☐ Infix to Postfix (06_expression_evaluation.py ✅)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔴 LEVEL 3: ADVANCED (Interview-ready)
   ☐ Evaluate Postfix Expression (06_expression_evaluation.py ✅)
   ☐ Largest Rectangle in Histogram (07_advanced_problems.py ✅)
   ☐ Trapping Rain Water (07_advanced_problems.py ✅)
   ☐ Maximum area rectangle in binary matrix
   ☐ Sum of Subarray Minimums
   ☐ Remove K Digits

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚫ LEVEL 4: CHALLENGING (For the brave!)
   ☐ Longest Valid Parentheses
   ☐ Simplify Path (Unix file path)
   ☐ Asteroid Collision
   ☐ The Celebrity Problem
   ☐ Basic Calculator I / II (harder expression eval!)

================================================================================
🧠 MEMORIZE THESE PATTERNS
================================================================================

PATTERN 1: VALID PARENTHESES
  "Brackets match", "string with (, {, ["
  
  Template:
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []
    for char in s:
        if char in bracket_map:         # closing bracket
            if not stack or stack.pop() != bracket_map[char]:
                return False
        else:
            stack.append(char)           # opening bracket
    return not stack

PATTERN 2: MONOTONIC STACK
  "Next greater/smaller", "nearest bigger to left/right", "span"
  
  Template:
    stack = []
    for i in range(n):
        while stack and arr[i] "beats" arr[stack[-1]]:
            top = stack.pop()
            result[top] = arr[i]      # current element answers `top`
        stack.append(i)
    # leftovers: no answer → default (-1, 0, n, etc.)

PATTERN 3: EXPRESSION EVALUATION
  "Infix/Postfix/Prefix", "evaluate expression", "calculator"
  
  Template:
    operand → push to stack
    operator → pop b, pop a → compute (a op b) → push result

PATTERN 4: TWO-STACK DESIGNS
  "Implement X using Y", "get min/max in O(1)"
  
  Template:
    Second stack keeps "state history" at every level!
""")

# ==============================================================================
# LEETCODE PROBLEM LINKS FOR REFERENCE
# ==============================================================================

LEETCODE_PROBLEMS = {
    "Valid Parentheses": "https://leetcode.com/problems/valid-parentheses/",
    "Min Stack": "https://leetcode.com/problems/min-stack/",
    "Implement Stack using Queues": "https://leetcode.com/problems/implement-stack-using-queues/",
    "Implement Queue using Stacks": "https://leetcode.com/problems/implement-queue-using-stacks/",
    "Next Greater Element I": "https://leetcode.com/problems/next-greater-element-i/",
    "Next Greater Element II": "https://leetcode.com/problems/next-greater-element-ii/",
    "Online Stock Span": "https://leetcode.com/problems/online-stock-span/",
    "Evaluate Reverse Polish Notation": "https://leetcode.com/problems/evaluate-reverse-polish-notation/",
    "Largest Rectangle in Histogram": "https://leetcode.com/problems/largest-rectangle-in-histogram/",
    "Trapping Rain Water": "https://leetcode.com/problems/trapping-rain-water/",
    "Maximal Rectangle": "https://leetcode.com/problems/maximal-rectangle/",
    "Sum of Subarray Minimums": "https://leetcode.com/problems/sum-of-subarray-minimums/",
    "Remove K Digits": "https://leetcode.com/problems/remove-k-digits/",
    "Longest Valid Parentheses": "https://leetcode.com/problems/longest-valid-parentheses/",
    "Simplify Path": "https://leetcode.com/problems/simplify-path/",
    "Asteroid Collision": "https://leetcode.com/problems/asteroid-collision/",
    "Basic Calculator": "https://leetcode.com/problems/basic-calculator/",
    "Daily Temperatures": "https://leetcode.com/problems/daily-temperatures/",
}
# ==============================================================================
# 30-DAY PRACTICE SCHEDULE + TIPS
# ==============================================================================

print("""
================================================================================
🎯 30-DAY PRACTICE SCHEDULE
================================================================================

Day 1-2:   Stack basics, run 01, implement Stack from memory
Day 3-4:   Implement using linked list, run 02
Day 5-6:   Stack ↔ Queue conversions, run 04
Day 7-8:   Valid Parentheses + Min Stack, run 03
Day 9-10:  Monotonic stack intro, run 05 - NGE
Day 11-14: Monotonic stack problems - solve NGE 3x from memory!
Day 15-16: Stock Span + Daily Temperatures
Day 17-18: Expressions - run 06, convert + evaluate
Day 19-20: Hard problems - run 07, solve Histogram 3x!
Day 21:    Review everything - re-run all files
Day 22-25: Level 3 problems (Maximal Rectangle, Remove K Digits)
Day 26-28: Level 4 problems (Longest Valid Parentheses, Daily Temperatures)
Day 30:    MOCK INTERVIEW - solve 3 problems in 45 min!

================================================================================
✅ FINAL CHECKLIST BEFORE MOVING TO TREES
================================================================================

   ☐ Can implement Stack from memory (all O(1) ops)
   ☐ Can explain LIFO vs FIFO to a 5-year-old
   ☐ Solved Valid Parentheses without help
   ☐ Solved Next Greater Element 3 times independently
   ☐ Can code the monotonic stack template from memory
   ☐ Can convert Infix → Postfix and evaluate it
   ☐ Solved Largest Rectangle in Histogram without help
   ☐ Built intuition for: "When do I reach for a stack?"
   ☐ Solved at least 15 stack problems total

   When you finish, Trees & Graphs will come MUCH easier
   because recursion (tree traversal) uses the CALL STACK!
   You've got this! 🚀

💡 TIPS FROM A MENTOR:
   1. Draw the stack on paper for EVERY problem
   2. Stack = your "memory" of previous elements
   3. Monotonic stacks kill "next greater/smaller" problems in O(n)
   4. See parentheses in a problem → THINK STACK!
   5. Compare with Queue: everything you learned has a mirror
   6. Consistency beats intensity: 30 min every day > 4 hours weekly
""")

# ==============================================================================
# MAIN FUNCTION
# ==============================================================================

if __name__ == "__main__":
    print("\n" + "█" * 60)
    print("██  STACK PRACTICE ROADMAP")
    print("█" * 60)

    # The big checklist is printed above

    print("\n📌 LEETCODE PROBLEM LINKS:")
    print("-" * 60)
    for name, url in LEETCODE_PROBLEMS.items():
        print(f"   • {name}: {url}")

    print()
    print("🔥 REMEMBER: Consistency beats intensity!")
    print("   Practice 30 minutes EVERY day, not 4 hours once a week!")