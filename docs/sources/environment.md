# Python実行環境

## Python

Pythonの実行環境は[Miniconda]( https://conda.io/miniconda.html)をインストールすることをお勧めする．さらにインストール中のオプションはすべてデフォルト選択し，

* インストール対象の選択では，Just for meを選ぶ．
* PATHには追加しない．

とする．

## 環境の作成

まずは環境を作成する．環境の名前は`iroha`とする．環境を作った後`iroha`環境をアクティベートする．

```bash
> conda create -n iroha
> activate iroha
```

`conda list`はインストールされているパッケージの一覧表を表示する．

```bash
(iroha) > conda list
# no packages
```

作ったばかりの環境にはひとつもパッケージが含まれていない．

!!! Note
    プロンプト前の`(iroha)`は`iroha`環境下でコマンドを実行していること意味する．

`iroha`パッケージは[`click`パッケージ](http://click.pocoo.org)に依存する（を使う）のでインストールしておこう．

```bash
(iroha) > conda install click
```

パッケージがインストールされたら，確認のため`conda list`を再度実行する．

```bash
(iroha) > conda list
certifi                   2017.11.5        py36hb8ac631_0
click                     6.7              py36hec8c647_0
pip                       9.0.1            py36h226ae91_4
python                    3.6.3                h3b118a2_4
setuptools                36.5.0           py36h65f9e6e_0
vc                        14                   h2379b0c_2
vs2015_runtime            14.0.25123           hd4c4e62_2
wheel                     0.30.0           py36h6c3ec14_1
wincertstore              0.2              py36h7fe50ca_0
```

インストールするように指示した`click`パッケージ以外にもいろいろインストールされているようだ．準備が整ったので実際にプロジェクトを作っていこう．
