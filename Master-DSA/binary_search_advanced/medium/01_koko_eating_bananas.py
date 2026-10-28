# 📘 Binary Search — Advanced Medium 01
# Topic: Binary Search on Answer — Koko Eating Bananas
# Approach: Search the answer space (min eating speed)
# Time: O(n log M) where n=len(piles), M=max(piles)
# Space: O(1)

def min_eating_speed(piles, h):
    """
    Returns the minimum integer k such that Koko can eat all bananas
    within h hours. Each hour, Koko eats k bananas from a pile.
    """
    def can_finish(speed):
        hours = 0
        for pile in piles:
            hours += (pile + speed - 1) // speed  # ceil division
            if hours > h:
                return False
        return True

    low, high = 1, max(piles)
    while low < high:
        mid = (low + high) // 2
        if can_finish(mid):
            high = mid
        else:
            low = mid + 1
    return low


def min_eating_speed_brute(piles, h):
    """
    Brute force: check every speed from 1 to max(piles).
    """
    for speed in range(1, max(piles) + 1):
        hours = 0
        for pile in piles:
            hours += (pile + speed - 1) // speed
        if hours <= h:
            return speed
    return max(piles)


if __name__ == "__main__":
    import unittest

    class TestMinEatingSpeed(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(min_eating_speed([3, 6, 7, 11], 8), 4)

        def test_single_pile(self):
            self.assertEqual(min_eating_speed([30, 11, 23, 4, 20], 5), 30)

        def test_small(self):
            self.assertEqual(min_eating_speed([1, 1, 1], 3), 1)

    # Demo
    demo_piles = [3, 6, 7, 11]
    demo_h = 8
    print(f"Piles: {demo_piles}, Hours: {demo_h}")
    print(f"Min eating speed: {min_eating_speed(demo_piles, demo_h)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
