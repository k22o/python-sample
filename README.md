# Python Sample プロジェクト

以下を内包したPythonのサンプルレポジトリ

- モジュール化
- テストコード
- venv
- 環境変数の利用 (dotenv)
- 型定義

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
python3 -m unittest test.utils.test_utils

# 個別のテストクラスの実行
python3 -m unittest test.test_calculator.TestCalculator
```
