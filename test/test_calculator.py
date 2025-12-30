import unittest
from src.calculator import Calculator, calculate_average, calculate_factorial

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculator()
    
    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(3.5, 2.5), 6.0)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(1, 1), 0)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(3.5, 1.5), 2.0)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertEqual(self.calc.divide(-6, 2), -3)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)
    
    def test_history(self):
        self.calc.add(2, 3)
        self.calc.subtract(5, 2)
        self.calc.multiply(3, 4)
        
        history = self.calc.get_history()
        self.assertEqual(len(history), 3)
        self.assertIn("2 + 3 = 5", history)
        self.assertIn("5 - 2 = 3", history)
        self.assertIn("3 * 4 = 12", history)
    
    def test_clear_history(self):
        self.calc.add(2, 3)
        self.calc.clear_history()
        self.assertEqual(len(self.calc.get_history()), 0)


class TestCalculateAverage(unittest.TestCase):
    
    def test_normal_average(self):
        self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(calculate_average([10, 20, 30]), 20.0)
        self.assertEqual(calculate_average([1.5, 2.5, 3.5]), 2.5)
    
    def test_single_element(self):
        self.assertEqual(calculate_average([5]), 5.0)
    
    def test_empty_list(self):
        with self.assertRaises(ValueError):
            calculate_average([])


class TestCalculateFactorial(unittest.TestCase):
    
    def test_normal_factorial(self):
        self.assertEqual(calculate_factorial(0), 1)
        self.assertEqual(calculate_factorial(1), 1)
        self.assertEqual(calculate_factorial(5), 120)
        self.assertEqual(calculate_factorial(10), 3628800)
    
    def test_negative_number(self):
        with self.assertRaises(ValueError):
            calculate_factorial(-1)


if __name__ == '__main__':
    unittest.main() 