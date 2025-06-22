"""
Python Sample Package

このパッケージは計算機能とユーティリティ機能を提供します。
"""

from .calculator import Calculator, calculate_average, calculate_factorial
from .utils import (
    is_prime,
    fibonacci,
    format_number,
    validate_number_range,
    find_max_min
)

__version__ = "1.0.0"
__author__ = "Python Sample"

__all__ = [
    "Calculator",
    "calculate_average",
    "calculate_factorial",
    "is_prime",
    "fibonacci",
    "format_number",
    "validate_number_range",
    "find_max_min"
] 