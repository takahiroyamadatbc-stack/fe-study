#!/usr/bin/env bash
# リンク切れ・ルール違反のチェック（CLAUDE.md §7, §8）
# 使い方: リポジトリのルートで `bash _templates/check_links.sh`
# _templates/ 配下はサンプルのリンクを含むため対象外。
set -u
cd "$(dirname "$0")/.."

python3 - <<'PY'
import pathlib, re, sys

root = pathlib.Path(".").resolve()
errors = []
link_re = re.compile(r'\[([^\]]*)\]\(([^)\s]+)\)')

for md in sorted(root.rglob("*.md")):
    rel = md.relative_to(root)
    if rel.parts[0] in (".git", "_templates"):
        continue
    text = md.read_text(encoding="utf-8")
    # コードブロック・インラインコード・HTMLコメント内の例は除外する
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"`[^`\n]*`", "", text)

    # パンくず（ルートの README.md と CLAUDE.md 以外は1行目が [目次](...) で始まること）
    if str(rel) not in ("README.md", "CLAUDE.md"):
        first = md.read_text(encoding="utf-8").lstrip().splitlines()[0] if md.stat().st_size else ""
        if not first.startswith("[目次]("):
            errors.append(f"{rel}: 1行目にパンくずがありません")

    for label, target in link_re.findall(text):
        if re.match(r"^(https?:|mailto:)", target):
            if "github.com" in target:
                errors.append(f"{rel}: GitHub の URL ではなく相対パスで書いてください → {target}")
            continue
        if target.startswith("/"):
            errors.append(f"{rel}: 絶対パスは使えません → {target}")
            continue
        if "#" in target:
            errors.append(f"{rel}: アンカーリンク（#）は使えません → {target}")
            target = target.split("#")[0]
            if not target:
                continue
        dest = (md.parent / target).resolve()
        if not dest.exists():
            errors.append(f"{rel}: リンク切れ → {target}")

if errors:
    print("\n".join(errors))
    print(f"\nエラー: {len(errors)} 件")
    sys.exit(1)
print("OK: リンク切れ・ルール違反はありません")
PY
