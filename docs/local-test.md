# ローカルでのテスト

テストフレームワークは[pytest](https://docs.pytest.org/en/latest/)を使います．専用の環境を作成しましょう．

```bash
> conda create -n pytest
> activate pytest
(pytest) > conda install python
(pytest) > conda install pytest
```

!!! Note
    `conda install pytest`のみだと，Python 3.5がインストールされてしまったので，pytestの前にpythonをインストールしています．

テストスクリプトは`tests`ディレクトリの中に入れていきます．`tests`ディレクトリ自体の配置方法は２つあります．一つは，`takuhai`パッケージのサブパッケージとする方法です．この場合には，テストスクリプトもパッケージ本体の中に含まれていて，`pip install`時に`takuhai`パッケージとともに配布されます．もう一つは，`takuhai`パッケージと並列に配置する方法です．この場合には，`tests`はパッケージではなく，テストスクリプトをまとめるディレクトリになります．テストスクリプトはパッケージと一緒に配布されません．

`takuhai`プロジェクトは，後者の方法を採用しています．pytestが`takuhai`パッケージを使えるようにするために，ローカルに「開発モード」でインストールします．`setup.py`があるディレクトリ下で以下を実行します．

```bash
(pytest) > pip install -e .
```

テストを実行しましょう．

```bash
(pytest) > pytest
============================= test session starts =============================
platform win32 -- Python 3.6.3, pytest-3.3.0, py-1.5.2, pluggy-0.6.0
rootdir: C:\Users\daizu\Documents\GitHub\takuhai, inifile:
plugins: hypothesis-3.38.5
collected 9 items

tests\test_convert.py .........                                          [100%]

========================== 9 passed in 0.17 seconds ===========================
```

テストにパスしたことが分かります．
