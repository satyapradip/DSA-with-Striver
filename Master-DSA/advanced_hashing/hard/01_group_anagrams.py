# 📘 Advanced Hashing — Hard 01
# Topic: Frequency Grouping — Group Anagrams
# Approach: Sort each string to create a unique key, then group by key
# Time: O(n * m log m) where n = len(strs), m = max(len(word))
# Space: O(n * m)

from collections import defaultdict

def group_anagrams(strs):
    """
    Groups strings that are anagrams of each other.
    """
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)
    return list(groups.values())


def group_anagrams_prime_hash(strs):
    """
    More advanced: use prime number multiplication as hash key.
    Each letter maps to a unique prime; anagram products are equal.
    """
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
              53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    groups = defaultdict(list)
    for s in strs:
        key = 1
        for ch in s:
            key *= primes[ord(ch) - ord('a')]
        groups[key].append(s)
    return list(groups.values())


def group_anagrams_brute(strs):
    """
    Brute force: O(n² * m) — compare all pairs.
    """
    n = len(strs)
    result = []
    used = [False] * n

    for i in range(n):
        if used[i]:
            continue
        group = [strs[i]]
        used[i] = True
        for j in range(i + 1, n):
            if not used[j] and sorted(strs[j]) == sorted(strs[i]):
                group.append(strs[j])
                used[j] = True
        result.append(group)

    return result


def _normalize_groups(groups):
    """Normalize groups for comparison: sort each group, then sort groups."""
    normalized = []
    for group in groups:
        normalized.append(sorted(group))
    return sorted(normalized)


if __name__ == "__main__":
    import unittest

    class TestGroupAnagrams(unittest.TestCase):
        def test_basic(self):
            # Order of groups and order within groups doesn't matter
            result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
            self.assertEqual(_normalize_groups(result),
                             _normalize_groups([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]))

        def test_single(self):
            self.assertEqual(group_anagrams(["a"]), [["a"]])

        def test_empty(self):
            self.assertEqual(group_anagrams([]), [])

    # Demo
    demo = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f"Input: {demo}")
    print(f"Grouped anagrams: {group_anagrams(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
