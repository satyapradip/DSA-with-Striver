# 📚 Graphs (BFS/DFS) — Master Guide

> A complete, placement-oriented guide to **Graph Traversal** — BFS (Breadth-First Search)
> and DFS (Depth-First Search). These patterns form the backbone of many interview problems
> involving networks, grids, and connectivity.

---

## 🗺️ Graph Patterns Map

| Pattern | Difficulty | Key Problems | Key Idea |
|---|---|---|---|
| **1. BFS (Queue)** | Easy | Level order tree, Rotten oranges, Island perimeter | FIFO queue, shortest path in unweighted graph |
| **2. DFS (Stack/Recursion)** | Easy | Connected components, Number of islands | LIFO stack/recursion, explores deeply first |
| **3. Union-Find / Disjoint Set** | Easy→Medium | Number of provinces, Redundant connection | Track connected components with Union-Find |
| **4. Graph Representation** | Easy | Adjacency list vs matrix | Choose the right representation |
| **5. Shortest Path (Unweighted)** | Medium | 0-1 BFS, Word ladder, Shortest path in grid | BFS guarantees shortest path |
| **6. Cycle Detection** | Medium | Detect cycle in directed/undirected graph | Color marking (0=unvisited, 1=visiting, 2=visited) |
| **7. Topological Sort** | Medium→Hard | Course schedule, Alien dictionary | Kahn's algorithm (BFS) or DFS |

---

## 🧠 The Core Mindset

### Graph Representation
```python
# Adjacency List (recommended for sparse graphs)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}

# Adjacency Matrix (for dense graphs)
# matrix[i][j] = 1 if edge from i to j
```

### BFS Template (Queue-based)
```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node)  # Process node

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

### DFS Template (Recursion-based)
```python
def dfs(graph, node, visited):
    visited.add(node)
    print(node)  # Process node

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

visited = set()
dfs(graph, 'A', visited)
```

### DFS Template (Iterative with Stack)
```python
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    visited.add(start)

    while stack:
        node = stack.pop()
        print(node)  # Process node

        for neighbor in reversed(graph[node]):  # reversed for consistent order
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
```

---

## 📖 Problem Mapping

| # | Pattern | Easy | Medium | Hard |
|---|---|---|---|---|
| **1. BFS (Queue)** | Easy | Level order tree, Rotten oranges | 0-1 BFS, Word ladder | Pacific Atlantic, Shortest bridge |
| **2. DFS (Recursion)** | Easy | Connected components, Island perimeter | Number of islands, Surrounded regions | — |
| **3. Union-Find** | Easy | Number of provinces | Redundant connection | — |
| **4. Graph Representation** | Easy | Adjacency list vs matrix | — | — |
| **5. Shortest Path** | Medium | 0-1 BFS, Word ladder | — | — |
| **6. Cycle Detection** | Medium | Detect cycle in directed/undirected graph | — | — |
| **7. Topological Sort** | Medium→Hard | Course schedule, Alien dictionary | — | — |

---

## 🚀 Placement Strategy

### Phase 1: BFS Basics (Day 1)
- Understand adjacency list representation
- Code BFS using queue (iterative)
- Run easy problems

### Phase 2: DFS Basics (Day 2)
- Understand recursion on graphs
- Code DFS using recursion and iterative
- Run easy problems

### Phase 3: BFS/DFS Patterns (Day 3)
- BFS with queue for level order
- DFS with recursion for connected components
- Run medium problems

### Phase 4: Advanced (Day 4)
- Union-Find
- Cycle detection
- Topological sort

### Phase 5: Mock Interviews (Day 5)
- Timed practice
- Simulate real interview conditions

---

## ✅ Final Checklist

- [ ] Can represent a graph using adjacency list and matrix
- [ ] Can code BFS using a queue from memory
- [ ] Can code DFS using recursion from memory
- [ ] Can code DFS iteratively using an explicit stack
- [ ] Can detect a cycle in a directed graph using 3-color marking
- [ ] Can detect a cycle in an undirected graph
- [ ] Can implement Union-Find with path compression
- [ ] Can perform topological sort using BFS (Kahn's algorithm)
- [ ] Can identify which graph problem type they're facing
- [ ] Can explain the difference between BFS and DFS
