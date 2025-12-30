# Python Sample プロジェクト

以下を内包したPythonのサンプルレポジトリ

- モジュール化
- テストコード
- venv

## 起動方法

``` shell
python3 -m venv .venv # すでに作成済みなら不要
source .venv/bin/activate
pip3 install -r requirements.txt
```

## テストの実行

```bash
#全テストの実行
python3 -m unittest discover test 

# 特定のテストファイルの実行
python3 -m unittest test.test_utils

# 個別のテストクラスの実行
python3 -m unittest test.test_calculator.TestCalculator
```