import unittest
from my_solution import solution


class TestSolution(unittest.TestCase):

    def test_tip(self):
        tip = int
        self.assertEqual(tip(1), int, "Should be Int Type!")
    
    def test_total_bill(self):
        total_bill = float
        self.assertEqual(total_bill(2.52), float, "Should be Float Type!")


if __name__ == '__main__':
    unittest.main()
