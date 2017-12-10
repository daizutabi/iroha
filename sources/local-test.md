# ローカルでのテスト

テストフレームワークは[pytest](https://docs.pytest.org/en/latest/)を使う．専用の環境を作成しよう．

```bash
> conda create -n pytest
> activate pytest
(pytest) > conda install python
(pytest) > conda install pytest
```

!!! Note
    `conda install pytest`のみだと，Python 3.5がインストールされてしまったので，pytestの前にpythonをインストールしている．

`iroha`のディレクトリ構造は以下のようになっていた．

```
+ iroha
    + iroha
        + add
        + data
        + sub
        - __init__.py
        - common.py
        - main.py
```

テストディレクトリ`tests`の配置方法は２つある．一つは，`iroha`パッケージのサブパッケージとする方法である．この場合，テストコードもパッケージ本体の中に含まれていて，`pip install`時に`iroha`パッケージとともに配布される．

```
+ iroha
    + iroha
        + add
        + data
        + sub
        + tests
            - __init__.py
            - test_add.py
        - __init__.py
        - common.py
        - main.py
```

もう一つは，`iroha`パッケージと並列に配置する方法である．この場合`tests`はパッケージではなく，テストスクリプトをまとめるフォルダである．テストコードはパッケージと一緒に配布されず，ローカルファイルやレポジトリ上だけで見ることができる．

```
+ iroha
    + iroha
        + add
        + data
        + sub
        - __init__.py
        - common.py
        - main.py
    + tests
        - test_add.py
```

!!! Note
    上記の方法には限られないと思うが，多くのパッケージで上記２つのうち一つを採用しているようである．

今回は後者の方法を用いる．２つのテストファイルを作成する．

```python
# iroha/tests/test_add.py
from iroha.add.calc import calc


def test_add_calc():
    assert calc(1, 2) == 3
```

```python
# iroha/tests/test_sub.py
from iroha.sub.calc import calc


def test_sub_calc():
    assert calc(1, 2) == -1
```

`iroha`パッケージを使えるようにするために，ローカルに「開発モード」でインストールする．`iroha`ディレクトリ下で以下を実行する．

```bash
(pytest) > pip install -e .
```

テストを実行しよう．

```bash
(pytest) > pytest
============================= test session starts =============================
platform win32 -- Python 3.6.3, pytest-3.3.0, py-1.5.2, pluggy-0.6.0
rootdir: c:\Users\daizu\Python\iroha, inifile:
plugins: hypothesis-3.38.5
collected 2 items

tests\test_add.py .                                                      [ 50%]
tests\test_sub.py .                                                      [100%]

========================== 2 passed in 0.10 seconds ===========================
```
