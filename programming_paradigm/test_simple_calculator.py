import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Create a calculator instance before each test."""
        self.calc = SimpleCalculator()

    # Tests for Addition
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -5), -10)
        self.assertEqual(self.calc.add(0, 100), 100)
        self.assertEqual(self.calc.add(2.5, 7.5), 10.0)

    
    # Tests for Subtraction
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(0, 10), -10)
        self.assertEqual(self.calc.subtract(-5, -5), 0)
        self.assertEqual(self.calc.subtract(10.5, 0.5), 10.0)

    
    # Tests for Multiplication
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-4, 5), -20)
        self.assertEqual(self.calc.multiply(-3, -3), 9)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)

  
    # Tests for Division

    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(9, 3), 3.0)
        self.assertEqual(self.calc.divide(-9, 3), -3.0)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(0, 0))  # Even 0/0 should return None

if __name__ == "__main__":
    unittest.main()
