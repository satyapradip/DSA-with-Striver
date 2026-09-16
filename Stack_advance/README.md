# 📚 Stack Learning Path — Basic to Advanced

Welcome! This is your complete guide to mastering **Stacks** from scratch to
interview-level problem solving. Follow this path in order.

---

## 🗺️ The Roadmap

### Phase 1: Foundations (Day 1–2)
1. Understand LIFO (Last In First Out) — opposite of Queue's FIFO
2. Run `01_stack_basics.py` — see the simple stack demo
3. Understand WHY all stack ops are `O(1)` (append/pop at the end)

**Milestone:** Answer this without looking:
> What's the difference between `push/pop` (stack) vs `enqueue/dequeue` (queue)?
> Where does each operation happen in a stack?

---

### Phase 2: Implementations (Day 3–4)
1. Study the **Fixed-Size Array Stack** — understand `top` pointer & OVERFLOW
2. Study the **Linked List Stack** — dynamic memory, push/pop at head
3. Compare all three implementations (list vs array vs linked list)
4. Implement a linked list stack YOURSELF from scratch (no peeking!)

**Milestone:** Code a Stack class from memory:
- `push`, `pop`, `peek`, `is_empty`, `size`
- All operations must be **O(1)**

---

### Phase 3: Stack ↔ Queue Conversions (Day 5–6)
1. **Stack using Two Queues** — understand the "rotate" trick
2. **Queue using Two Stacks** — understand the "transfer" trick
3. Analyze time complexity of each operation (amortized analysis!)

**Milestone:** Explain to yourself:
> Why is push in StackUsingQueues O(n)?
> Why is dequeue in QueueUsingStacks "amortized O(1)"?

---

### Phase 4: Monotonic Stack — The Superpower of Stacks (Day 7–10) ⭐
This is where stacks become **powerful**. It's the stack version of the
monotonic deque from the Queue module.

1. Study **Next Greater Element** very carefully
2. Understand WHY we pop smaller elements (they get "answered"!)
3. Try the mirror problems:
   - Next Greater Element II (circular array)
   - Stock Span / Daily Temperatures
   - Sum of Subarray Minimums (hard!)

**Milestone:** Solve "Next Greater Element" on LeetCode WITHOUT hints.

---

### Phase 5: Expression Evaluation (Day 11–14)
Compilers use stacks everywhere. This is your "BFS moment" for stacks!

1. Study **Infix → Postfix** (the Shunting Yard algorithm)
2. Understand operator precedence & why '(' blocks the stack
3. Study **Evaluate Postfix** — the beautiful 3-rule algorithm
4. Try: Basic Calculator I & II, Evaluate Reverse Polish Notation

**Milestone:** Convert `"A+B*C-D/E"` to postfix on PAPER from memory,
then evaluate `"23*54*+"` mentally → `26`.

---

### Phase 6: Advanced Applications (Day 15+)
1. **Largest Rectangle in Histogram** — the famous hard problem
2. **Trapping Rain Water** — walls, valleys, and water 💧
3. **Design Problems:**
   - Min Stack (done in Phase 1 problems, O(1) min!)
   - Two-stack queue / two-queue stack
4. **Even harder:**
   - Maximal Rectangle (Histogram on a matrix)
   - Longest Valid Parentheses
   - Asteroid Collision
   - Remove K Digits

---

## 🧠 Mental Model Cheat Sheet

| Scenario | Data Structure | Why |
|---|---|---|
| "Last action first (undo)" | Stack | LIFO natural fit |
| "Matching brackets" | Stack | Push open, match close |
| "Function calls / recursion" | Stack | The call stack! |
| "Next/previous greater element" | Monotonic Stack | Pop smaller, get answered |
| "Process in arrival order" | Queue | FIFO natural fit |
| "Level by level / shortest path" | Queue (BFS) | BFS explores level-by-level |
| "Sliding window max/min" | Deque (monotonic) | Remove useless elements |
| "Expression evaluation" | Stack | Operator precedence |
| "Implement X using Y" | Two stacks/queues | Transfer & rotate tricks |
---

## 🔑 Pattern Recognition (The Secret to Problem Solving)

### Pattern 1: Valid Parentheses Family
**How to spot it:** "brackets match", "check string has separator balance"

```python
def is_valid(s):
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []
    for char in s:
        if char in bracket_map:
            if not stack or stack.pop() != bracket_map[char]:
                return False
        else:
            stack.append(char)
    return not stack
```

### Pattern 2: Monotonic Stack
**How to spot it:** "next/previous greater or smaller element", "span", "nearest bigger"

```python
def next_greater(arr):
    stack = []          # stores indices of "waiting" elements
    result = [-1] * len(arr)
    for i in range(len(arr)):
        # current "beats" the waiting elements on top
        while stack and arr[i] > arr[stack[-1]]:
            result[stack.pop()] = arr[i]
        stack.append(i)
    return result
```

### Pattern 3: Expression Evaluation / Compiler
**How to spot it:** "infix/postfix/prefix", "evaluate expression", "calculator"

**Template:** operand → push; operator → pop `b`, pop `a`, compute `(a op b)`, push.

### Pattern 4: Two-Stacks / Two-Queues Designs
**How to spot it:** "implement X using Y", "get min/max in O(1)",
"amortized O(1)"

**Template:** a second structure keeps the *history/state* at every level.

---

## 📝 30-Day Practice Schedule

| Day | Topic | Problem Set |
|---|---|---|
| 1 | Stack basics | Run `01_stack_basics.py`, implement from memory |
| 2 | Linked-list stack | Run `02_stack_linked_list.py`, build from scratch |
| 3 | Review implementations | Compare list vs array vs linked list |
| 4 | Valid Parentheses | LeetCode 20 (solve 3 times!) |
| 5 | Min Stack | LeetCode 155 |
| 6 | Reverse string using stack | Code with `collections.deque` |
| 7 | Stack using 2 queues | LeetCode 225 |
| 8 | Queue using 2 stacks | LeetCode 232 |
| 9 | Review both conversions | Explain amortized O(1) out loud |
| 10 | Monotonic stack intro | Next Greater Element (496) ⭐ |
| 11 | Monotonic stack | Next Greater Element II (503) |
| 12 | Monotonic stack | Daily Temperatures (739) |
| 13 | Monotonic stack | Online Stock Span (901) |
| 14 | Review monotonic stack | Solve NGE from complete memory |
| 15 | Expressions | Infix → Postfix on paper |
| 16 | Expressions | Evaluate Postfix (150) |
| 17 | Expressions | Infix → Prefix (bonus) |
| 18 | Hard | Largest Rectangle in Histogram (84) ⭐ first try |
| 19 | Hard | Largest Rectangle in Histogram (84) from memory |
| 20 | Hard | Trapping Rain Water (42) ⭐ |
| 21 | Review week 1–3 | Re-run all files, re-solve Level 1 problems |
| 22 | Design | Min Stack variants / two-stack queue |
| 23 | Hard | Maximal Rectangle (85) |
| 24 | Hard | Sum of Subarray Minimums (907) |
| 25 | Hard | Remove K Digits (402) |
| 26 | Hard | Longest Valid Parentheses (32) |
| 27 | Hard | Asteroid Collision (735) |
| 28 | Review week 4 | Re-solve all Level 2–3 problems |
| 29 | Mock interview | 45-min session, 2 problems |
| 30 | MOCK INTERVIEW DAY | 3 problems — full simulation |
---

## 💡 Advice From a Mentor

1. **Don't just read** — write every implementation by hand
2. **Draw diagrams** — top arrow, push/pop flow, monotonic stack snapshots
3. **Explain out loud** — the "rubber duck" method works!
4. **Spaced repetition** — redo problems at Day 7, 14, 21, 30
5. **Patterns > Memorization** — learn to RECOGNIZE stack patterns
6. **The monotonic stack is your new best friend** — it kills a whole family
   of "next greater / nearest smaller" problems in O(n)
7. **Compare with Queue** — everything you learned in Queue has a Stack mirror
8. **If you see parentheses, think stack. If you see a call stack, think stack.**

---

## 🔗 LeetCode Problem Links (Copy into browser)

- Valid Parentheses: https://leetcode.com/problems/valid-parentheses/
- Min Stack: https://leetcode.com/problems/min-stack/
- Implement Stack using Queues: https://leetcode.com/problems/implement-stack-using-queues/
- Implement Queue using Stacks: https://leetcode.com/problems/implement-queue-using-stacks/
- Next Greater Element I: https://leetcode.com/problems/next-greater-element-i/
- Next Greater Element II: https://leetcode.com/problems/next-greater-element-ii/
- Daily Temperatures: https://leetcode.com/problems/daily-temperatures/
- Online Stock Span: https://leetcode.com/problems/online-stock-span/
- Evaluate Reverse Polish Notation: https://leetcode.com/problems/evaluate-reverse-polish-notation/
- Largest Rectangle in Histogram: https://leetcode.com/problems/largest-rectangle-in-histogram/
- Trapping Rain Water: https://leetcode.com/problems/trapping-rain-water/
- Maximal Rectangle: https://leetcode.com/problems/maximal-rectangle/
- Sum of Subarray Minimums: https://leetcode.com/problems/sum-of-subarray-minimums/
- Remove K Digits: https://leetcode.com/problems/remove-k-digits/
- Longest Valid Parentheses: https://leetcode.com/problems/longest-valid-parentheses/
- Asteroid Collision: https://leetcode.com/problems/asteroid-collision/

---

## ✅ Final Checklist Before Moving to Trees

- [ ] Can implement Stack from memory (all O(1) ops)
- [ ] Can implement Stack using Linked List from memory
- [ ] Can explain LIFO vs FIFO to a 5-year-old
- [ ] Solved Valid Parentheses 3 times independently
- [ ] Solved Next Greater Element without help
- [ ] Can code the monotonic stack template from memory
- [ ] Can convert Infix → Postfix and evaluate Postfix from memory
- [ ] Solved Largest Rectangle in Histogram without help
- [ ] Solved Trapping Rain Water without help
- [ ] Can explain "amortized O(1)" to a friend
- [ ] Built intuition for: "When do I reach for a stack?"
- [ ] Solved at least 15 stack problems total

> When you finish this roadmap, Trees and Graphs will come MUCH easier
> because recursion (which trees use everywhere) runs on the CALL STACK.
> Good luck — you've got this! 🚀