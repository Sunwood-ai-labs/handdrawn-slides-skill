# handdrawn-slides-skill

手書き風（ゆれた線・蛍光ペン・手書きフォント）のHTMLスライドを作る、Claude Code 用のスキルです。1枚1メッセージの単一HTMLに仕上げ、そのまま画像やPDFにできます。

## このリポジトリに素材は入っていません

イラストやアイコンの SVG は**含めていません**。再配布にならないよう、`scripts/fetch_assets.py` が、使う人のPCへ配布元から直接取得します。

| 用途 | 素材 | 配布元 |
|---|---|---|
| アイコン | Doodle Icons | https://khushmeen.com/icons |
| 人物・イラスト | Open Doodles | https://www.opendoodles.com/ |

使う前に、各サイトの規約（商用可否・表記・禁止用途）を自分で確認してください。

Doodle Icons の公式配布は Gumroad か Figma（購入手続き・メール入力が要る）です。スクリプトは、同じ絵を SVG で収めた npm パッケージ `doodle-icons`（第三者が作った変換版）から取り出します。公式経由ではない点に注意してください。

## CLIだけで最初から最後まで

Python 3 と git があれば、コマンドだけで通せます。

```bash
# 1. スキルを入れる
git clone https://github.com/Sunwood-ai-labs/handdrawn-slides-skill ~/.claude/skills/handdrawn-slides

# 2. テンプレートを作業フォルダへコピーする
cp -r ~/.claude/skills/handdrawn-slides/template my-slides

# 3. 素材を配布元から取得する（index.html が使っている素材だけ）
python ~/.claude/skills/handdrawn-slides/scripts/fetch_assets.py my-slides

# 4. ブラウザで確認する（file:// だと画像が読めないことがあるのでサーバー経由）
cd my-slides && python -m http.server 8000
# http://localhost:8000/ を開く（← → で移動、F で全画面）
```

Windows の PowerShell では、2 は `Copy-Item -Recurse $HOME\.claude\skills\handdrawn-slides	emplate my-slides` です。

### 素材を名前で選ぶ

スライドに新しい絵を使いたいときは、名前を調べて取得します。

```bash
python scripts/fetch_assets.py --list-icons      # Doodle Icons の名前一覧（440点）
python scripts/fetch_assets.py --list-doodles    # Open Doodles の名前一覧
python scripts/fetch_assets.py my-slides --icon Rocket --icon Heart --doodle sleek
python scripts/fetch_assets.py my-slides --all-icons   # Doodle Icons を全件取得
```

HTML には `<img src="assets/doodle-icons/Rocket.svg">` や `<img src="assets/open-doodles/sleek.svg">` のように書くと、名前を指定しなくても、次の実行で自動で取得されます。

### 画像（PNG）にする

Chrome があれば、コマンドで1枚ずつ撮れます（右下の操作ヒントは先に消しておく）。

```bash
chrome --headless=new --window-size=1600,900 --virtual-time-budget=6000   --screenshot=slide01.png "file:///.../my-slides/index.html#1"
```

## 使い方（Claude Code から）

Claude Code に「手書き風スライドを作って」と頼むと、スキルが次の順で進めます。

1. 聞き手と行動を確かめ、各スライドの主張を1文にする
2. `template/` を作業フォルダへコピーして、スライドを書き換える
3. `fetch_assets.py` で、使う素材だけを取得する
4. ローカルサーバー経由でブラウザで確認する

## 中身

| パス | 内容 |
|---|---|
| `SKILL.md` | スキル本体（手順・守ること） |
| `template/index.html` | 14枚のテンプレート（素材は取得後に表示される） |
| `scripts/fetch_assets.py` | 素材の取得スクリプト（標準ライブラリのみ） |
| `references/materials.md` | 手書き風素材サイトの一覧と取得方法 |

## ライセンス

このリポジトリのファイル（スキルの文章、テンプレート、スクリプト）は MIT です。取得した素材には含まれず、素材はそれぞれの配布元の規約に従います。
