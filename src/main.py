#!/usr/bin/env python3
from calculator import Calculator, calculate_average, calculate_factorial
from utils.utils import is_prime, fibonacci, format_number, validate_number_range, find_max_min
from dotenv import load_dotenv
import os

def load_env():
    load_dotenv()
    print("env:" + os.getenv("SAMPLE_TOKEN"))

def main():
    print("=== Python Sample プログラム ===")
    print()
    
    # Calculatorクラスの使用例
    print("1. Calculatorクラスの使用例:")
    calc = Calculator()
    
    print(f"  2 + 3 = {calc.add(2, 3)}")
    print(f"  10 - 4 = {calc.subtract(10, 4)}")
    print(f"  5 * 6 = {calc.multiply(5, 6)}")
    print(f"  15 / 3 = {calc.divide(15, 3)}")
    
    print(f"  計算履歴: {calc.get_history()}")
    print()
    
    # 関数の使用例
    print("2. ユーティリティ関数の使用例:")
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"  数値リスト: {numbers}")
    print(f"  平均値: {calculate_average(numbers)}")
    
    max_val, min_val = find_max_min(numbers)
    print(f"  最大値: {max_val}, 最小値: {min_val}")
    
    print(f"  5の階乗: {calculate_factorial(5)}")
    print(f"  7は素数: {is_prime(7)}")
    print(f"  10番目のフィボナッチ数: {fibonacci(10)}")
    print(f"  3.14159を2桁でフォーマット: {format_number(3.14159)}")
    print(f"  5は0-10の範囲内: {validate_number_range(5, 0, 10)}")
    print()
    
    # エラーハンドリングの例
    print("3. エラーハンドリングの例:")
    try:
        calc.divide(10, 0)
    except ValueError as e:
        print(f"  エラー: {e}")
    
    try:
        calculate_factorial(-1)
    except ValueError as e:
        print(f"  エラー: {e}")
    
    try:
        calculate_average([])
    except ValueError as e:
        print(f"  エラー: {e}")
    
    print()
   
    load_env()

    print("=== プログラム終了 ===")


if __name__ == "__main__":
    main() 