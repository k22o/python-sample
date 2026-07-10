"""
デコレータ (Decorator) サンプル

デコレータは関数やクラスの振る舞いを変更・拡張するための構文糖衣。
@decorator 構文は func = decorator(func) と等価。
"""

import time
import functools
from typing import Callable, Any


# --- 1. 基本的なデコレータ ---

def simple_logger(func: Callable) -> Callable:
    """関数の呼び出しをログ出力するデコレータ"""
    @functools.wraps(func)  # func のメタ情報 (__name__ 等) を保持
    def wrapper(*args, **kwargs):
        print(f"[LOG] {func.__name__} を呼び出し")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} が終了、戻り値: {result}")
        return result
    return wrapper


@simple_logger
def add(a: int, b: int) -> int:
    return a + b


# --- 2. 引数を取るデコレータ (デコレータファクトリ) ---

def repeat(n: int) -> Callable:
    """関数を n 回繰り返すデコレータ"""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat(3)
def greet(name: str) -> str:
    print(f"Hello, {name}!")
    return f"Hello, {name}!"


# --- 3. 実行時間を計測するデコレータ ---

def timer(func: Callable) -> Callable:
    """関数の実行時間を計測するデコレータ"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[TIMER] {func.__name__}: {elapsed:.6f}s")
        return result
    return wrapper


@timer
def slow_sum(n: int) -> int:
    return sum(range(n))


# --- 4. キャッシュ (メモ化) デコレータ ---

def memoize(func: Callable) -> Callable:
    """計算結果をキャッシュするデコレータ"""
    cache: dict = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper


@memoize
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# --- 5. クラスベースのデコレータ ---

class Retry:
    """例外発生時にリトライするデコレータ"""

    def __init__(self, max_attempts: int = 3, exceptions: tuple = (Exception,)):
        self.max_attempts = max_attempts
        self.exceptions = exceptions

    def __call__(self, func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, self.max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except self.exceptions as e:
                    print(f"[RETRY] {attempt}/{self.max_attempts} 回目失敗: {e}")
                    if attempt == self.max_attempts:
                        raise
        return wrapper


@Retry(max_attempts=3, exceptions=(ValueError,))
def unstable_parse(value: str) -> int:
    result = int(value)
    if result < 0:
        raise ValueError(f"負の値は不正: {result}")
    return result


# --- 6. 複数デコレータの積み重ね ---
# デコレータは下から上の順に適用される (timer → simple_logger の順)

@simple_logger
@timer
def multiply(a: int, b: int) -> int:
    return a * b


# --- 動作確認 ---

if __name__ == "__main__":
    print("=== 1. 基本的なデコレータ ===")
    add(3, 4)

    print("\n=== 2. 引数付きデコレータ ===")
    greet("Alice")

    print("\n=== 3. 実行時間計測 ===")
    slow_sum(1_000_000)

    print("\n=== 4. メモ化 ===")
    print(fibonacci(10))
    print(fibonacci(10))  # キャッシュから返る

    print("\n=== 5. クラスベース (Retry) ===")
    try:
        unstable_parse("-5")
    except ValueError:
        print("最大リトライ回数に達しました")

    print("\n=== 6. 複数デコレータ ===")
    multiply(6, 7)
