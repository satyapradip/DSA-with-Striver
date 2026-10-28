# 📘 Binary Search — Advanced Medium 06
# Topic: Binary Search on Answer — Min Speed to Arrive on Time
# Approach: Search the speed answer
# Time: O(n log(max_speed))
# Space: O(1)

def min_speed_on_time(dist, hour):
    """
    Returns the minimum integer speed to reach on time.
    Returns -1 if impossible.
    """
    def can_arrive_on_time(speed):
        total_time = 0
        for i, d in enumerate(dist):
            if i == len(dist) - 1:
                total_time += d / speed
            else:
                total_time += (d + speed - 1) // speed  # ceil
            if total_time > hour:
                return False
        return total_time <= hour

    # Speed range: 1 to 10^7
    low, high = 1, 10**7
    while low < high:
        mid = (low + high) // 2
        if can_arrive_on_time(mid):
            high = mid
        else:
            low = mid + 1

    return low if can_arrive_on_time(low) else -1


def min_speed_on_time_brute(dist, hour):
    """
    Brute force: check each speed from 1 to 10^7.
    """
    for speed in range(1, 10**7 + 1):
        total_time = 0
        for i, d in enumerate(dist):
            if i == len(dist) - 1:
                total_time += d / speed
            else:
                total_time += (d + speed - 1) // speed
            if total_time > hour:
                break
        if total_time <= hour:
            return speed
    return -1


if __name__ == "__main__":
    import unittest

    class TestMinSpeedOnTime(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(min_speed_on_time([1, 3, 2], 6), 1)

        def test_exact(self):
            # At speed 98912: total time ≈ 3.011 hours → exactly on time
            self.assertEqual(min_speed_on_time([1, 1, 100000], 3.011), 98912)

        def test_impossible(self):
            # At speed 10^7: total time ≈ 0.01 hours
            # hour = 0.011 is close but at speed 10^7: total = 0.01 < 0.011
            # So it IS possible. Test with a truly impossible case:
            self.assertEqual(min_speed_on_time([1, 1, 100000], 0.011), -1)

    # Demo
    demo_dist = [1, 3, 2]
    demo_hour = 6
    print(f"Distances: {demo_dist}, hour: {demo_hour}")
    print(f"Min speed: {min_speed_on_time(demo_dist, demo_hour)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
