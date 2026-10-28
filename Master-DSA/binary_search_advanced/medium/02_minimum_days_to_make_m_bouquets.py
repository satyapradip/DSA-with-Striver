# 📘 Binary Search — Advanced Medium 02
# Topic: Binary Search on Answer — Min Days to Make M Bouquets
# Approach: Search the day space, check feasibility
# Time: O(n log(max_day)) where n=len(blooms)
# Space: O(1)

def min_days_to_make_bouquets(bloom_day, m, k):
    """
    Returns the minimum day needed to make m bouquets.
    Each bouquet needs k adjacent flowers that have bloomed.
    Returns -1 if impossible.
    """
    if m * k > len(bloom_day):
        return -1

    def can_make_bouquets(day):
        bouquets = 0
        consecutive = 0
        for bd in bloom_day:
            if bd <= day:
                consecutive += 1
                if consecutive == k:
                    bouquets += 1
                    consecutive = 0
            else:
                consecutive = 0
            if bouquets >= m:
                return True
        return False

    low, high = 1, max(bloom_day)
    while low < high:
        mid = (low + high) // 2
        if can_make_bouquets(mid):
            high = mid
        else:
            low = mid + 1
    return low


def min_days_to_make_bouquets_brute(bloom_day, m, k):
    """
    Brute force: simulate each day from 1 to max(bloom_day).
    """
    max_day = max(bloom_day)
    for day in range(1, max_day + 1):
        bouquets = 0
        consecutive = 0
        for bd in bloom_day:
            if bd <= day:
                consecutive += 1
                if consecutive == k:
                    bouquets += 1
                    consecutive = 0
            else:
                consecutive = 0
            if bouquets >= m:
                return day
    return -1


if __name__ == "__main__":
    import unittest

    class TestMinDaysToMakeBouquets(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(min_days_to_make_bouquets([1, 10, 3, 10, 2], 3, 1), 3)

        def test_multiple_per_flower(self):
            self.assertEqual(min_days_to_make_bouquets([1, 10, 3, 10, 2], 3, 1), 3)

        def test_impossible(self):
            self.assertEqual(min_days_to_make_bouquets([1, 10, 3, 10, 2], 4, 2), -1)

    # Demo
    demo_bloom = [1, 10, 3, 10, 2]
    demo_m = 3
    demo_k = 1
    print(f"Bloom days: {demo_bloom}, m = {demo_m}, k = {demo_k}")
    print(f"Min day: {min_days_to_make_bouquets(demo_bloom, demo_m, demo_k)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
