# 📚 Stacks & Queues — Master Guide

> A complete, placement-oriented guide to **Stacks and Queues** — the linear data
> structures used in many interview problems. Covers: LIFO stacks, FIFO queues,
> monotonic stacks, and the key patterns you need.

---

## 🗺️ Stacks & Queues Pattern Map

| Pattern | Difficulty | Key Problems | Key Idea |
|---|---|---|---|
| **1. Stack Basics** | Easy | Valid Parentheses, Min Stack | LIFO, push/pop/top |
| **2. Monotonic Stack** | Medium→Hard | Next Greater Element, Largest Rectangle | Stack maintains monotonic order |
| **3. Queue Basics** | Easy | Implement Queue with Stack, Circular Queue | FIFO, enqueue/dequeue |
| **4. Sliding Window / Deque** | Medium→Hard | Sliding Window Maximum, Task Scheduler | Double-ended queue |
| **5. BFS / Level Order** | Medium | Rotten Oranges, Task Scheduler | BFS using queue |

---

## 🧠 The Core Mindset

### Stack (LIFO — Last In, First Out)
```python
class Stack:
    def __init__(self):
        self.items = []
    def push(self, x): self.items.append(x)
    def pop(self): return self.items.pop()
    def top(self): return self.items[-1]
    def empty(self): return len(self.items) == 0
```

### Queue (FIFO — First In, First Out)
```python
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    def enqueue(self, x): self.items.append(x)
    def dequeue(self): return self.items.popleft()
    def front(self): return self.items[0]
    def empty(self): return len(self.items) == 0
```

---

## 📐 Key Templates

### Template 1: Valid Parentheses
```python
def is_valid(s):
    mapping = {')': '(', '}': '{', ']': '['}
    stack = []
    for ch in s:
        if ch in mapping:
            if not stack or stack.pop() != mapping[ch]:
                return False
        else:
            stack.append(ch)
    return len(stack) == 0
```

### Template 2: Monotonic Decreasing Stack (Next Greater Element)
```python
def next_greater_element(nums):
    stack = []  # stores indices
    result = [-1] * len(nums)
    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)
    return result
```

### Template 3: Min Stack
```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    def pop(self):
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()
    def top(self): return self.stack[-1]
    def getMin(self): return self.min_stack[-1]
```

### Template 4: Sliding Window Maximum (Monotonic Deque)
```python
def max_sliding_window(nums, k):
    from collections import deque
    dq = deque()  # stores indices, decreasing values
    result = []
    for i in range(len(nums)):
        # Remove indices outside window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        # Remove smaller values from back
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result
```

---

## 📖 Problem Mapping

| # | Pattern | Easy | Medium | Hard |
|---|---|---|---|---|
| **1. Stack Basics** | Valid Parentheses | Valid Parentheses, Min Stack | — |
| **2. Monotonic Stack** | Next Greater Element | — | Largest Rectangle, Daily Temperatures |
| **3. Queue Basics** | Implement Queue | Implement Queue with Stack | — |
| **4. Deque** | — | Sliding Window Maximum | Task Scheduler |
| **5. BFS** | — | Rotten Oranges | Task Scheduler |

---

## 🚀 Placement Strategy

### Phase 1: Stack Basics (Day 1)
- Code `01_valid_parentheses.py` from memory
- Code `02_min_stack.py` from memory

### Phase 2: Monotonic Stack (Day 2)
- Code `03_nearest_greater_to_left.py` and `04_nearest_greater_to_right.py`
- Understand the monotonic stack pattern

### Phase 3: Queue Basics (Day 3)
- Implement queue with two stacks
- Understand circular queue

### Phase 4: Advanced Patterns (Day 4)
- Code `05_sliding_window_maximum.py`
- Code `06_implement_queue_using_stacks.py`

---

## 📚 Resources

| Resource | Link |
|---|---|
| LeetCode Stack & Queue | https://leetcode.com/tag/stack/ |
| GFG Stack | https://www.geeksforgeeks.org/stack-data-structure/ |
| GFG Queue | https://www.geeksforgeeks.org/queue-data-structure/ |
| NeetCode Stack & Queue | https://neetcode.io/practice/data-structures/linked-list |

---

## ✅ Final Checklist

- [ ] Can implement a stack from scratch (array-based)
- [ ] Can implement a queue from scratch (linked list-based)
- [ ] Can code Valid Parentheses from memory
- [ ] Can code Min Stack from memory
- [ ] Can code Next Greater Element using monotonic stack
- [ ] Can code Sliding Window Maximum using deque
- [ ] Can implement Queue using two stacks
- [ ] Can code the bottom-up approach for largest rectangle
- [ ] Understands time complexity: O(n) for monotonic stack
