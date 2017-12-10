# 継続的インテグレーションでのテスト

継続的インテグレーションツールとして，GitHubと連動する[Travis CI](https://travis-ci.org/)を用いる．Travis CIがはじめてならば，まずは[Getting started](https://docs.travis-ci.com/user/getting-started/)を一読しよう．以下では最低限の，少なくとテストがパスするまでの手順について説明する．


## 準備

Travis CIにGitHubアカウントでログインする．画面右上のユーザ名のメニューから[Accounts](https://travis-ci.org/profile)を選択する．レポジトリ一覧が表示されるので，`irohapj`レポジトリをビルド可能状態にする．

![Build enable](img/enable.png) daizutabi/irohapj

ローカルの`irohapj`ディレクトリ下に`.travis.yml`ファイルを作成し，以下の内容で保存する．

```yaml
language: python
```

## ビルトが成功するまで

`git push`する．するとTravis CIのページが自動で切り替わり，ビルド処理を始めたことがわかるだろう．`python 2.7`といった文字列が見受けられる．しばらくすると，ビルドが失敗に終わったことが通知される．何も設定していないので当然だ．Job logを見ると，`requirements.txt`がないことに警告が出ている模様だ．`requirements.txt`には依存パッケージを記述するようなので，以下の内容のファイルを`irohapj`ディレクト下に`requirements.txt`の名前で保存しておく．

```text
click
```

!!! Note
    `iroha`パッケージが依存するパッケージは，`setup.py`内に記述していた．再度，`requirements.txt`にも同じ内容を書くのは冗長でないかと疑問を持つかもしれない．冗長を回避するために，`setup.py`が`requirements.txt`の内容を解析して自動で依存パッケージを指定することも可能である．


その他もろもろのドキュメントを読んでみると，Pythonのバージョン，インストール作業，および実行スクリプトを指定すればよいようだ．現時点での`.travis.yml`は以下のようになっている．


```yaml
language: python
python:
  - "2.7"
  - "3.4"
  - "3.5"
  - "3.6"
install:
  - pip install -r requirements.txt
script:
  - pytest
```

もう一度`git push`する．pytestの実行までは進んだようだが，エラーで停止してしまった．どうやら`iroa`パッケージが見つからないらしい．`.travis.yml`の`install`のところまで処理が進んだとき，カレントディレクトリはプロジェクトのルートディレクトリになっているようなので，次のようにして自分自身を作業用としてインストールする．

```yaml
language: python
(中略)
install:
  - pip install -r requirements.txt
  - pip install -e .
(後略)
```

再び`git push`する．今度はビルドに成功した．

!!! Tip
    `pip install -e .` 以外でパッケージにパスを通す方法は？

## バッジをつけよう

ビルドに成功したのでGitHubレポジトリに ![Build: Passing](img/passing.svg) のバッジをつけよう．あわせてPyPIのバッジもつけておく．

`README.md`を以下の内容で保存する．

```markdown
# Iroha Project

Python Packaging Tutorial

---

[![PyPI Version][pypi-v-image]][pypi-v-link]
[![Build Status][travis-image]][travis-link]

[pypi-v-image]: https://img.shields.io/pypi/v/iroha.png
[pypi-v-link]: https://pypi.python.org/pypi/iroha
[travis-image]: https://travis-ci.org/daizutabi/irohapj.svg?branch=master
[travis-link]: https://travis-ci.org/daizutabi/irohapj
```

`git push`後に[レポジトリのページ](https://github.com/daizutabi/irohapj)を確認するとバッジが表示されている．

![バッジ](img/badge.png)
