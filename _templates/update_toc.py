#!/usr/bin/env python3
"""目次（/README.md）の「最終更新」「記録」列を自動で更新する（CLAUDE.md §8）。

使い方: リポジトリのルートで `python3 _templates/update_toc.py`

- 最終更新: その中カテゴリで（YY-MM-DD 形式）、問題・知識を最後に追加・変更した日（日本時間）。
  - README.md だけの変更（統計の更新など）は数えない。
  - 「構造:」で始まるコミット（構成の変更）は数えない。
  - まだコミットしていない変更があれば、今日の日付にする。
  - 一度も更新がなければ「-」。
- 記録: その中カテゴリ配下の questions/*.md の数。
"""
import datetime
import os
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
os.chdir(ROOT)
ENV = dict(os.environ, TZ="Asia/Tokyo")
TODAY = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).strftime("%y-%m-%d")


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True, env=ENV, check=True).stdout


def pathspec(d):
    # README.md（統計・一覧）は除外し、知識と問題の変更だけを見る
    return ["--", d, f":(exclude,glob){d}/**/README.md"]


def last_update(d):
    if git("status", "--porcelain", *pathspec(d)).strip():
        return TODAY
    out = git("log", "-1", "--date=format-local:%y-%m-%d", "--format=%ad",
              "--invert-grep", "--grep=^構造:", *pathspec(d)).strip()
    return out or "-"


readme = ROOT / "README.md"
text = readme.read_text(encoding="utf-8")
row = re.compile(r"^\| (\[[^\]]+\]\(([0-9]_[^/]+/[0-9]{2}_[^/]+)/README\.md\)) \| [^|]* \| [^|]* \|$", re.M)


def repl(m):
    link, d = m.group(1), m.group(2)
    count = len(list((ROOT / d).glob("**/questions/*.md")))
    return f"| {link} | {last_update(d)} | {count} |"


new, n = row.subn(repl, text)
if n != 23:
    raise SystemExit(f"中カテゴリの行が23行見つかりません（{n}行）。README.md の表の形式を確認してください")
if new != text:
    readme.write_text(new, encoding="utf-8")
    print(f"README.md を更新しました（{n}行）")
else:
    print("README.md は最新です")
