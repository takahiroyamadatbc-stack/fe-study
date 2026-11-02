# 構成図（ドラフト確認用。本番には置かない）

```
fe-study/
├─ README.md                    目次
├─ CLAUDE.md                    ルール
├─ formulas.md                  公式・計算問題集
├─ _templates/
│   ├─ category_readme.md       中カテゴリの概要
│   ├─ subcategory_readme.md    小カテゴリの入口
│   ├─ knowledge.md             知識
│   ├─ question_a.md            科目A／午前の問題
│   ├─ question_b.md            科目B／午後（記述式）の問題
│   ├─ subject_b_readme.md      科目Bの分野ごとの README
│   ├─ batch_input.xlsx         まとめて記録する用（プルダウン付き）
│   └─ batch_input.csv          同上（CSV）
│
├─ 1_fundamentals/              基礎理論
│   ├─ README.md
│   ├─ 01_basic-theory/
│   └─ 02_algorithm-programming/
├─ 2_computer-system/           コンピュータシステム
│   ├─ 03_computer-components/
│   ├─ 04_system-components/
│   ├─ 05_software/
│   └─ 06_hardware/
├─ 3_technology-elements/       技術要素
│   ├─ 07_human-interface/
│   ├─ 08_multimedia/
│   ├─ 09_database/
│   ├─ 10_network/
│   │   ├─ README.md            概要
│   │   ├─ knowledge.md         知識
│   │   ├─ questions/
│   │   └─ protocol/            ← 小カテゴリ（必要になったら作る）
│   │       ├─ README.md
│   │       ├─ knowledge.md
│   │       └─ questions/
│   │           └─ FE_R01A_AM25.md
│   └─ 11_security/
├─ 4_development/               開発技術
│   ├─ 12_system-development/
│   └─ 13_software-dev-management/
├─ 5_project-management/
│   └─ 14_project-management/
├─ 6_service-management/
│   ├─ 15_service-management/
│   └─ 16_system-audit/
├─ 7_system-strategy/
│   ├─ 17_system-strategy/
│   └─ 18_system-planning/
├─ 8_business-strategy/
│   ├─ 19_business-strategy-mgmt/
│   ├─ 20_technology-strategy-mgmt/
│   └─ 21_business-industry/
├─ 9_corporate-legal/
│   ├─ 22_corporate-activity/
│   └─ 23_legal/
│
├─ fe-subject-b/                FE 科目B
│   ├─ README.md
│   ├─ algorithm/   (README.md, questions/)
│   └─ security/    (README.md, questions/)
└─ ap-subject-b/                AP 科目B（記述式）
    ├─ README.md
    ├─ 01_security/
    ├─ 02_network/
    ├─ 03_database/
    ├─ 04_programming/
    └─ 05_project-management/
```

## 初回に作るもの・作らないもの

| 作る | 作らない |
|---|---|
| 大カテゴリ・中カテゴリの README.md（中身は1行の説明だけ） | 小カテゴリ |
| 中カテゴリの空の knowledge.md（パンくずとポイント欄だけ） | 問題ファイル |
| 科目Bのフォルダと README.md（解き方の型は空欄） | |
| formulas.md（見出しだけ） | |
