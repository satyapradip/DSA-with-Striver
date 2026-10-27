# 📘 Advanced Hashing — Hard 02
# Topic: Frequency Map + Bucket Sort — Top K Frequent Words
# Approach: Frequency map + bucket sort (O(n) time)
# Space: O(n)

from collections import Counter

def top_k_frequent_words(words, k):
    """
    Returns the k most frequent words (sorted by frequency, then alphabetically).
    """
    freq = Counter(words)

    # Bucket sort: index = frequency, value = list of words
    buckets = [[] for _ in range(len(words) + 1)]
    for word, count in freq.items():
        buckets[count].append(word)

    # Collect from highest frequency down
    result = []
    for i in range(len(buckets) - 1, 0, -1):
        for word in sorted(buckets[i]):  # alphabetical within same frequency
            result.append(word)
            if len(result) == k:
                return result
    return result


def top_k_frequent_words_heap(words, k):
    """
    Alternative: Counter + heap — O(n log k) time.
    """
    import heapq
    from collections import Counter

    freq = Counter(words)
    heap = [(-count, word) for word, count in freq.items()]
    heapq.heapify(heap)

    result = []
    for _ in range(k):
        count, word = heapq.heappop(heap)
        result.append(word)
    return result


def top_k_frequent_words_sort(words, k):
    """
    Sort approach — O(n log n) time.
    """
    freq = Counter(words)
    return [word for word, _ in sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:k]]


def top_k_frequent_words_brute(words, k):
    """
    Brute force: O(n²) — repeated counting.
    """
    result = []
    remaining = words[:]
    while len(result) < k:
        max_count = 0
        max_word = None
        for word in remaining:
            count = remaining.count(word)
            if count > max_count:
                max_count = count
                max_word = word
        result.append(max_word)
        remaining = [w for w in remaining if w != max_word]
    return result


if __name__ == "__main__":
    import unittest

    class TestTopKFrequentWords(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(top_k_frequent_words(["i", "love", "leetcode", "i", "love", "coding"], 2),
                             ["i", "love"])

        def test_sorted(self):
            self.assertEqual(top_k_frequent_words(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4),
                             ["the", "is", "sunny", "day"])

        def test_tie_breaker(self):
            self.assertEqual(top_k_frequent_words(["a", "aa", "a", "a", "aa", "aaa"], 2),
                             ["a", "aa"])

    # Demo
    demo_words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    print(f"Input: {demo_words}, k = {k}")
    print(f"Top {k}: {top_k_frequent_words(demo_words, k)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
