"""
================================================================================
                    TASK SCHEDULER ⭐⭐⭐ (Hot Interview Problem)
================================================================================
Given tasks (A-Z) and a cooldown n, find the minimum time to finish all tasks.
Same tasks must be separated by at least n units of time.

Example:
  tasks = ['A','A','A','B','B','B'], n = 2
  Output: 8
  Schedule: A → B → idle → A → B → idle → A → B

This problem combines GREEDY thinking with QUEUE intuition!
"""

from collections import Counter


# ==============================================================================
# PROBLEM: TASK SCHEDULER  (LeetCode 621) ⭐⭐⭐
# ==============================================================================
# LOGIC:
# 1. Count frequency of each task
# 2. The MOST frequent task dictates the schedule
# 3. Formula: (max_freq - 1) * (n + 1) + count_of_max_freq_tasks
# 4. Answer is max(formula, len(tasks))
#
# WHY THIS WORKS:
#   The most frequent task (say 'A' appears 3 times) needs:
#     A _ _ A _ _ A
#     (3-1) gaps of size n=2 between them = 2 * 2 = 4 slots
#     Plus the 3 A's themselves = 7 slots
#   Other tasks fill the gaps. If there are more tasks than gaps,
#   we just use len(tasks) (no idle needed).
#
# Time Complexity: O(tasks)
# Space Complexity: O(1) - at most 26 letters
# ------------------------------------------------------------------------------

def task_scheduler(tasks, n):
    """
    Find minimum intervals needed to complete all tasks.
    
    Time Complexity: O(tasks)
    Space Complexity: O(1) - at most 26 letters
    """
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
# VISUAL EXPLANATION 🧠
# ==============================================================================
"""
VISUALIZING THE FORMULA:
=========================

Example: tasks = ['A','A','A','B','B','B'], n = 2

Step 1: Count frequencies
  A: 3, B: 3
  max_freq = 3, max_count = 2 (both A and B appear 3 times)

Step 2: Visualize the most frequent task
  A _ _ A _ _ A
  ↑         ↑
  (3-1)=2 gaps of size n=2 each

Step 3: Fill gaps with other tasks
  A B _ A B _ A B
  ↑ ↑   ↑ ↑   ↑ ↑
  B fills the first gap, then B again, then B

Step 4: Count total slots
  A B _ A B _ A B = 8 slots
  Formula: (3-1) × (2+1) + 2 = 2 × 3 + 2 = 8 ✓

WHY max(len(tasks), formula)?
  If there are MANY different tasks, they might fill all gaps
  without needing idle time. In that case, answer = len(tasks).
  
  Example: tasks = ['A','B','C','D','E','F'], n = 2
  A B C D E F → 6 slots (no idle needed!)
  Formula: (1-1) × 3 + 1 = 1
  max(1, 6) = 6 ✓
"""


# ==============================================================================
# MAIN FUNCTION
# ==============================================================================

if __name__ == "__main__":
    
    print("\n" + "█" * 60)
    print("██  TASK SCHEDULER - Greedy + Queue Intuition")
    print("█" * 60)
    
    # ──────────────────────────────────────────────────────────────────────────
    # PROBLEM: Task Scheduler
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 PROBLEM: TASK SCHEDULER")
    print("=" * 60)
    print()
    print("   🧠 MENTAL MODEL:")
    print("   • The MOST frequent task dictates the schedule")
    print("   • Other tasks fill the 'idle' gaps")
    print("   • If tasks fill all gaps → no idle needed!")
    
    time_taken = task_scheduler(['A','A','A','B','B','B'], 2)
    print(f"\n   ✅ Minimum intervals: {time_taken}\n")
    
    # ──────────────────────────────────────────────────────────────────────────
    # VISUAL EXPLANATION
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 VISUAL EXPLANATION")
    print("=" * 60)
    print("""
   tasks = ['A','A','A','B','B','B'], n = 2
   
   A appears 3 times → needs 2 gaps of size 2:
     A _ _ A _ _ A
   
   Fill gaps with B:
     A B _ A B _ A B
   
   Total = 8 slots ✓
   
   Formula: (3-1) × (2+1) + 2 = 8
   """)
    
    # ──────────────────────────────────────────────────────────────────────────
    # MORE TEST CASES
    # ──────────────────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("📖 MORE TEST CASES")
    print("=" * 60)
    
    task_scheduler(['A','A','A','B','B','B'], 0)  # No cooldown
    task_scheduler(['A','A','A','B','B','B','C','C','C'], 2)  # 3 max freq
    task_scheduler(['A','B','C','D','E','F'], 2)  # All different
    
    print("\n🚀 NEXT: Run 09_practice_roadmap.py to see your full")
    print("   learning path and practice checklist!")