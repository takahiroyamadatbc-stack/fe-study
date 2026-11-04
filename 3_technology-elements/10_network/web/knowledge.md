[目次](../../../README.md) > [技術要素](../../README.md) > [ネットワーク](../README.md) > [Web](README.md) > 知識

# Webの知識

## 試験で問われるポイント

1. [FE] HTTP は状態を覚えない（ステートレス）。Cookie とセッションで「続きのやり取り」を実現する
2. [FE] HTTP はポート80、HTTPS はポート443。HTTPS は TLS で暗号化する
3. [FE] CGI は言語ではなく、Webサーバが外部プログラムを呼び出す仕組み

## 詳細

### HTTP と HTTPS [FE]

**HTTP（HyperText Transfer Protocol）**は、ブラウザとWebサーバがやり取りするための決まり（プロトコル）。ブラウザが**リクエスト**（要求）を送り、サーバが**レスポンス**（応答）を返す。

| 項目 | HTTP | HTTPS |
|---|---|---|
| 正式名 | HyperText Transfer Protocol | HTTP Secure |
| ポート番号 | 80 | 443 |
| 暗号化 | なし | TLS（Transport Layer Security）で暗号化 |

- HTTP は**ステートレス**（前のやり取りを覚えていない）。1回のリクエストとレスポンスで完結する

### URL [FE]

**URL（Uniform Resource Locator）**は、Web上の場所を表す住所。

例：`https://www.example.com:443/news/index.html?id=5`

| 部分 | 例 | 意味 |
|---|---|---|
| スキーム | https | 使うプロトコル |
| ホスト名 | www.example.com | サーバの名前（DNSでIPアドレスに変換） |
| ポート番号 | 443 | 省略するとスキームの標準番号 |
| パス | /news/index.html | サーバ内のファイルの場所 |
| クエリ | ?id=5 | サーバに渡す追加の情報 |

- DNS（Domain Name System）は、ホスト名をIPアドレスに変換する仕組み

### HTTPのメソッドとステータスコード [FE]

| メソッド | 用途 | データの渡し方 |
|---|---|---|
| GET | ページやデータを取得する | URLの後ろ（クエリ）に付く。履歴に残る |
| POST | フォームの内容を送信する | リクエストの本文に入れる。URLに出ない |

| コード | 意味 | 例 |
|---|---|---|
| 200番台 | 成功 | 200 OK |
| 300番台 | 転送（リダイレクト） | 301 恒久的に移動 |
| 400番台 | クライアント側のエラー | 404 Not Found（ページがない） |
| 500番台 | サーバ側のエラー | 500 Internal Server Error |

### Cookie [FE]

**Cookie（クッキー）**は、Webサーバがブラウザに保存させる小さなデータ。ブラウザは、次に同じサイトへアクセスするとき、Cookie を**自動で送り返す**。

- 流れ：サーバがレスポンスで Cookie を渡す → ブラウザが保存 → 次のリクエストで Cookie を送る → サーバが「前に来た人だ」と分かる
- 用途：ログイン状態の維持、ショッピングカートの中身、サイトの表示設定
- 有効期限を決められる。期限なしならブラウザを閉じると消える

| 属性 | 意味 |
|---|---|
| Secure | HTTPS の通信でだけ Cookie を送る（盗聴対策） |
| HttpOnly | JavaScript から Cookie を読めなくする（XSS：Cross Site Scripting 対策） |

### セッション管理 [FE]

**セッション**は、ログインしてからログアウトするまでのような、一続きのやり取りのこと。HTTP はステートレスなので、次のようにして「同じ人」を見分ける。

1. ログインに成功したら、サーバが推測されにくい**セッションID**を発行する
2. セッションIDを Cookie に入れてブラウザに渡す
3. 以後、ブラウザは毎回セッションIDを送り、サーバはそれで利用者を見分ける

- セッションIDを盗まれると、その人になりすまされる（**セッションハイジャック**）。HTTPS と Secure 属性で盗まれにくくする

### CGI [FE]

**CGI（Common Gateway Interface）**は、Webサーバが**外部のプログラムを呼び出し**、その実行結果を**Webページとしてブラウザに返す**ための仕組み。

- 流れ：ブラウザ → Webサーバ → CGIプログラムを実行 → 結果（HTML：HyperText Markup Language）をブラウザへ返す
- 用途：掲示板やアンケートフォームなど、アクセスのたびに内容が変わる**動的なページ**
- CGIは**言語ではなく、Webサーバとプログラムをつなぐ決まり**。Perl でよく書かれたが、C や Python などでも書ける
- 要求のたびにプログラムを起動するため、サーバの負荷が高い。今は PHP やアプリケーションサーバが主流

| 用語 | 中身が変わるか | 例 |
|---|---|---|
| 静的なページ | 変わらない（HTMLファイルをそのまま返す） | 会社概要のページ |
| 動的なページ | アクセスのたびに作る | 検索結果、掲示板 |

## 関連

- [プログラム言語](../../../1_fundamentals/02_algorithm-programming/programming-languages/knowledge.md)：CGI を書く言語（Perl、PHP など）
- [LANの基礎](../lan-basics/knowledge.md)：同じ「ネットワーク」の別の論点

## 関連問題

- [H29秋 FE 午前 問8](../../../1_fundamentals/02_algorithm-programming/programming-languages/questions/FE_H29-aki_AM08.md)：Perl と CGI

## 関連する科目B

- [AP 科目B ネットワーク](../../../ap-subject-b/02_network/README.md)
