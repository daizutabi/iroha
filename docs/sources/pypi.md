# PyPIへのアップロード


## ディストリビューションの作成

プロジェクトを[PyPI](https://pypi.python.org/pypi)に公開するために，プロジェクトのディストリビューションを作る．

### ソースディストリビューション

ソースディストリビューションを作成する．`irohapj`ディレクトリ下で以下を実行する．

```bash
(irohaenv) > python setup.py sdist
```

`dist`ディレクトリが新しく作られて，その中に`iroha-0.1.0.tar.gz`が格納された．

### Wheels

ビルドされたwheelを作成する．`irohapj`ディレクトリ下で以下を実行する．

```bash
(irohaenv) > python setup.py bdist_wheel
```

`build`ディレクトリが新しく作られて，いろいろなファイルが生成された．wheel自体は，`dist`下に`iroha-0.1.0-py3-none-any.whl`の名前で格納された．

## アップロード

### アカウントの作成

プロジェクトを[PyPI](https://pypi.python.org/pypi)にアップロードするためには事前にユーザーアカウントを作成しておく必要がある．テスト用の[Test PyPI](https://testpypi.python.org/pypi)にアップロードする場合は，別途ユーザーアカウントが必要である．それぞれの登録フォームは以下である．

* [PyPIのユーザ登録](https://pypi.python.org/pypi?%3Aaction=register_form)
* [Test PyPIのユーザ登録](https://testpypi.python.org/pypi?%3Aaction=register_form)

ユーザー登録が終わったら，`~/.pypirc`を用意し，以下のように書く．

```
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
repository: https://upload.pypi.org/legacy/
username: <username>
password: <password>

[testpypi]
repository: https://test.pypi.org/legacy/
username: <username>
password: <password>
```

`username`行および`password`行は省略してもよい。`twine`に`-u USERNAME`引数，`-p PASSWORD`引数を渡すか、単に要求されたときに入力すればよい．


!!! Note
    pypiのrepository行は省略可能である．

### アップロード

アップロードするには[twine](https://github.com/pypa/twine)を使う．twineは他のプロジェクトでも使うので，専用の環境`twine`下にインストールする．こうすることで，`iroha`プロジェクトに直接関係のない`twine`やそれが依存するパッケージで`irohaenv`環境が汚染されることを防ぐ．

!!! Note
    `python setup.py sdist`，`python setup.py bdist_wheel`は`twine`環境下で実行することができる．


```bash
(irohaenv) > conda create -n twine
(irohaenv) > activate twine
(twine) > conda install twine -c conda-forge
```

さて，実際にアップロードしよう．`irohapj`ディレクトリ下で以下を実行する．

```bash
(twine) > twine upload dist/*
```

!!! Note
    最初のリリースの際にアップロード前にプロジェクトを明示的に登録する`twine register`は現在（2017/12）は不要になっている．

### PyPIからのインストール

PyPIからインストールできるかテストしてみよう．そのための一時的な環境`irohatest`を作る．この環境には`pip`自体がないのでインストールする．

```bash
(twine) > conda create -n irohatest
(twine) > activate irohatest
(irohatest) > conda install pip
(irohatest) > pip freeze
certifi==2017.11.5
wincertstore==0.2
```

さきほどアップロードした`iroha`パッケージをインストールする．確実にリモートからダウンロードするためにキャッシュを無効にする．

```bash
(irohatest) > pip install iroha --no-cache-dir
Collecting iroha
  Downloading iroha-0.1.1-py3-none-any.whl
Collecting click (from iroha)
  Downloading click-6.7-py2.py3-none-any.whl (71kB)
    100% |████████████████████████████████| 71kB 1.1MB/s
Installing collected packages: click, iroha
Successfully installed click-6.7 iroha-0.1.1
```

`click`パッケージも同時にインストールされていることがわかる．インストールされているパッケージを確認しておく．


```bash
(irohatest) > pip freeze
certifi==2017.11.5
click==6.7
iroha==0.1.1
wincertstore==0.2
```

!!! Note
    `conda`でパッケージを管理している場合には，`click`がpipでインストールされるのを望ましく思わないかもしれない．その場合には，事前に`conda install click`を実行しよう．

`iroha`パッケージは作業ディレクトリのものではなく，`irohatest`環境の`site-packages`下にダウンロードされたものが使われている．

```python
(irohatest) > python
>>> import iroha
>>> iroha.__file__
'C:\\Users\\daizu\\Miniconda3\\envs\\irohatest\\lib\\site-packages\\iroha\\__init__.py'
```
