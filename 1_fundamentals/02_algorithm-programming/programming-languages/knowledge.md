[目次](../../../README.md) > [基礎理論](../../README.md) > [アルゴリズムとプログラミング](../README.md) > [プログラム言語](README.md) > 知識

# プログラム言語の知識

## 試験で問われるポイント

1. [FE] コンパイラ方式とインタプリタ方式の違い
2. [FE] 各言語の実行方式と主な用途（下の一覧表）
3. [FE] Java は中間コードを仮想マシン（JVM：Java Virtual Machine）で実行する

## 詳細

### 言語処理系 [FE]

| 方式 | 動き | 特徴 |
|---|---|---|
| コンパイラ | 実行前に全体を機械語へ翻訳 | 実行が速い。事前の翻訳が必要 |
| インタプリタ | 1行ずつ解釈しながら実行 | すぐ実行できる。実行は遅め |
| 中間コード＋仮想マシン | 中間コードに翻訳し、仮想マシンで実行 | OS（Operating System：基本ソフトウェア）に依存しにくい（Javaなど） |

### 主な言語の特徴 [FE]

| 言語 | 実行方式 | 特徴・主な用途 |
|---|---|---|
| C | コンパイラ | OS・組込み。ポインタで低水準な操作ができる |
| C++ | コンパイラ | C にオブジェクト指向を追加 |
| Java | 中間コード＋JVM | オブジェクト指向。OSを問わず動く |
| Python | インタプリタ | 文法が簡潔。インデントでブロックを表す。AI（Artificial Intelligence：人工知能）・データ分析 |
| Perl | インタプリタ | テキスト処理が得意。CGI（Common Gateway Interface）。UNIX・Windows両対応 |
| PHP | インタプリタ | Webサーバ側の処理。HTML（HyperText Markup Language）に埋め込める |
| Ruby | インタプリタ | 日本発。すべてがオブジェクト。Webアプリ（Rails） |
| JavaScript | インタプリタ | Webブラウザ上で動く。Node.jsでサーバ側も可 |
| R | インタプリタ | 統計解析・グラフ作成 |
| COBOL | コンパイラ | 事務処理（帳票・金額計算）。英語に近い文法。COmmon Business Oriented Language の略 |
| Fortran | コンパイラ | 科学技術計算。FORmula TRANslation（数式翻訳）の略 |

- インタプリタ言語は**事前のコンパイル不要**。CGI に使われることはあっても、**Webサーバがなくても実行できる**

### CGI [FE]

**CGI（Common Gateway Interface）**は、Webサーバが**外部のプログラムを呼び出し**、その実行結果を**Webページとしてブラウザに返す**ための仕組み。

- 流れ：ブラウザ → Webサーバ → CGIプログラムを実行 → 結果（HTML）をブラウザへ返す
- 用途：掲示板やアンケートフォームなど、アクセスのたびに内容が変わる**動的なページ**
- CGIは**言語ではなく、Webサーバとプログラムをつなぐ決まり**。Perl でよく書かれたが、C や Python などでも書ける
- 要求のたびにプログラムを起動するため、サーバの負荷が高い。今は PHP やアプリケーションサーバが主流

## 関連

- [オブジェクト指向](../../../4_development/12_system-development/object-oriented/knowledge.md)：C++・Java・Ruby の土台

## 関連問題

- [H29秋 FE 午前 問8](questions/FE_H29-aki_AM08.md)：Perl の実行方式

## 関連する科目B

- [FE 科目B アルゴリズム](../../../fe-subject-b/algorithm/README.md)
