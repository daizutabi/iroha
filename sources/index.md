# Pythonパッケージの作り方

更新日：2017/12/10

## はじめに

Pythonパッケージの作り方を説明する．単にパッケージを作るだけでなく，自作のパッケージをPyPI，Anaconda.orgに公開することを目指す．

## 参考URL

パッケージを公開するために，多くのサイトを参照したが，特に，以下のサイトに依るところが大きい．これらを参照すれば，より深く有益な情報を得ることができるだろう．

* [How To Package Your Python Code](https://python-packaging.readthedocs.io/en/latest/minimal.html)
* [Python Packaging User Guide](https://packaging.python.org/)
* [Python Packaging User Guide (日本語訳)](http://python-packaging-user-guide-ja.readthedocs.io/ja/latest/index.html)
* [Building conda packages with conda skeleton](https://conda.io/docs/user-guide/tutorials/build-pkgs-skeleton.html#building-conda-packages-with-conda-skeleton)

## 用語

ここで用いる単語を明確化しておく．

* 環境：Anacondaの仮想環境．`conda create -n <環境名>`で作られる．
* パッケージ：PyPIやAnaconda Cloudに公開するPythonコードの集合．Pythonスクリプト内で`import <package>`と記述してインポートされる．
* プロジェクト：上記のパッケージ自体と，それをPyPIやAnaconda Cloudに公開するために必要となるファイル（設定ファイル）やディレクトリ（ドキュメントやテスト）の集合．文脈によって，これを「パッケージ」や「ディストリビューション」と呼んだりするが，ここでは，「プロジェクト」と呼ぶことにする．

それぞれの具体的な名前を以下の通りとする．

* 環境名：`iroha`
* パッケージ：`iroha`
* プロジェクト：`iroha`

全部同じ名前である．区別が必要なときには，`iroha`環境，`iroha`パッケージ，`iroha`プロジェクトと明記する．
