"""
計算機能を提供するモジュール

このモジュールは基本的な数学演算を提供します。
"""


class Calculator:
    """基本的な計算機能を提供するクラス"""
    
    def __init__(self):
        """Calculatorクラスの初期化"""
        self.history = []
    
    def add(self, a: float, b: float) -> float:
        """
        2つの数値を加算します
        
        Args:
            a (float): 第1の数値
            b (float): 第2の数値
            
        Returns:
            float: 加算結果
        """
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a: float, b: float) -> float:
        """
        2つの数値を減算します
        
        Args:
            a (float): 被減数
            b (float): 減数
            
        Returns:
            float: 減算結果
        """
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a: float, b: float) -> float:
        """
        2つの数値を乗算します
        
        Args:
            a (float): 第1の数値
            b (float): 第2の数値
            
        Returns:
            float: 乗算結果
        """
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a: float, b: float) -> float:
        """
        2つの数値を除算します
        
        Args:
            a (float): 被除数
            b (float): 除数
            
        Returns:
            float: 除算結果
            
        Raises:
            ValueError: 除数が0の場合
        """
        if b == 0:
            raise ValueError("除数は0にできません")
        
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def get_history(self) -> list:
        """
        計算履歴を取得します
        
        Returns:
            list: 計算履歴のリスト
        """
        return self.history.copy()
    
    def clear_history(self):
        """計算履歴をクリアします"""
        self.history.clear()


def calculate_average(numbers: list) -> float:
    """
    数値のリストの平均値を計算します
    
    Args:
        numbers (list): 数値のリスト
        
    Returns:
        float: 平均値
        
    Raises:
        ValueError: リストが空の場合
    """
    if not numbers:
        raise ValueError("リストは空にできません")
    
    return sum(numbers) / len(numbers)


def calculate_factorial(n: int) -> int:
    """
    階乗を計算します
    
    Args:
        n (int): 非負整数
        
    Returns:
        int: 階乗の結果
        
    Raises:
        ValueError: 負の整数が指定された場合
    """
    if n < 0:
        raise ValueError("負の整数の階乗は定義されていません")
    
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result 