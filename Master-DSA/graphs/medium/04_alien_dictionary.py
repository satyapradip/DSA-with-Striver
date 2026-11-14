# 📘 Graphs (BFS/DFS) — Medium 04
# Topic: Topological Sort — Alien Dictionary
# Approach: BFS (Kahn's algorithm) on character graph
# Time: O(V + E) where V = number of characters, E = number of word comparisons | Space: O(V + E)

from collections import deque, defaultdict

def alien_order(words):
    """
    Returns the lexicographical order of characters in an alien language.
    Returns empty string if the given words are invalid (e.g., contain a cycle).
    """
    # Step 1: Build graph and in-degree map
    graph = defaultdict(list)
    in_degree = {}

    # Initialize all characters
    for word in words:
        for char in word:
            in_degree[char] = 0

    # Step 2: Build graph edges
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        min_len = min(len(word1), len(word2))

        # Invalid case: "abc" comes after "ab" (prefix longer but appears first)
        if len(word1) > len(word2) and word1.startswith(word2):
            return ""

        # Find first different character
        for j in range(min_len):
            if word1[j] != word2[j]:
                # Add edge word1[j] -> word2[j]
                graph[word1[j]].append(word2[j])
                in_degree[word2[j]] += 1
                break

    # Step 3: Topological sort (Kahn's algorithm)
    queue = deque([char for char in in_degree if in_degree[char] == 0])
    result = []

    while queue:
        char = queue.popleft()
        result.append(char)

        for neighbor in graph[char]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check for cycle
    if len(result) != len(in_degree):
        return ""

    return ''.join(result)


def alien_order_brute(words):
    """
    Brute force: Build graph and do DFS-based topological sort.
    This version uses DFS instead of BFS.
    """
    graph = defaultdict(list)
    in_degree = {}

    # Initialize all characters
    for word in words:
        for char in word:
            in_degree[char] = 0

    # Build graph
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        min_len = min(len(word1), len(word2))

        if len(word1) > len(word2) and word1.startswith(word2):
            return ""

        for j in range(min_len):
            if word1[j] != word2[j]:
                graph[word1[j]].append(word2[j])
                in_degree[word2[j]] += 1
                break

    # DFS-based topological sort with cycle detection
    visited = {}  # 0 = unvisited, 1 = visiting, 2 = visited
    result = []

    def dfs(char):
        if char in visited:
            return visited[char] == 2  # False if cycle detected

        visited[char] = 1  # Mark as visiting
        for neighbor in graph[char]:
            if not dfs(neighbor):
                return False

        visited[char] = 2  # Mark as visited
        result.append(char)
        return True

    for char in in_degree:
        if char not in visited:
            if not dfs(char):
                return ""

    return ''.join(reversed(result))


if __name__ == "__main__":
    import unittest

    class TestAlienOrder(unittest.TestCase):
        def test_alien_order(self):
            self.assertEqual(alien_order(["w", "x", "w", "x", "w"]), "")

        def test_simple_order(self):
            self.assertEqual(alien_order(["w", "x"]), "wx")

        def test_positive_case(self):
            self.assertEqual(alien_order(["w", "x", "w", "x"]), "")

    # Demo
    print("Alien Dictionary: ['w', 'x', 'x', 'z']")
    print(f"Alien order: {alien_order(['w', 'x', 'x', 'z'])}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
