# 📚 Advanced Hashing — Master Guide

> A complete, placement-oriented guide to **advanced hashing** — the patterns that
> turn into interview questions. Builds on `basic_hashing` (character/number hashing,
> frequency arrays) and introduces **dict-based hashing**, **complement lookups**,
> **prefix sum + hashmap**, and **frequency-grouping**.

---

## 🗺️ Advanced Hashing Pattern Map

| Pattern | Difficulty | Key Problems | Key Idea |
|---|---|---|---|
| **1. Dict Hashing** (key ≠ value) | Easy | Two Sum, Contains Duplicate | Map key → count/index in O(1) |
| **2. Complement Lookup** | Easy→Medium | Two Sum, Four Sum, Valid Anagram | `needed = target - current` |
| **3. Prefix Sum + Hashmap** | Medium→Hard | Subarray Sum Equals K, Longest Subarray Sum K | `prefix_sum - k` seen before |
| **4. Frequency Grouping** | Easy→Medium | Group Anagrams, Sort by Frequency | Group by a hash key |
| **5. Top K Elements** | Medium | Top K Frequent Elements | Heap + frequency map |

---

## 🧠 The Core Hashing Mindset

### Array Hashing vs Dict Hashing

| | Array Hashing (basic) | Dict Hashing (advanced) |
|---|---|---|
| **Key type** | Integers (index = key) | Any hashable type (str, tuple, etc.) |
| **Key space** | Small & dense (e.g., 'a'–'z' → 26 slots) | Large & sparse (e.g., strings, names) |
| **Implementation** | `arr[key] = count` | `dict[key] = count` |
| **Use when** | Values in small range (0–25, 0–N) | Arbitrary keys, O(1) lookup needed |
| **Python** | List indexing | `dict` / `collections.Counter` |

### The 3 Golden Rules of Hashing

1. **Build once, query O(1)** — precompute a frequency map in O(n), then every query is O(1)
2. **Key space matters** — dense small range → array; anything else → dict
3. **Never re-count inside a query loop** — that defeats the purpose (O(n·Q) → O(n+Q))

---

## 📐 Key Templates

### Template 1: Dict Frequency Counter
```python
def count_freq(nums):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    return freq
# or using defaultdict
from collections import defaultdict
freq = defaultdict(int)
for num in nums:
    freq[num] += 1
```

### Template 2: Complement Lookup (Two Sum)
```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

### Template 3: Prefix Sum + Hashmap (Subarray Sum K)
```python
def subarray_sum_equals_k(nums, k):
    prefix_count = {0: 1}
    current_sum = 0
    count = 0
    for num in nums:
        current_sum += num
        count += prefix_count.get(current_sum - k, 0)
        prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1
    return count
```

### Template 4: Group by Frequency
```python
from collections import defaultdict
def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)
    return list(groups.values())
```

---

## 📖 Problem Mapping (By Difficulty)

| # | Pattern | Easy | Medium | Hard |
|---|---|---|---|---|
| **Dict Hashing** | Two Sum, Contains Duplicate | Two Sum, Contains Duplicate | — |
| **Complement Lookup** | Two Sum | 4Sum, Valid Anagram | — |
| **Prefix Sum + Hashmap** | — | Subarray Sum Equals K | — |
| **Frequency Grouping** | — | Group Anagrams | — |
| **Top K Elements** | — | Top K Frequent Elements | — |

---

## 🚀 Placement Strategy

### Phase 1: Dict Hashing (Day 1)
- Read this README
- Code `01_two_sum.py` from memory
- Code `02_contains_duplicate.py` from memory

### Phase 2: Complement Lookup (Day 2)
- Code `03_four_sum.py` (sorted two-pointers + dict for dedup)
- Code `04_group_anagrams.py` from memory

### Phase 3: Prefix Sum + Hashmap (Day 3–4)
- Code `05_subarray_sum_equals_k.py` from memory
- Code `06_longest_subarray_sum_k.py` (with non-negative constraint)

### Phase 4: Frequency Grouping (Day 5)
- Code `07_top_k_frequent.py` (heap + Counter)

### Phase 5: Mock Interviews (Day 6–7)
- Timed practice: 20 min per problem
- Simulate real interview: no editor, no hints

---

## 🔗 Next After This
After `advanced_hashing`, move to **Binary Search** (`Binary Search` folder already exists in repo).
