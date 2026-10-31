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

## 入れ方

```bash
git clone https://github.com/Sunwood-ai-labs/handdrawn-slides-skill ~/.claude/skills/handdrawn-slides
```

## 使い方

Claude Code に「手書き風スライドを作って」と頼むと、スキルが次の順で進めます。

1. 聞き手と行動を確かめ、各スライドの主張を1文にする
2. `template/` を作業フォルダへコピーして、スライドを書き換える
3. `python scripts/fetch_assets.py <作業フォルダ>` で、使う素材だけを取得する
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
