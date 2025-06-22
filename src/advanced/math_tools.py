"""
高度な数学ツール
"""
import math

def power(a: float, b: float) -> float:
    """
    aのb乗を計算します
    """
    return math.pow(a, b)

def sqrt(x: float) -> float:
    """
    平方根を計算します
    """
    if x < 0:
        raise ValueError("負の数の平方根は定義されていません")
    return math.sqrt(x) 