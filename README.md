# Python Sample プロジェクト

このプロジェクトは、モジュール化とテストコードを備えたPythonサンプルレポジトリです。

## 機能

## 使用方法

### メインプログラムの実行

```bash
python main.py
```

## テストの実行

### 全テストの実行

```bash
python -m unittest discover test
```

### 特定のテストファイルの実行

```bash
python -m unittest test.test_calculator
python -m unittest test.test_utils
```

### 個別のテストクラスの実行

```bash
python -m unittest test.test_calculator.TestCalculator
python -m unittest test.test_utils.TestIsPrime
```
