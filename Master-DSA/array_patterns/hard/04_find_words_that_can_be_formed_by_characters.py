# 📘 Array Patterns — Hard 04
# Topic: Hashing — Words That Can Be Formed by Characters
# Approach: Frequency map comparison
# Time: O(N * L) where N = number of words, L = avg word length
# Space: O(1) (26-letter alphabet)

def count_characters(words, chars):
    """
    Returns the sum of lengths of all words that can be formed
    using characters from chars (each character used once).
    """
    char_count = [0] * 26
    for ch in chars:
        char_count[ord(ch) - ord('a')] += 1

    total_length = 0
    for word in words:
        word_count = [0] * 26
        for ch in word:
            word_count[ord(ch) - ord('a')] += 1

        # Check if word can be formed
        can_form = True
        for i in range(26):
            if word_count[i] > char_count[i]:
                can_form = False
                break

        if can_form:
            total_length += len(word)

    return total_length


def count_characters_set(words, chars):
    """
    Alternative: using Counter (more readable).
    """
    from collections import Counter
    char_count = Counter(chars)
    total_length = 0
    for word in words:
        word_count = Counter(word)
        if all(word_count[c] <= char_count[c] for c in word_count):
            total_length += len(word)
    return total_length


if __name__ == "__main__":
    import unittest

    class TestCountCharacters(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(count_characters(["cat", "bt", "hat", "tree"], "atach"),
                             6)  # "cat"(3) + "hat"(3) = 6

        def test_no_match(self):
            self.assertEqual(count_characters(["hello", "world"], "abc"),
                             0)

    # Demo
    demo_words = ["cat", "bt", "hat", "tree"]
    demo_chars = "atach"
    print(f"Words: {demo_words}, chars: {demo_chars}")
    print(f"Total length: {count_characters(demo_words, demo_chars)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
