# 📘 Greedy Algorithms (Medium 04)
# Topic: Partition Labels
# Approach: Record last occurrence, greedy partitioning
# Time: O(n) | Space: O(1)

def partition_labels(s):
    """
    Partition string into as many parts as possible so each letter appears
    in at most one part. Return sizes of parts.
    """
    # Record last occurrence of each character
    last = {char: i for i, char in enumerate(s)}

    result = []
    start = 0
    end = 0

    for i, char in enumerate(s):
        end = max(end, last[char])

        if i == end:
            # End of current partition
            result.append(end - start + 1)
            start = i + 1

    return result


def partition_labels_brute(s):
    """
    Brute force: O(n²) time.
    Check all possible partitions.
    """
    result = []
    i = 0

    while i < len(s):
        # Find the last occurrence of s[i]
        last = i
        for j in range(i + 1, len(s)):
            if s[j] == s[i]:
                last = j

        # Check if any character in [i, last] appears beyond last
        changed = True
        while changed:
            changed = False
            for j in range(i, last + 1):
                for k in range(last + 1, len(s)):
                    if s[j] == s[k]:
                        last = k
                        changed = True
                        break
                if changed:
                    break

        result.append(last - i + 1)
        i = last + 1

    return result


if __name__ == "__main__":
    import unittest

    class TestPartitionLabels(unittest.TestCase):
        def test_partition_labels(self):
            self.assertEqual(partition_labels("ababcbacadefegdehijhklij"), [9, 7, 8])
            self.assertEqual(partition_labels("eccbbbbdec"), [10])

        def test_partition_labels_brute(self):
            self.assertEqual(partition_labels_brute("ababcbacadefegdehijhklij"), [9, 7, 8])
            self.assertEqual(partition_labels_brute("eccbbbbdec"), [10])

    # Demo
    demo = "ababcbacadefegdehijhklij"
    print(f"String: {demo}")
    print(f"Partition sizes: {partition_labels(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)