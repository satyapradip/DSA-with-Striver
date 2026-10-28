# 📘 Binary Search — Advanced Medium 05
# Topic: Binary Search on Answer — Ship Packages
# Approach: Search the ship capacity answer
# Time: O(n log(max_weight))
# Space: O(1)

def ship_packages(weights, days):
    """
    Returns the minimum ship capacity to ship all packages within days days.
    """
    def can_ship(capacity):
        days_needed = 1
        current_weight = 0
        for w in weights:
            if current_weight + w > capacity:
                days_needed += 1
                current_weight = w
                if days_needed > days:
                    return False
            else:
                current_weight += w
        return True

    low, high = max(weights), sum(weights)
    while low < high:
        mid = (low + high) // 2
        if can_ship(mid):
            high = mid
        else:
            low = mid + 1
    return low


def ship_packages_brute(weights, days):
    """
    Brute force: check each possible capacity from max(weights) to sum(weights).
    """
    for capacity in range(max(weights), sum(weights) + 1):
        days_needed = 1
        current_weight = 0
        for w in weights:
            if current_weight + w > capacity:
                days_needed += 1
                current_weight = w
                if days_needed > days:
                    break
            else:
                current_weight += w
        if days_needed <= days:
            return capacity
    return -1


if __name__ == "__main__":
    import unittest

    class TestShipPackages(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(ship_packages([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), 15)

        def test_single_day(self):
            self.assertEqual(ship_packages([3, 2, 2, 4, 1, 4], 3), 6)

        def test_single_package(self):
            self.assertEqual(ship_packages([1, 2, 3, 1, 1], 4), 3)

    # Demo
    demo_weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    demo_days = 5
    print(f"Package weights: {demo_weights}, days: {demo_days}")
    print(f"Min ship capacity: {ship_packages(demo_weights, demo_days)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
