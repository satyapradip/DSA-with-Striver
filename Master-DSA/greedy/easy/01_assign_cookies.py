# 📘 Greedy Algorithms (Easy 01)
# Topic: Activity Selection — Assign Cookies
# Approach: Sort both arrays, match greedily
# Time: O(n log n) | Space: O(1)

def find_content_children(g, s):
    """
    Assign cookies to children to maximize satisfied children.
    Each child i has greed factor g[i], each cookie j has size s[j].
    Child i is satisfied if s[j] >= g[i].
    """
    g.sort()
    s.sort()

    child_i = 0
    cookie_j = 0

    while child_i < len(g) and cookie_j < len(s):
        if s[cookie_j] >= g[child_i]:
            # Cookie satisfies child
            child_i += 1
        cookie_j += 1

    return child_i


def find_content_children_brute(g, s):
    """
    Brute force: O(n*m) time.
    Try all possible assignments.
    """
    satisfied = [False] * len(g)
    used = [False] * len(s)
    count = 0

    for i in range(len(g)):
        for j in range(len(s)):
            if not used[j] and s[j] >= g[i]:
                satisfied[i] = True
                used[j] = True
                count += 1
                break

    return count


if __name__ == "__main__":
    import unittest

    class TestAssignCookies(unittest.TestCase):
        def test_assign_cookies(self):
            self.assertEqual(find_content_children([1, 2, 3], [1, 1]), 1)
            self.assertEqual(find_content_children([1, 2], [1, 2, 3]), 2)
            self.assertEqual(find_content_children([10, 9, 8, 7], [5, 6, 7, 8]), 2)
            self.assertEqual(find_content_children([], [1, 2, 3]), 0)
            self.assertEqual(find_content_children([1, 2, 3], []), 0)

        def test_assign_cookies_brute(self):
            self.assertEqual(find_content_children_brute([1, 2, 3], [1, 1]), 1)
            self.assertEqual(find_content_children_brute([1, 2], [1, 2, 3]), 2)

    # Demo
    demo_g = [1, 2, 3]
    demo_s = [1, 1]
    print(f"Greed factors: {demo_g}")
    print(f"Cookie sizes: {demo_s}")
    print(f"Content children: {find_content_children(demo_g, demo_s)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)