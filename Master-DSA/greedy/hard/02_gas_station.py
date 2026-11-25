# 📘 Greedy Algorithms (Hard 02)
# Topic: Gas Station — Forward Greedy
# Approach: Track total gas and current gas, restart when negative
# Time: O(n) | Space: O(1)

def can_complete_circuit(gas, cost):
    """
    Find starting gas station index to complete circular route.
    Returns -1 if impossible.
    """
    total_gas = 0
    current_gas = 0
    start = 0

    for i in range(len(gas)):
        total_gas += gas[i] - cost[i]
        current_gas += gas[i] - cost[i]

        if current_gas < 0:
            # Can't reach station i+1 from start
            start = i + 1
            current_gas = 0

    return start if total_gas >= 0 else -1


def can_complete_circuit_brute(gas, cost):
    """
    Brute force: O(n²) time.
    Try starting from each station.
    """
    n = len(gas)

    for start in range(n):
        tank = 0
        possible = True

        for i in range(n):
            station = (start + i) % n
            tank += gas[station] - cost[station]
            if tank < 0:
                possible = False
                break

        if possible:
            return start

    return -1


if __name__ == "__main__":
    import unittest

    class TestGasStation(unittest.TestCase):
        def test_can_complete_circuit(self):
            self.assertEqual(can_complete_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), 3)
            self.assertEqual(can_complete_circuit([2, 3, 4], [3, 4, 3]), -1)
            self.assertEqual(can_complete_circuit([5, 1, 2, 3, 4], [4, 4, 1, 5, 1]), 4)

        def test_can_complete_circuit_brute(self):
            self.assertEqual(can_complete_circuit_brute([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), 3)
            self.assertEqual(can_complete_circuit_brute([2, 3, 4], [3, 4, 3]), -1)

    # Demo
    demo_gas = [1, 2, 3, 4, 5]
    demo_cost = [3, 4, 5, 1, 2]
    print(f"Gas: {demo_gas}")
    print(f"Cost: {demo_cost}")
    print(f"Starting station: {can_complete_circuit(demo_gas, demo_cost)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)