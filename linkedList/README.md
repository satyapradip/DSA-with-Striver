# 📚 Linked List Learning Path — Basic to Advanced

Welcome! This is your complete guide to mastering **Singly Linked Lists**
from scratch to interview-level problem solving. Follow this path in order.

---

## 📁 What's Inside This Folder

| File | Topic | Key Idea |
|---|---|---|
| `01_basic.py` | Build a linked list | `Node` + `head`, manual linking |
| `02_operations_in_LL.py` | Ops overview | Insert at begin/end/position in one class |
| `03_traversal_of_singly_LL.py` | Traversal | Walk with `current = current.next` |
| `04_insertion_at_begining.py` | Insert at head | `new_node.next = head`, O(1) |
| `05_insertion_at_end.py` | Insert at tail | Walk to end (or keep a `tail` pointer) |
| `06_insertion_at_specific_position.py` | Insert at position | Walk to `pos - 1`, relink carefully |
| `07_deletion_at_specific_position.py` | Delete at position | Single traversal, O(n) |
| `08_deletion_at_beginning.py` | Delete at head | `head = head.next`, O(1) |
| `09_deletion_at_end.py` | Delete at tail | Walk to second-last, set `next = None` |
| `10_Search an element in a Linked List.py` | Linear search | Walk until `data == target` |
| `11_Reverse a Linked List.py` | Reverse (iterative) | `prev / current / next_node` three-pointer flip |
| `12_middle_of_LL.py` | Middle node | Slow & fast pointers (tortoise–hare) |
| `13_detect_loop_in_LL.py` | Detect cycle | Floyd's algorithm — slow/fast meet? |
| `14_find_starting_of_loop_in_LL.py` | Cycle start node | Reset one pointer to head, walk both |
| `15_Check if a LinkedList is Palindrome or Not .py` | Palindrome check | Find middle → reverse first half → compare |
| `16_Length of loop in LL.py` | Cycle length | Freeze fast, count until it returns |
| `17_Segregate odd and even nodes in Linked List.py` | Odd–even list | Two chains (`odd`, `even`) merged at end |
| `18_Remove Nth node from the back of the LL.py` | Remove Nth from end | Dummy node + two pointers gap of n |
| `19_Delete the middle node in LL.py` | Delete middle | Slow/fast + predecessor link |
| `20_Sort a Linked List.py` | Sort a list | Merge sort on linked list — O(n log n) |
| `21_Add Two Numbers.py` | Add numbers as lists | Dummy head + carry, digit-by-digit |

Run any file with: `python "01_basic.py"` (quote names that contain spaces)

---

## 🗺️ The Roadmap

### Phase 1: Foundations — Nodes & Traversal (Day 1–2)
1. Run `01_basic.py` — understand `Node` (data + next) and the `head` reference
2. Run `02_operations_in_LL.py` — see every basic operation in one class
3. Run `03_traversal_of_singly_LL.py` — the `while current:` walk is the
   backbone of EVERY linked list problem

**Milestone:** Answer without looking:
> Why is `head` the only thing we must always keep track of?
> What's the difference between a node and a list?

---

### Phase 2: Insertion — The Relinking Skill (Day 3–4)
1. Run `04_insertion_at_begining.py` — O(1): point new node at head, move head
2. Run `05_insertion_at_end.py` — O(n): walk to the last node first
3. Run `06_insertion_at_specific_position.py` — walk to position-1, then
   **link in this order: new → next FIRST, then prev → new** (or you lose the chain!)

**Milestone:** Code from memory:
- Insert at head, insert at tail, insert at position
- State the time complexity of each

---

### Phase 3: Deletion — Don't Lose the Chain (Day 5–6)
1. Run `08_deletion_at_beginning.py` — just `head = head.next`
2. Run `09_deletion_at_end.py` — the hard one: singly lists need a walk to
   the second-last node
3. Run `07_deletion_at_specific_position.py` — combine both skills

**Milestone:** Do this on paper:
> Delete the middle node of `1 → 2 → 3 → 4 → 5` — which links must you update?
> Why can't a singly list delete from the tail in O(1)? (Hint: doubly list can!)

### Phase 4: Search & Reverse (Day 7–8)
1. Run `10_Search an element in a Linked List.py` — plain O(n) walk
2. Run `11_Reverse a Linked List.py` — ⭐ THE most important file in this
   folder. Three pointers: `prev`, `current`, `next_node`. Memorize the pattern:
   ```
   next_node = current.next   # save
   current.next = prev        # flip
   prev = current             # advance
   current = next_node
   ```

**Milestone:** Reverse `1 → 2 → 3 → 4 → 5` on PAPER, one arrow at a time,
without looking. Then code it from memory.

---

### Phase 5: Slow & Fast Pointers — The Superpower (Day 9–12) ⭐
This is where linked lists become **powerful**. The tortoise–hare technique
solves a whole family of problems in O(n) time, O(1) space.

1. Run `12_middle_of_LL.py` — fast moves 2 steps, slow moves 1 → fast lands
   at the end, slow lands at the middle
2. Run `13_detect_loop_in_LL.py` — if they meet, a cycle exists
3. Run `14_find_starting_of_loop_in_LL.py` — the beautiful trick: reset ONE
   pointer to `head`, move both at speed 1 → they meet at the cycle start
4. Run `16_Length of loop in LL.py` — freeze fast, count until you come back

**Milestone:** Explain out loud:
> WHY do they meet if a loop exists? (distance math: fast gains 1 step/cycle)
> WHY does resetting to head find the EXACT start of the loop?

---

### Phase 6: Classic Interview Problems (Day 13–17)
1. Run `15_Check if a LinkedList is Palindrome or Not .py` — find middle,
   reverse the first half, compare (three techniques combined!)
2. Run `17_Segregate odd and even nodes in Linked List.py` — maintain two
   chains, stitch them together at the end
3. Run `18_Remove Nth node from the back of the LL.py` — ⭐ dummy node +
   gap-of-n two pointers (avoids all edge cases of removing the head)
4. Run `19_Delete the middle node in LL.py` — keep a `prev` behind slow

**Milestone:** Solve WITHOUT hints:
- Remove Nth Node From End (19)
- Linked List Cycle (141) & Linked List Cycle II (142)

---

### Phase 7: Sorting & Hard Problems (Day 18–21)
1. Run `20_Sort a Linked List.py` — Merge Sort is THE sorting algorithm for
   linked lists (no random access → no quicksort). Aim for O(n log n)
2. Run `21_Add Two Numbers.py` — dummy head + carry loop, the pattern reused
   in "Add Two Numbers II" and "Multiply Strings"

**Milestone:** Code from memory:
- Merge sort on a linked list (split with slow/fast, merge with dummy)
- Add Two Numbers (2) with carry handling

---

## 🧠 Mental Model Cheat Sheet

| Operation | Time | Space | Note |
|---|---|---|---|
| Access element by index | O(n) | O(1) | No random access — must walk |
| Search (unsorted) | O(n) | O(1) | Linear scan |
| Insert at head | O(1) | O(1) | Just relink `head` |
| Insert at tail (no tail ptr) | O(n) | O(1) | Walk to end |
| Insert at tail (tail ptr) | O(1) | O(1) | Keep a `tail` reference |
| Delete at head | O(1) | O(1) | `head = head.next` |
| Delete at tail (singly) | O(n) | O(1) | Need second-last node |
| Delete at tail (doubly) | O(1) | O(1) | `tail = tail.prev` |
| Reverse (iterative) | O(n) | O(1) | Three-pointer flip |

| "I see this in a problem..." | Reach for |
|---|---|
| Find middle / kth from end | Slow & fast pointers |
| "Can you do it in O(1) space?" | Reverse in place / pointer surgery |
| Detect a loop | Floyd's tortoise & hare |
| Find where the loop starts | Reset one pointer to head |
| Reverse order | Iterative 3-pointer or recursion |
| Sorted list, divide & conquer | Merge sort on linked list |
| Dummy head keeps appearing | It kills "head might change" edge cases |
| Palindrome in a list | Middle → reverse half → compare |
| LRU cache (design) | Hash map + **doubly** linked list |

## 💡 Best Learning Suggestions (How to Actually Master This)

1. **Draw before you code** — on paper draw boxes and arrows for every
   problem. Pointer bugs are invisible in your head and obvious on paper.
2. **Never skip the edge cases** — empty list, single node, two nodes,
   removing the head, removing the tail. Interviewers probe exactly there.
3. **The relinking order mantra** — always "save next → relink → advance".
   If you overwrite `current.next` before saving, the rest of the list is lost.
4. **Master the three superpatterns** — everything else is a variation:
   - Reverse (3-pointer flip)
   - Slow & fast (middle / cycle / nth-from-end)
   - Dummy node (insert/delete anywhere without head edge cases)
5. **Retype, don't copy-paste** — close the file and rebuild each solution
   from memory. Reading code ≠ being able to write it.
6. **Explain out loud (rubber duck)** — if you can't explain WHY slow/fast
   meet, you'll freeze in an interview.
7. **Spaced repetition** — redo files 11, 13, 14, 18 at Day 7, 14, 21.
8. **Do it blind, then time yourself** — first solve with notes (learning),
   later solve in < 20 min (interview simulation).

---

## 🔗 LeetCode Problem Links (Copy into browser)

- Reverse Linked List (206): https://leetcode.com/problems/reverse-linked-list/
- Reverse Linked List II (92): https://leetcode.com/problems/reverse-linked-list-ii/
- Middle of the Linked List (876): https://leetcode.com/problems/middle-of-the-linked-list/
- Linked List Cycle (141): https://leetcode.com/problems/linked-list-cycle/
- Linked List Cycle II (142): https://leetcode.com/problems/linked-list-cycle-ii/
- Palindrome Linked List (234): https://leetcode.com/problems/palindrome-linked-list/
- Odd Even Linked List (328): https://leetcode.com/problems/odd-even-linked-list/
- Remove Nth Node From End of List (19): https://leetcode.com/problems/remove-nth-node-from-end-of-list/
- Delete the Middle Node of a Linked List (2095): https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
- Sort List (148): https://leetcode.com/problems/sort-list/
- Add Two Numbers (2): https://leetcode.com/problems/add-two-numbers/
- Add Two Numbers II (445): https://leetcode.com/problems/add-two-numbers-ii/
- Merge Two Sorted Lists (21): https://leetcode.com/problems/merge-two-sorted-lists/
- Merge k Sorted Lists (23): https://leetcode.com/problems/merge-k-sorted-lists/
- Intersection of Two Linked Lists (160): https://leetcode.com/problems/intersection-of-two-linked-lists/
- Rotate List (61): https://leetcode.com/problems/rotate-list/
- Remove Linked List Elements (203): https://leetcode.com/problems/remove-linked-list-elements/
- Swap Nodes in Pairs (24): https://leetcode.com/problems/swap-nodes-in-pairs/
- Reorder List (143): https://leetcode.com/problems/reorder-list/
- Design Linked List (707): https://leetcode.com/problems/design-linked-list/

**GeeksforGeeks:**
- Search in a Linked List: https://www.geeksforgeeks.org/problems/search-in-linked-list-1664464/1
- Linked List (all operations): https://www.geeksforgeeks.org/problems/linked-list/1

---

## ✅ Final Checklist Before Moving to Doubly_LinkedList

- [ ] Can build a singly linked list (Node + head) from memory
- [ ] Can insert at head / tail / position without losing the chain
- [ ] Can delete at head / tail / position, including all edge cases
- [ ] Can reverse a linked list iteratively AND recursively from memory
- [ ] Can explain slow & fast pointers and WHY Floyd's algorithm works
- [ ] Solved Linked List Cycle (141) and Cycle II (142) without help
- [ ] Solved Remove Nth From End (19) using a dummy node without help
- [ ] Can code merge sort on a linked list from memory
- [ ] Can explain when a dummy node is needed (and why it saves edge cases)
- [ ] Built intuition for: "pointers are links — draw them, then relink"
- [ ] Solved at least 20 linked list problems total

> When you finish this roadmap, **Trees** will feel much easier — a tree node
> is just a linked-list node with TWO pointers (`left` / `right`), and all the
> traversal discipline you built here carries straight over. Next stop:
> `Doubly_LinkedList`. Good luck — you've got this! 🚀


