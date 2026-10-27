# 📘 Advanced Hashing — Medium 04
# Topic: Frequency Map + Heap — Top K Frequent Elements
# Approach: Frequency map + min-heap
# Time: O(n log k) | Space: O(n)

from collections import Counter
import heapq

def top_k_frequent(nums, k):
    """
    Returns the k most frequent elements.
    Uses Counter + min-heap (keeps only k elements).
    """
    freq = Counter(nums)
    heap = []
    for num, count in freq.items():
        heapq.heappush(heap, (count, num))
        if len(heap) > k:
            heapq.heappop(heap)
    return [num for count, num in heap]


def top_k_frequent_sort(nums, k):
    """
    Sort approach — O(n log n) time.
    """
    freq = Counter(nums)
    return [num for num, _ in sorted(freq.items(), key=lambda x: -x[1])[:k]]


def top_k_frequent_bucket(nums, k):
    """
    Bucket sort approach — O(n) time, O(n) space.
    Group elements by frequency.
    """
    freq = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, count in freq.items():
        buckets[count].append(num)

    result = []
    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result
    return result


if __name__ == "__main__":
    import unittest

    class TestTopKFrequent(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)), [1, 2])

        def test_sorted(self):
            self.assertEqual(sorted(top_k_frequent([1], 1)), [1])

        def test_three_most(self):
            self.assertEqual(sorted(top_k_frequent([1, 2], 2)), [1, 2])

    # Demo
    demo_nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(f"Input: {demo_nums}, k = {k}")
    print(f"Top {k} frequent: {top_k_frequent(demo_nums, k)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
