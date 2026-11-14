# 📘 Graphs (BFS/DFS) — Medium 03
# Topic: Topological Sort — Course Schedule
# Approach: Kahn's algorithm (BFS) on directed graph
# Time: O(V + E) | Space: O(V + E)

from collections import deque, defaultdict

def can_finish_courses(num_courses, prerequisites):
    """
    Returns True if all courses can be finished (i.e., there's no cycle).
    Prerequisites: [a, b] means course a depends on course b.
    """
    # Build adjacency list and in-degree array
    graph = defaultdict(list)
    in_degree = [0] * num_courses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    # Kahn's algorithm: start with courses that have no prerequisites
    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    count = 0

    while queue:
        course = queue.popleft()
        count += 1

        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If we processed all courses, there's no cycle
    return count == num_courses


def can_finish_courses_brute(num_courses, prerequisites):
    """
    Brute force: DFS cycle detection.
    """
    # Build graph
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)

    # Colors: 0 = unvisited, 1 = visiting, 2 = visited
    visited = [0] * num_courses

    def has_cycle(course):
        if visited[course] == 1:  # Currently visiting → cycle
            return True
        if visited[course] == 2:  # Already fully processed → no cycle
            return False

        visited[course] = 1  # Mark as visiting
        for neighbor in graph[course]:
            if has_cycle(neighbor):
                return True
        visited[course] = 2  # Mark as fully processed
        return False

    for course in range(num_courses):
        if has_cycle(course):
            return False

    return True


def can_finish_courses_brute2(num_courses, prerequisites):
    """
    Brute force: DFS with path tracking (more intuitive).
    """
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)

    visited = set()  # Nodes that are fully processed
    path = set()  # Nodes in current path

    def has_cycle(course):
        if course in path:
            return True  # Cycle found
        if course in visited:
            return False  # Already processed

        path.add(course)
        for neighbor in graph[course]:
            if has_cycle(neighbor):
                return True
        path.remove(course)
        visited.add(course)
        return False

    for course in range(num_courses):
        if has_cycle(course):
            return False

    return True


if __name__ == "__main__":
    import unittest

    class TestCourseSchedule(unittest.TestCase):
        def test_positive_cases(self):
            # No prerequisites → can finish
            self.assertTrue(can_finish_courses(1, []))

            # 1 depends on 0 → can finish
            self.assertTrue(can_finish_courses(2, [[1, 0]]))

            # 0 and 1 both depend on nothing
            self.assertTrue(can_finish_courses(2, []))

        def test_circular_dependency(self):
            # 1 -> 0, 0 -> 1 (cycle!)
            self.assertFalse(can_finish_courses(2, [[1, 0], [0, 1]]))

        def test_multiple_prereqs(self):
            # 3 courses, prerequisites: 1->0, 2->0, 2->1
            self.assertTrue(can_finish_courses(3, [[1, 0], [2, 0], [2, 1]]))

    # Demo
    print("Course Schedule: 2 courses, prerequisites: [[1, 0]]")
    print(f"Can finish? {can_finish_courses(2, [[1, 0]])}")
    print("Running unit tests...")
    unittest.main(verbosity=0)