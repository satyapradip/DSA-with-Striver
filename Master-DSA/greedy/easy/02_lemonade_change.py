# 📘 Greedy Algorithms (Easy 02)
# Topic: Fractional Knapsack — Lemonade Change
# Approach: Greedy with coin counting
# Time: O(n) | Space: O(1)

def lemonade_change(bills):
    """
    Determine if we can provide change to all customers.
    Each lemonade costs $5. Customers pay with $5, $10, or $20.
    """
    five = 0
    ten = 0

    for bill in bills:
        if bill == 5:
            five += 1
        elif bill == 10:
            if five > 0:
                five -= 1
                ten += 1
            else:
                return False
        elif bill == 20:
            # Prefer giving one $10 + one $5 (save $5 bills)
            if ten > 0 and five > 0:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False

    return True


def lemonade_change_brute(bills):
    """
    Brute force: Try all combinations of giving change.
    """
    from collections import Counter

    def can_give_change(idx, five, ten):
        if idx == len(bills):
            return True

        bill = bills[idx]

        if bill == 5:
            return can_give_change(idx + 1, five + 1, ten)
        elif bill == 10:
            if five > 0 and can_give_change(idx + 1, five - 1, ten + 1):
                return True
            return False
        elif bill == 20:
            # Try one $10 + one $5
            if ten > 0 and five > 0 and can_give_change(idx + 1, five - 1, ten - 1):
                return True
            # Try three $5
            if five >= 3 and can_give_change(idx + 1, five - 3, ten):
                return True
            return False

    return can_give_change(0, 0, 0)


if __name__ == "__main__":
    import unittest

    class TestLemonadeChange(unittest.TestCase):
        def test_lemonade_change(self):
            self.assertTrue(lemonade_change([5, 5, 5, 10, 20]))
            self.assertFalse(lemonade_change([5, 5, 10, 10, 20]))
            self.assertTrue(lemonade_change([5, 5, 10]))
            self.assertFalse(lemonade_change([10, 10]))  # Can't give change for first $10
            self.assertFalse(lemonade_change([20]))  # Can't give change for $20 with no bills

        def test_lemonade_change_brute(self):
            self.assertTrue(lemonade_change_brute([5, 5, 5, 10, 20]))
            self.assertFalse(lemonade_change_brute([5, 5, 10, 10, 20]))

    # Demo
    demo = [5, 5, 5, 10, 20]
    print(f"Bills: {demo}")
    print(f"Can provide change? {lemonade_change(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)