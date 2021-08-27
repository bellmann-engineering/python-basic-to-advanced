import unittest
from calc import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator      

    def test_sum(self):
        # ARRANGE
        summand1 = 2
        summand2 = 2
        expected =  4
        # ACT
        actual =  self.calculator.sum(summand1, summand2)
        # ASSERT       
        self.assertEqual(actual, expected)

        
    def test_sum_complex(self):
        # ARRANGE
        summand1 = -2
        summand2 = 2
        expected =  0
        # ACT
        actual = self.calculator.sum(summand1, summand2)
        # ASSERT       
        self.assertEqual(actual, expected)