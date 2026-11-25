# 📘 Greedy Algorithms (Hard 03)
# Topic: Candy — Two-Pass Greedy
# Approach: Left-to-right then right-to-left pass
# Time: O(n) | Space: O(n)

def candy(ratings):
    """
    Distribute candies to children based on ratings.
    Each child gets at least 1 candy. Children with higher rating
    than neighbors get more candies.
    """
    n = len(ratings)
    candies = [1] * n

    # Left to right: ensure increasing ratings get more candies
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # Right to left: ensure decreasing ratings get more candies
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)


def candy_brute(ratings):
    """
    Brute force: Try all possible distributions.
    """
    from itertools import product

    n = len(ratings)
    min_candies = float('inf')

    # Try all combinations up to n candies per child (reasonable bound)
    for candies in product(range(1, n + 1), repeat=n):
        valid = True
        for i in range(n):
            if i > 0 and ratings[i] > ratings[i - 1] and candies[i] <= candies[i - 1]:
                valid = False
                break
            if i < n - 1 and ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                valid = False
                break

        if valid:
            min_candies = min(min_candies, sum(candies))

    return min_candies


if __name__ == "__main__":
    import unittest

    class TestCandy(unittest.TestCase):
        def test_candy(self):
            self.assertEqual(candy([1, 0, 2]), 5)
            self.assertEqual(candy([1, 2, 2]), 4)
            self.assertEqual(candy([1]), 1)
            self.assertEqual(candy([1, 2, 3, 4, 5]), 15)
            self.assertEqual(candy([5, 4, 3, 2, 1]), 15)

        def test_candy_small(self):
            # Brute force only works for small arrays
            self.assertEqual(candy_brute([1, 0, 2]), 5)
            self.assertEqual(candy_brute([1, 2, 2]), 4)

    # Demo
    demo = [1, 0, 2]
    print(f"Ratings: {demo}")
    print(f"Minimum candies: {candy(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)