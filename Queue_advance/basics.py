"""
================================================================================
                    QUEUE - COMPLETE LEARNING MODULE 🚀
================================================================================

Welcome to your Queue learning journey! This folder is organized into
focused concept files. Follow them IN ORDER:

┌─────────────────────────────────────────────────────────────────────────────┐
│  📁 Queue_advance/                                                          │
│  ├── 01_queue_basics.py          → Queue concept + simple Queue class       │
│  ├── 02_circular_queue.py        → Efficient O(1) Circular Queue            │
│  ├── 03_deque.py                 → collections.deque + problems             │
│  ├── 04_queue_stack_conversions.py → Queue↔Stack conversions                │
│  ├── 05_basic_problems.py        → Generate binary, First negative, etc.    │
│  ├── 06_monotonic_queue.py       → Sliding Window Max/Min ⭐ INTERVIEW GOLD  │
│  ├── 07_bfs_rotten_oranges.py    → BFS with Queue (Rotten Oranges, 01 Matrix)│
│  ├── 08_task_scheduler.py        → Greedy + Queue intuition                 │
│  ├── 09_practice_roadmap.py      → Full checklist + 30-day schedule         │
│  └── README.md                   → Complete learning path guide             │
└─────────────────────────────────────────────────────────────────────────────┘

HOW TO USE:
  1. Run each file IN ORDER: python 01_queue_basics.py
  2. Read the explanations carefully
  3. Run the demos to SEE how queues work
  4. Try to code each implementation from memory
  5. Solve the practice problems on LeetCode
  6. Track your progress in 09_practice_roadmap.py
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
        "file": "01_queue_basics.py",
        "title": "QUEUE BASICS - Understanding FIFO",
        "description": "Learn what a queue is, FIFO principle, and the simple "
                       "list-based implementation (with its O(n) drawback).",
        "key_concepts": ["FIFO", "enqueue", "dequeue", "front", "rear"],
    },
    {
        "file": "02_circular_queue.py",
        "title": "CIRCULAR QUEUE - Efficient O(1) Operations",
        "description": "Fix the wasted space problem with circular wrapping. "
                       "Learn the magic of % (modulo) for wrap-around.",
        "key_concepts": ["Circular Queue", "modulo wrapping", "is_full", "O(1)"],
    },
    {
        "file": "03_deque.py",
        "title": "DEQUE - The Swiss Army Knife",
        "description": "Python's collections.deque - add/remove from BOTH ends "
                       "in O(1). Solve palindrome check and reveal cards.",
        "key_concepts": ["deque", "appendleft", "popleft", "double-ended"],
    },
    {
        "file": "04_queue_stack_conversions.py",
        "title": "QUEUE ↔ STACK CONVERSIONS",
        "description": "Implement a queue using two stacks, and a stack using "
                       "two queues. Learn amortized analysis!",
        "key_concepts": ["Queue using Stacks", "Stack using Queues", "amortized O(1)"],
    },
    {
        "file": "05_basic_problems.py",
        "title": "BASIC QUEUE PROBLEMS",
        "description": "Generate binary numbers, first negative in window, "
                       "reverse first K elements. Build your queue intuition!",
        "key_concepts": ["BFS generation", "window tracking", "queue + stack combo"],
    },
    {
        "file": "06_monotonic_queue.py",
        "title": "MONOTONIC QUEUE - SLIDING WINDOW ⭐",
        "description": "THE MOST IMPORTANT QUEUE INTERVIEW TOPIC! Sliding "
                       "Window Maximum/Minimum using monotonic deque.",
        "key_concepts": ["Monotonic Deque", "Sliding Window Max", "O(n) solution"],
    },
    {
        "file": "07_bfs_rotten_oranges.py",
        "title": "BFS - BREADTH FIRST SEARCH",
        "description": "The SUPERPOWER of queues! Rotten Oranges and 01 Matrix "
                       "using multi-source BFS on grids.",
        "key_concepts": ["BFS", "multi-source BFS", "level-by-level", "shortest path"],
    },
    {
        "file": "08_task_scheduler.py",
        "title": "TASK SCHEDULER",
        "description": "Hot interview problem combining greedy thinking with "
                       "queue intuition. Learn the formula!",
        "key_concepts": ["Greedy", "cooldown", "frequency counting"],
    },
    {
        "file": "09_practice_roadmap.py",
        "title": "PRACTICE ROADMAP & CHECKLIST",
        "description": "Your complete learning path, pattern templates, "
                       "30-day schedule, and LeetCode problem links.",
        "key_concepts": ["Patterns", "30-day plan", "checklist", "LeetCode links"],
    },
]


def show_learning_path():
    """Display the complete learning path."""
    print("\n" + "█" * 60)
    print("██  QUEUE LEARNING PATH - Follow In Order!")
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
    print("   Example: python 01_queue_basics.py")
    print()
    print("📌 OR run everything at once:")
    print("   python basics.py --run-all")
    print()


def run_all_modules():
    """Run all learning modules in sequence."""
    print("\n" + "█" * 60)
    print("██  RUNNING ALL QUEUE MODULES IN SEQUENCE")
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
    print("🎉 Congratulations on completing the Queue learning path!")
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