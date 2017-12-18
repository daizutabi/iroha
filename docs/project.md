# プロジェクトの作成

「プロジェクト」は，Pythonコード内で`import`されるパッケージに付加情報を合わせたものです．ひとつのプロジェクトに対して，ひとつのGitHubレポジトリを対応させます．まずは，GitHubに新規にレポジトリを作成します．レポジトリの名前はプロジェクト名と同じく`takuhai`です．新規作成の際には，

* [x] Initialize this repository with a README
* Add .gitignore: [None]
* Add a license: [MIT License]

を選んでおきます．次にレポジトリをローカルPCにクローンします．

```bash
(takuhai) > cd C:\Users\daizu\Documents\GitHub
(takuhai) > git clone https://github.com/daizutabi/takuhai.git
```

`C:\Users\daizu\Documents\GitHub\takuhai`ディレクトリが作成されました．


## パッケージの作成

`takuhai`パッケージの詳細についてはここでは説明しませんが，できることを示しておきます：

+ ファイル名からPelican文書のメタデータを自動作成．
+ 文書が変更されたら自動でサイト生成を行ってブラウザをリロード．

実際に使ってみましょう．そのためには，`takuhai`環境下にインストールする必要があります．

!!! Note
    もちろん，環境変数`PYTHONPATH`に`takuhai`ディレクトリを追加すればパッケージをインストールしないでも実行できます．しかし，ここではあえてこの方法を避けて，余計な環境変数を作らない方針をとります．Pythonを実行するために，環境変数`PATH`にも一切ふれていないことを思い出してください．

## 設定ファイルの作成

パッケージをインストールするために必要な設定ファイルを作成していきましょう．詳しくは，[「Python Packaging User Guide」](http://python-packaging-user-guide-ja.readthedocs.io/ja/latest/index.html)の[「プロジェクトのパッケージングと配布」](http://python-packaging-user-guide-ja.readthedocs.io/ja/latest/distributing.html)を参照してください．まずは必須となる[`setup.py`](https://github.com/daizutabi/takuhai/blob/master/setup.py)を準備しました．`setup.py`は`takuhai`レポジトリの直下に置きます．

## 作業用にインストール

ここまで準備できたら，パッケージをインストールすることができます．`setup.py`があるディレクトリで以下を実行します．オプション`-e`をつけることで，「編集可能」な作業用としてインストールします．

```bash
(takuhai) > pip install -e .
```

`takuhai`パッケージの中の`main.py`を実行してみます．

```bash
(takuhai) > cd takuhai
(takuhai) > python main.py
Usage: main.py [OPTIONS] COMMAND [ARGS]...
（後略）
```

`main.py`は`takuhai`パッケージの中の`main.py`としてではなく，単なる一つのPythonスクリプトとして実行されていることに留意しましょう．

`setup.py`で指定しておいた実行コマンドも使えるようになっています．

```bash
(takuhai) > takuhai
Usage: main.py [OPTIONS] COMMAND [ARGS]...
（後略）
```

コマンド`takuhai`の実行ファイルは，

```
C:\Users\daizu\Miniconda3\envs\takuhai\Scripts\takuhai.exe
```

です．試しにアンインストールしてみましょう．

```bash
(takuhai) > pip uninstall takuhai
```

上記の`takuhai.exe`が消去されるのが分かると思います．

別のPythonプログラムから`takuhai`パッケージを使うこともできます．

```python
(takuhai) > python
>>> import takuhai
>>> takuhai.__file__
'c:\\users\\daizu\\documents\\github\\takuhai\\takuhai\\__init__.py'
```

インストールといっても，今回は作業用にインストールしたので，別の場所にコピーが作られているわけではありません．`takuhai`ディレクトリ以下のファイルがそのまま使われています．`sys.path`を見てみましょう．

```python
>>> import sys
>>> for path in sys.path:
...     print(path)

C:\Users\daizu\Miniconda3\envs\takuhai\python36.zip
C:\Users\daizu\Miniconda3\envs\takuhai\DLLs
C:\Users\daizu\Miniconda3\envs\takuhai\lib
C:\Users\daizu\Miniconda3\envs\takuhai
C:\Users\daizu\Miniconda3\envs\takuhai\lib\site-packages
c:\users\daizu\documents\github\takuhai
```

`sys.path`の最後に作業ディレクトリが追加されています．先ほどと同じように`takuhai`パッケージをアンインストールすると，`sys.path`から`takuhai`パッケージへの参照がなくなります．
