[目次](../../../README.md) > [技術要素](../../README.md) > [ネットワーク](../README.md) > [プロトコル](README.md) > 知識

# プロトコルの知識

## 試験で問われるポイント

1. [FE/AP] 各層の代表的なプロトコルを答えられる
2. [FE/AP] よく出るポート番号（80/443/25/53 など）
3. [AP] TCP と UDP のどちらを使うかと、その理由

## 詳細

### OSI参照モデルと代表的なプロトコル [FE/AP]

| 層 | 名前 | 例 |
|---|---|---|
| 7 | アプリケーション | HTTP, SMTP, DNS |
| 4 | トランスポート | TCP, UDP |
| 3 | ネットワーク | IP, ICMP |

<!-- 表は3列まで。1段落は3行まで -->

### TCP と UDP [AP]

- TCP：コネクション型。再送制御あり
- UDP：コネクションレス型。速い。DNSの問い合わせ、動画配信など

## 関連

- [IPアドレス](../ip-address/knowledge.md)：IP は第3層
- [セキュリティ / TLS](../../11_security/knowledge.md)：HTTPS は TLS の上で HTTP を動かす

## 関連問題

- [R1秋 FE 午前 問25](questions/FE_R01A_AM25.md)：ポート番号
- [R1秋 FE 午前 問31](../questions/FE_R01A_AM31.md)：中カテゴリ直下の問題

## 関連する科目B

- [R5春 AP 午後 問5](../../../ap-subject-b/02_network/questions/AP_R05S_PM05.md)
