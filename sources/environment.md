# Python実行環境

## Python

Pythonの実行環境は[Miniconda]( https://conda.io/miniconda.html)をインストールすることをお勧めします．インストール中のオプションはすべてデフォルトを選択します：

* インストール対象の選択では，Just for meを選ぶ．
* PATHには追加しない．


## 環境の作成

まずは`takuhai`環境を作成します．以下では`takuhai`環境で作業を行うので，アクティベートを忘れずに行いましょう．

```bash
> conda create -n takuhai
> activate takuhai
```

`conda list`はインストールされているパッケージの一覧表を表示します．

```bash
(takuhai) > conda list
# no packages
```

作ったばかりの環境にはひとつもパッケージが含まれていません．

!!! Note
    プロンプト前の`(takuhai)`は`takuhai`環境下でコマンドを実行していること意味します．

`takuhai`パッケージは[`click`](http://click.pocoo.org)，[`pelican`](http://docs.getpelican.com/en/stable/)，および[`livereload`](https://github.com/lepture/python-livereload)を使うのでインストールしておきましょう．

```bash
(takuhai) > conda install click
(takuhai) > conda install -c conda-forge pelican livereload
```

パッケージがインストールされたら，確認のため`conda list`を再度実行してみましょう．インストールされたパッケージの一覧表が表示されたはずです．

準備が整ったので実際にプロジェクトを作って行きましょう．
