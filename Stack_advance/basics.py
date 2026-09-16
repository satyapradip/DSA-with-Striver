"""
================================================================================
                     STACK - COMPLETE LEARNING MODULE 🚀
================================================================================

Welcome to your Stack learning journey! This folder is organized into
focused concept files. Follow them IN ORDER:

┌─────────────────────────────────────────────────────────────────────────────┐
│  📁 Stack_advance/                                                          │
│  ├── 01_stack_basics.py           → Stack concept + simple Stack class     │
│  ├── 02_stack_linked_list.py      → Array & Linked List implementations    │
│  ├── 03_basic_problems.py         → Valid Parentheses, Min Stack, etc.     │
│  ├── 04_stack_queue_conversions.py→ Stack↔Queue conversions                │
│  ├── 05_monotonic_stack.py        → NGE, Stock Span ⭐ INTERVIEW GOLD      │
│  ├── 06_expression_evaluation.py  → Infix/Postfix (compiler's stack)       │
│  ├── 07_advanced_problems.py      → Histogram, Trapping Rain Water ⭐⭐⭐⭐  │
│  ├── 08_practice_roadmap.py       → Full checklist + 30-day schedule       │
│  ├── basics.py                    → This launcher (run everything!)        │
│  └── README.md                    → Complete learning path guide           │
└─────────────────────────────────────────────────────────────────────────────┘

HOW TO USE:
  1. Run each file IN ORDER: python 01_stack_basics.py
  2. Read the explanations carefully
  3. Run the demos to SEE how stacks work
  4. Try to code each implementation from memory
  5. Solve the practice problems on LeetCode
  6. Track your progress in 08_practice_roadmap.py
"""

import subprocess
import sys
import os
import io

# Force UTF-8 output encoding for Windows compatibility with emoji/unicode
if sys.stdout and hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
if sys.stderr and hasattr(sys.stderr, "buffer"):
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")


# ==============================================================================
# LEARNING PATH GUIDE
# ==============================================================================

LEARNING_PATH = [
    {
        "file": "01_stack_basics.py",
        "title": "STACK BASICS - Understanding LIFO",
        "description": "Learn what a stack is, the LIFO principle, and the "
                       "simple list-based implementation (all O(1) ops).",
        "key_concepts": ["LIFO", "push", "pop", "peek", "top"],
    },
    {
        "file": "02_stack_linked_list.py",
        "title": "STACK IMPLEMENTATIONS - ARRAY & LINKED LIST",
        "description": "Rebuild the stack with a fixed-size array (overflow!) "
                       "and a linked list (dynamic memory). Compare them.",
        "key_concepts": ["ArrayStack", "LinkedListStack", "overflow", "top pointer"],
    },
    {
        "file": "03_basic_problems.py",
        "title": "BASIC PROBLEMS - Build Intuition",
        "description": "Valid Parentheses (most asked!), Min Stack in O(1), "
                       "and reversing a string with a stack.",
        "key_concepts": ["Valid Parentheses", "Min Stack", "two-stack trick"],
    },
    {
        "file": "04_stack_queue_conversions.py",
        "title": "STACK ↔ QUEUE CONVERSIONS",
        "description": "Implement a stack using two queues, and a queue using "
                       "two stacks. Learn amortized analysis!",
        "key_concepts": ["LIFO from FIFO", "FIFO from LIFO", "amortized O(1)"],
    },
    {
        "file": "05_monotonic_stack.py",
        "title": "MONOTONIC STACK - THE INTERVIEW GOLD ⭐",
        "description": "Next Greater Element (I & II circular) and Stock Span. "
                       "The most valuable stack pattern for interviews!",
        "key_concepts": ["Monotonic stack", "next greater", "stock span"],
    },
{
        "file": "06_expression_evaluation.py",
        "title": "EXPRESSION EVALUATION - The Compiler's Stack",
        "description": "Convert Infix → Postfix (Shunting Yard) and evaluate "
                       "postfix. See how compilers use stacks!",
        "key_concepts": ["Infix/Postfix", "precedence", "evaluation"],
    },
    {
        "file": "07_advanced_problems.py",
        "title": "ADVANCED PROBLEMS - Hard Monotonic Stack ⭐⭐⭐⭐",
        "description": "Largest Rectangle in Histogram and Trapping Rain "
                       "Water - FAANG interview classics solved with stacks.",
        "key_concepts": ["Histogram", "rain water", "boundaries"],
    },
    {
        "file": "08_practice_roadmap.py",
        "title": "PRACTICE ROADMAP & CHECKLIST",
        "description": "Your complete learning path, pattern templates, "
                       "30-day schedule, and LeetCode problem links.",
        "key_concepts": ["Patterns", "30-day plan", "checklist", "LeetCode links"],
    },
]


def show_learning_path():
    """Display the complete learning path."""
    print("\n" + "█" * 60)
    print("██  STACK LEARNING PATH - Follow In Order!")
    print("█" * 60)

    for i, module in enumerate(LEARNING_PATH, 1):
        print(f"\n{'─' * 60}")
        print(f"📘 MODULE {i}: {module['title']}")
        print(f"{'─' * 60}")
        print(f"   📄 File: {module['file']}")
        print(f"   📝 What you'll learn: {module['description']}")
        print(f"   🔑 Key concepts: {', '.join(module['key_concepts'])}")
        print(f"   ▶️  Run: python {module['file']}")

    print(f"\n{'─' * 60}")
    print("\n📌 QUICK START:")
    print("   Run each file in order to learn step by step!")
    print("   Example: python 01_stack_basics.py")
    print()
    print("📌 OR run everything at once:")
    print("   python basics.py --run-all")
    print()


def run_all_modules():
    """Run all learning modules in sequence."""
    print("\n" + "█" * 60)
    print("██  RUNNING ALL STACK MODULES IN SEQUENCE")
    print("█" * 60)

    for i, module in enumerate(LEARNING_PATH, 1):
        filepath = os.path.join(os.path.dirname(__file__), module["file"])
        print(f"\n{'=' * 60}")
        print(f"▶️  MODULE {i}/{len(LEARNING_PATH)}: {module['title']}")
        print(f"{'=' * 60}")

        try:
            # Set PYTHONIOENCODING=utf-8 so emoji/unicode print correctly
            env = os.environ.copy()
            env["PYTHONIOENCODING"] = "utf-8"

            result = subprocess.run(
                [sys.executable, filepath],
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                env=env,
            )
            print(result.stdout)
            if result.stderr:
                print(f"⚠️  Warnings/Errors:\n{result.stderr}")
        except Exception as e:
            print(f"❌ Error running {module['file']}: {e}")

    print("\n" + "█" * 60)
    print("✅ ALL MODULES COMPLETE!")
    print("█" * 60)
    print()
    print("🎉 Congratulations on completing the Stack learning path!")
    print("   Remember: Practice makes permanent. Keep coding!")


# ==============================================================================
# MAIN FUNCTION
# ==============================================================================

if __name__ == "__main__":

    # Check if user wants to run all modules
    if len(sys.argv) > 1 and sys.argv[1] == "--run-all":
        run_all_modules()
    else:
        show_learning_path()

        print("💡 TIP: Run 'python basics.py --run-all' to execute all modules!")