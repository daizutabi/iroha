# Pythonパッケージの作り方

更新日：2017/12/16

## はじめに

Pythonパッケージの作り方を説明します．単にパッケージを作るだけでなく，自作のパッケージを[PyPI](https://pypi.org)，[Anaconda Cloud](https://anaconda.org/)に公開することを目指します．また，[Travis CI](https://travis-ci.org/)を使って継続的インテグレーションを実践します．

## 参考URL

以下のサイトを参考にしました．直接参照すれば，より深く有益な情報を得ることができるでしょう．

* [How To Package Your Python Code](https://python-packaging.readthedocs.io/en/latest/minimal.html)
* [Python Packaging User Guide](https://packaging.python.org/)
* [Python Packaging User Guide (日本語訳)](http://python-packaging-user-guide-ja.readthedocs.io/ja/latest/index.html)
* [Building conda packages with conda skeleton](https://conda.io/docs/user-guide/tutorials/build-pkgs-skeleton.html#building-conda-packages-with-conda-skeleton)

## 用語

本サイトで用いる単語を明確化しておきます：

* 環境：Anacondaの仮想環境．`conda create -n <環境名>`で作られる．
* パッケージ：PyPIやAnaconda Cloudに公開するPythonコードの集合．Pythonスクリプト内で`import <package>`と記述して利用する．
* プロジェクト：上記のパッケージ自体と，それをPyPIやAnaconda Cloudに公開するために必要となるファイル（設定ファイル）やディレクトリ（ドキュメントやテスト）の集合．ひとつのプロジェクトに対してひとつのGitHubレポジトリを作る．

以下では，`takuhai`プロジェクトを作成していきます．それぞれの具体的な名前を以下に示します：

* 環境名：`takuhai`
* パッケージ名：`takuhai`
* プロジェクト名：`takuhai`

全部同じ名前ですね．区別が必要なときには，`takuhai`環境，`takuhai`パッケージ，`takuhai`プロジェクトと明記することにします．
