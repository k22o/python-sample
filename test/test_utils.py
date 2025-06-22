"""
utilsモジュールのテストコード
"""
import unittest
import sys
import os

# srcディレクトリをパスに追加
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from utils import (
    is_prime,
    fibonacci,
    format_number,
    validate_number_range,
    find_max_min
)


class TestIsPrime(unittest.TestCase):
    """is_prime関数のテスト"""
    
    def test_prime_numbers(self):
        """素数のテスト"""
        prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        for num in prime_numbers:
            self.assertTrue(is_prime(num), f"{num}は素数であるべきです")
    
    def test_non_prime_numbers(self):
        """非素数のテスト"""
        non_prime_numbers = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]
        for num in non_prime_numbers:
            self.assertFalse(is_prime(num), f"{num}は素数ではないべきです")
    
    def test_negative_numbers(self):
        """負の数のテスト"""
        negative_numbers = [-1, -2, -3, -10]
        for num in negative_numbers:
            self.assertFalse(is_prime(num), f"{num}は素数ではないべきです")


class TestFibonacci(unittest.TestCase):
    """fibonacci関数のテスト"""
    
    def test_fibonacci_sequence(self):
        """フィボナッチ数列のテスト"""
        expected_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        for i, expected in enumerate(expected_sequence):
            self.assertEqual(fibonacci(i), expected, f"fibonacci({i}) = {expected}")
    
    def test_large_numbers(self):
        """大きな数のテスト"""
        self.assertEqual(fibonacci(20), 6765)
    
    def test_negative_numbers(self):
        """負の数のエラーテスト"""
        with self.assertRaises(ValueError):
            fibonacci(-1)
        
        with self.assertRaises(ValueError):
            fibonacci(-10)


class TestFormatNumber(unittest.TestCase):
    """format_number関数のテスト"""
    
    def test_integer_formatting(self):
        """整数のフォーマットテスト"""
        self.assertEqual(format_number(5), "5")
        self.assertEqual(format_number(0), "0")
        self.assertEqual(format_number(-10), "-10")
    
    def test_float_formatting(self):
        """浮動小数点数のフォーマットテスト"""
        self.assertEqual(format_number(3.14159), "3.14")
        self.assertEqual(format_number(2.5), "2.50")
        self.assertEqual(format_number(0.123), "0.12")
    
    def test_custom_decimal_places(self):
        """カスタム小数点以下の桁数テスト"""
        self.assertEqual(format_number(3.14159, 3), "3.142")
        self.assertEqual(format_number(2.5, 0), "2")
        self.assertEqual(format_number(0.123, 4), "0.1230")


class TestValidateNumberRange(unittest.TestCase):
    """validate_number_range関数のテスト"""
    
    def test_valid_ranges(self):
        """有効な範囲のテスト"""
        self.assertTrue(validate_number_range(5, 0, 10))
        self.assertTrue(validate_number_range(0, 0, 10))
        self.assertTrue(validate_number_range(10, 0, 10))
        self.assertTrue(validate_number_range(3.5, 0, 5))
    
    def test_invalid_ranges(self):
        """無効な範囲のテスト"""
        self.assertFalse(validate_number_range(-1, 0, 10))
        self.assertFalse(validate_number_range(11, 0, 10))
        self.assertFalse(validate_number_range(5, 10, 20))
    
    def test_edge_cases(self):
        """境界値のテスト"""
        self.assertTrue(validate_number_range(0, 0, 0))
        self.assertTrue(validate_number_range(5, 5, 5))
        self.assertFalse(validate_number_range(4, 5, 5))


class TestFindMaxMin(unittest.TestCase):
    """find_max_min関数のテスト"""
    
    def test_normal_lists(self):
        """通常のリストのテスト"""
        max_val, min_val = find_max_min([1, 2, 3, 4, 5])
        self.assertEqual(max_val, 5)
        self.assertEqual(min_val, 1)
        
        max_val, min_val = find_max_min([10, -5, 0, 100, -10])
        self.assertEqual(max_val, 100)
        self.assertEqual(min_val, -10)
    
    def test_float_lists(self):
        """浮動小数点数のリストのテスト"""
        max_val, min_val = find_max_min([1.5, 2.5, 0.5, 3.5])
        self.assertEqual(max_val, 3.5)
        self.assertEqual(min_val, 0.5)
    
    def test_single_element(self):
        """単一要素のテスト"""
        max_val, min_val = find_max_min([5])
        self.assertEqual(max_val, 5)
        self.assertEqual(min_val, 5)
    
    def test_duplicate_values(self):
        """重複値のテスト"""
        max_val, min_val = find_max_min([3, 3, 3, 3])
        self.assertEqual(max_val, 3)
        self.assertEqual(min_val, 3)
    
    def test_empty_list(self):
        """空リストのエラーテスト"""
        with self.assertRaises(ValueError):
            find_max_min([])


if __name__ == '__main__':
    unittest.main() 