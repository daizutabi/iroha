# プロジェクトの作成

「プロジェクト」は，Pythonコード内で`import`されるパッケージに付加情報を合わせたものである．プロジェクトをGitHub上の一つのレポジトリに対応させる．まずは，GitHubで新規にレポジトリを作成する．名前はプロジェクト名と同じく`iroha`とする．新規作成の際には，

* [x] Initialize this repository with a README
* Add .gitignore: [None]
* Add a license: [MIT License]

を選ぶ．

レポジトリをローカルにクローンする．適当なディレクトリに移動し，

```bash
(iroha) > cd C:\Users\daizu\Python
(iroha) > git clone https://github.com/daizutabi/iroha.git
```

とする．`C:\Users\daizu\Documents\Python\iroha`ディレクトリが作成された．


## パッケージの作成

まずは根幹となるパッケージを作っていこう．ディレクトリ構造は以下の通りである．同時に`.gitignore`も作っておく． 各ファイルの内容は，GitHubの[irohaレポジトリ](https://github.com/daizutabi/iroha/tree/master/iroha)を参照されたい．

```
+ iroha
    + iroha
        + add
            - __init__.py
            - calc.py
        + data
            - numbers.txt
        + sub
            - __init__.py
            - calc.py
        - __init__.py
        - common.py
        - main.py
    .gitignore
```

動作はいたって単純である．`numbers.txt`の内容から数値を読み取って，加算もしくは減算の結果をプリントする．実際に実行するためには，このパッケージをローカルにインストールする必要がある．

!!! Note
    もちろん，環境変数`PYTHONPATH`に`iroha`ディレクトリを追加すればパッケージをインストールしないでも実行できる．ここではあえてこの方法を避けて，余計な環境変数を作らない方針をとる．環境変数`PATH`にも一切ふれていないことを思い出してほしい．

## 設定ファイルの作成

プロジェクトをパッケージングしてインストールするために必要な設定ファイルを作成していく．詳しくは，[「Python Packaging User Guide」](http://python-packaging-user-guide-ja.readthedocs.io/ja/latest/index.html)の[「プロジェクトのパッケージングと配布」](http://python-packaging-user-guide-ja.readthedocs.io/ja/latest/distributing.html#id4)を参照されたい．今回は以下の2つのファイルを準備した．


* [`setup.py`](https://github.com/daizutabi/iroha/blob/master/setup.py)
* [`MANIFEST.in`](https://github.com/daizutabi/iroha/blob/master/MANIFEST.in)


## 作業用にローカルにインストール

ここまで準備できたら，パッケージとしてローカルにインストールすることができる．`iroha`ディレクトリ下で以下を実行する．オプション`-e`をつけることで，編集可能な作業用としてインストールする．

```bash
(iroha) > pip install -e .
```

動作をおさらいしておこう．`numbers.txt`の内容（`3 2`）から数値を読み取って，加算もしくは減算の結果をプリントする．まずは，通常のPythonファイルとして実行する．`iroha`ディレクトリ下で以下を実行する．

```bash
(iroha) > python main.py add
5
(iroha) > python main.py sub
1
```

ここで，`main.py`は`iroha`パッケージの中の`main.py`としてではなく，単なる一つのPythonスクリプトとして実行されている．

`setup.py`で指定しておいた実行コマンドも使えるようになっている．

```bash
(iroha) > iroha add
5
(iroha) > iroha sub
1
```

上のコマンドの実行ファイルは，

```
C:\Users\daizu\Miniconda3\envs\iroha\Scripts\iroha.exe
```

である．試しにアンインストールしてみよう．

```bash
(iroha) > pip uninstall iroha
```

上記`iroha.exe`が勝手に消去されるのが分かる．

別のPythonプログラムから`iroha`パッケージを使うこともできる．

```python
(iroha) > python
>>> import iroha
>>> iroha.__file__
'C:\\Users\\daizu\\Documents\\Python\\iroha\\iroha\\__init__.py'
```

インストールといっても，今回は作業用にインストールしたので，別の場所にコピーが作成されているのではなく，`iroha`ディレクトリ以下の元のファイルがそのまま使われている．`sys.path`を見てみよう．

```python
>>> import sys
>>> for path in sys.path:
...     print(path)

C:\Users\daizu\Miniconda3\envs\iroha\python36.zip
C:\Users\daizu\Miniconda3\envs\iroha\DLLs
C:\Users\daizu\Miniconda3\envs\iroha\lib
C:\Users\daizu\Miniconda3\envs\iroha
C:\Users\daizu\Miniconda3\envs\iroha\lib\site-packages
c:\users\daizu\documents\python\iroha
```

`sys.path`の最後に作業ディレクトリが追加されている．先ほどと同じように`iroha`パッケージをアンインストールすると，`sys.path`から`iroha`パッケージへの参照がなくなる．
