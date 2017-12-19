# 継続的インテグレーションでのテスト

継続的インテグレーションツールとして，GitHubと連動する[Travis CI](https://travis-ci.org/)を用います．Travis CIがはじめてなら，まずは[Getting started](https://docs.travis-ci.com/user/getting-started/)を一読しましょう．以下ではテストがパスするまでの最低限の手順について説明します．

## 準備

Travis CIにGitHubアカウントでログインします．画面右上のユーザ名のメニューから[Accounts](https://travis-ci.org/profile)を選択します．レポジトリ一覧が表示されるので，`takuhai`レポジトリをビルド可能状態にします．

![Build enable](img/enable.png) daizutabi/takuhai

ローカルPCの`takuhai`プロジェクトディレクトリ下に`.travis.yml`ファイルを作成します．以下の内容で保存しておきましょう．

```yaml
language: python
python:
  - "3.6"
install:
  - pip install -r requirements.txt
  - pip install -e .
script:
  - takuhai
  - pytest
```

`requirements.txt`には依存パッケージを記述します．`setup.py`と同じディレクトリに以下の内容で保存しておきます．

```text
click
pelican
livereload
```

!!! Note
    `takuhai`パッケージが依存するパッケージは，`setup.py`内に記述していました．再度，`requirements.txt`にも同じ内容を書くのは冗長でないかと疑問を持つかもしれません．冗長を回避するために，`setup.py`が`requirements.txt`の内容を解析して自動で依存パッケージを指定することも可能です．

## ビルド

Travis CIの`takuhai`プロジェクトページを開きます．ローカルPCのコマンドラインから`takuhai`レポジトリを`git push`してみましょう．するとTravis CIのページが自動で切り替わり，ビルド処理を始めます．しばらくすると，テストにパスしたことが確認できます．

## バッジをつけよう

ビルドに成功したのでGitHubレポジトリのREADMEにバッジをつけましょう．あわせてPyPIのバッジもつけておきます．`README.md`を以下の内容で保存します．

```markdown
# Takuhai Project

---
[![PyPI version][pypi-image]][pypi-link]
[![Travis][travis-image]][travis-link]

[pypi-image]: https://badge.fury.io/py/takuhai.svg
[pypi-link]: https://pypi.org/project/takuhai
[travis-image]: https://travis-ci.org/daizutabi/takuhai.svg?branch=master
[travis-link]: https://travis-ci.org/daizutabi/takuhai
```

`git push`後に[レポジトリのページ](https://github.com/daizutabi/takuhai)を確認するとバッジが表示されています．
