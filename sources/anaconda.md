# Anaconda Cloudへのアップロード

いよいよ最後のタスクです．`takuhai`パッケージを[Anaconda Cloud](https://anaconda.org/)で公開しましょう． [Building conda packages with conda skeleton](https://conda.io/docs/user-guide/tutorials/build-pkgs-skeleton.html)を参照して一歩ずつ進めていきます．

## condaパッケージの作成

condaパッケージを作成するために必要な`conda-build`パッケージは，ルート環境にしかインストールできません．`m2-patch`も同時にインストールしておきます．

```bash
> activate root
(root) > conda install m2-patch conda-build
```

パッケージを作成したいディレクトリに移動して，以下を実行します．

```bash
(root) > cd C:\Users\daizu\Desktop
(root) > conda skeleton pypi takuhai
```

!!! Note
    そのディレクトリにすでに`takuhai`ディレクトリがあるとエラーが発生します．

`takuhai`ディレクトリが作成されて，その下に`meya.yml`ファイルが格納されます．パッケージをビルドします．`pelican`，`livereload`をダウンロードするために`conda-forge`チャネルを指定する必要があります．

```bash
(root) > conda build -c conda-forge takuhai
```

しばらくするとビルドが完了します．


## ローカルのパッケージをインストール

`--use-local`フラッグを指定して`takuhai`パッケージをインストールします．

```bash
(root) > conda create -n takuhai-anaconda
(root) > activate takuhai-anaconda
(takuhai-anaconda) > conda install --use-local -c conda-forge takuhai
```

依存パッケージとともに`takuhai`パッケージがインストールされました．`conda list`を確認すると，`takuhai`パッケージが`local`チャネルでインストールされていることが分かります．チェックが済んだので，不要になった環境を削除しておきます．

```bash
(takuhai-anaconda) > activate root
(root) > conda remove -n takuhai-anaconda --all
```

## オプションのステップ

説明は省きますが，以下のようなオプションのステップがあります．

* [Optional—Building for a different Python version]( https://conda.io/docs/user-guide/tutorials/build-pkgs-skeleton.html#optional-building-for-a-different-python-version)

* [Optional—Converting conda package for other platforms](https://conda.io/docs/user-guide/tutorials/build-pkgs-skeleton.html#optional-converting-conda-package-for-other-platforms)

## Anaconda Cloudへのアップロード

[Anaconda Cloud](https://anaconda.org/)へアップロードしましょう．アカウントを作成していない場合は，[Anaconda Cloud](https://anaconda.org)でアカウントを作成しておきます．

アップロードに必要な`anaconda-client`をインストールします．

```bash
(root) > conda install anaconda-client
```

次に，

```bash
(root) > anaconda login
```

として，Anaconda Cloudのユーザー名とパスワードを入力します．

先ほど作ったパッケージをアップロードします．

```bash
(root) > cd C:\Users\daizu\Miniconda3\conda-bld\win-64
(root) > anaconda upload takuhai-0.1.2-py36_0.tar.bz2
```

[Anaconda Cloud](https://anaconda.org)にアクセスすると，Packagesのところに`takuhai`パッケージの表示が見つかるはずです．

!!! Note
    ビルド成功時に同時にアップロードを行うためには，`conda config --set anaconda_upload yes`を実行します．

Anaconda Cloud上のパッケージをインストールしてみます．チャネルには`daizutabi`と`conda-forge`の両方を指定します．念のためキャッシュを削除しておきましょう．

```bash
(root) > conda clean --all
(root) > conda create -n takuhai-anaconda
(root) > activate takuhai-anaconda
(conda-takuhai) > conda install -c daizutabi -c conda-forge takuhai
```

依存パッケージとともに`takuhai`パッケージがインストールされました．

`conda list`を確認すると，`takuhai`パッケージが`daizutabi`チャネルでインストールされていることが分かります．最後に，不要になった環境を削除しておきます．

```bash
(takuhai-anaconda) > activate root
(root) > conda remove -n takuhai-anaconda --all
```


## バッジの追加

Anaconda Cloudにパッケージを登録したことを示すバッジを`README.md`につけます．

```markdown
# takuhai Project

Pelican converter and server

---

[![PyPI Version][pypi-v-image]][pypi-v-link]
[![Anaconda Version][anaconda-v-image]][anaconda-v-link]
[![Travis][travis-image]][travis-link]

[pypi-v-image]: https://img.shields.io/pypi/v/takuhai.png
[pypi-v-link]: https://pypi.python.org/pypi/takuhai
[anaconda-v-image]: https://anaconda.org/daizutabi/takuhai/badges/version.svg
[anaconda-v-link]: https://anaconda.org/daizutabi/takuhai
[travis-image]: https://img.shields.io/travis/daizutabi/takuhai.svg?style=flat-square&label=Travis+CI
[travis-link]: https://travis-ci.org/daizutabi/takuhai
```

`git push`後に[レポジトリのページ](https://github.com/daizutabi/takuhai)を確認するとバッジが追加されていることが確認できるでしょう．
