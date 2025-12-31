"""
ユーティリティ機能を提供するモジュール

このモジュールは一般的なユーティリティ関数を提供します。
"""
import math
from typing import Union

def is_prime(n: int) -> bool:
    """
    数値が素数かどうかを判定します
    
    Args:
        n (int): 判定する数値
        
    Returns:
        bool: 素数の場合True、そうでない場合False
    """
    if n < 2:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    
    return True


def fibonacci(n: int) -> int:
    """
    フィボナッチ数列のn番目の値を計算します
    
    Args:
        n (int): 非負整数
        
    Returns:
        int: フィボナッチ数列のn番目の値
        
    Raises:
        ValueError: 負の整数が指定された場合
    """
    if n < 0:
        raise ValueError("負の整数のフィボナッチ数は定義されていません")
    
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b


def format_number(number: Union[int, float], decimal_places: int = 2) -> str:
    """
    数値を指定された小数点以下の桁数でフォーマットします
    
    Args:
        number (Union[int, float]): フォーマットする数値
        decimal_places (int): 小数点以下の桁数
        
    Returns:
        str: フォーマットされた文字列
    """
    if isinstance(number, int):
        return str(number)
    
    return f"{number:.{decimal_places}f}"


def validate_number_range(value: float, min_val: float, max_val: float) -> bool:
    """
    数値が指定された範囲内にあるかを検証します
    
    Args:
        value (float): 検証する数値
        min_val (float): 最小値
        max_val (float): 最大値
        
    Returns:
        bool: 範囲内の場合True、そうでない場合False
    """
    return min_val <= value <= max_val


def find_max_min(numbers: list[float]) -> tuple:
    """
    数値のリストから最大値と最小値を取得します
    
    Args:
        numbers (List[float]): 数値のリスト
        
    Returns:
        tuple: (最大値, 最小値)のタプル
        
    Raises:
        ValueError: リストが空の場合
    """
    if not numbers:
        raise ValueError("リストは空にできません")
    
    return max(numbers), min(numbers) 