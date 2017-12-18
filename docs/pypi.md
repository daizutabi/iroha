# PyPIへのアップロード

## ディストリビューションの作成

プロジェクトを[PyPI](https://pypi.python.org/pypi)に公開するために，プロジェクトのディストリビューションを作ります．

### ソースディストリビューション

ソースディストリビューションを作成します．`setup.py`があるディレクトリ下で以下を実行します．

```bash
(takuhai) > python setup.py sdist
```

`dist`ディレクトリが新しく作られて，その中に`takuhai-0.1.0.tar.gz`が格納されます．

### Wheels

ビルドされたwheelを作成します．`setup.py`があるディレクトリ下で以下を実行します．

```bash
(takuhai) > python setup.py bdist_wheel
```

`build`ディレクトリが新しく作られて，いろいろなファイルが作られます．wheel自体は`dist`下に`takuhai-0.1.0-py3-none-any.whl`の名前で格納されます．

## アップロード

### アカウントの作成

プロジェクトを[PyPI](https://pypi.python.org/pypi)にアップロードするためには事前にユーザーアカウントを作成しておく必要があります．テスト用の[Test PyPI](https://testpypi.python.org/pypi)にアップロードする場合は，別途ユーザーアカウントが必要です．以下のフォームから登録しましょう．

* [PyPIのユーザ登録](https://pypi.python.org/pypi?%3Aaction=register_form)
* [Test PyPIのユーザ登録](https://testpypi.python.org/pypi?%3Aaction=register_form)

ユーザー登録が終わったら，`~/.pypirc`を用意し，以下のように書きます．

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


!!! Note
    pypiのrepository行は省略できます．また`username`行および`password`行も省略できます．後述の`twine`に`-u USERNAME`引数，`-p PASSWORD`引数を渡すか、単に要求されたときに入力しましょう．

### アップロード

アップロードするには[twine](https://github.com/pypa/twine)を使います．twineは他のプロジェクトでも使うので，専用の`twine`環境下にインストールします．こうすることで，`takuhai`プロジェクトに直接関係のない`twine`やそれが依存するパッケージで`takuhai`環境が汚染されることを防ぎます．

!!! Note
    `python setup.py sdist`，`python setup.py bdist_wheel`は`twine`環境下で実行することもできます．


```bash
(takuhai) > conda create -n twine
(takuhai) > activate twine
(twine) > conda install -c conda-forge twine
```

PyPIにアップロードしましょう．`dist`があるディレクトリ下で以下を実行します．

```bash
(twine) > twine upload dist/*
```

### PyPIからのインストール

PyPIからインストールできるかテストしてみましょう．そのための一時的な`takuhai-pypi`環境を作ります．確実にリモートからダウンロードするためにキャッシュを無効にします．

```bash
(twine) > conda create -n takuhai-pypi
(twine) > activate takuhai-pypi
(takuhai-pypi) > conda install pip
(takuhai-pypi) > pip install takuhai --no-cache-dir
Collecting takuhai
  Downloading takuhai-0.1.0-py3-none-any.whl
Collecting livereload (from takuhai)
  Downloading livereload-2.5.1.tar.gz
（後略）
```

必要なパッケージも同時にインストールされていることが分かります．

```bash
(takuhai-pypi) > pip freeze
blinker==1.4
certifi==2017.11.5
click==6.7
docutils==0.14
feedgenerator==1.9
Jinja2==2.10
livereload==2.5.1
MarkupSafe==1.0
pelican==3.7.1
Pygments==2.2.0
python-dateutil==2.6.1
pytz==2017.3
six==1.11.0
takuhai==0.1.0
tornado==4.5.2
Unidecode==0.4.21
wincertstore==0.2
```

`takuhai`パッケージは作業ディレクトリのものではなく，`takuhai-pypi`環境の`site-packages`下にダウンロードされたものが使われています．

```python
(takuhai-pypi) > cd ..
(takuhai-pypi) > python
>>> import takuhai
>>> takuhai.__file__
'C:\\Users\\daizu\\Miniconda3\\envs\\takuhai-pypi\\lib\\site-packages\\takuhai\\__init__.py'
```

最後に不要になった環境を削除しておきます．

```bash
(takuhai-pypi) > activate root
(root) > conda remove -n takuhai-pypi --all
```
