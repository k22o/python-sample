# Python Sample プロジェクト

以下を内包したPythonのサンプルレポジトリ

- モジュール化
- テストコード
- uv
- 環境変数の利用 (dotenv)
- 型定義



## 起動方法

``` shell
uv run python3 src/main.py
```

<details>
  <summary>venvを使った旧手順</summary>

    ``` shell
    python3 -m venv .venv # すでに作成済みなら不要
    source .venv/bin/activate
    pip3 install -r requirements.txt
    ```

</details>

## テストの実行

```bash
#全テストの実行
python3 -m unittest discover test 

# 特定のテストファイルの実行
python3 -m unittest test.utils.test_utils

# 個別のテストクラスの実行
python3 -m unittest test.test_calculator.TestCalculator
```

## 備考

作成時の設定

公式サイトの手順でuvをinstall

```
uv init 
uv add dotenv
```
