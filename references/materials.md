# 手書き風素材サイト（2026-10-31時点・公式サイトと規約で確認した情報）

| サイト | 絵柄・用途 | 無料商用 | 表記 | 形式 | 注意 |
|---|---|---|---|---|---|
| Doodle Icons https://khushmeen.com/icons | 手書き風の小物・記号。400点以上・15カテゴリー。アイコン向き | 可 | 不要 | SVG・PNG・Figma（CC0） | Font Awesomeの手書き版に最も近い |
| ソコスト https://soco-st.com/ | シンプルで柔らかい線画。人物・仕事・生活・建物。日本語で探せる | 可（点数制限なし） | 不要 | SVG・PNG・EPS | 再配布・素材自体の商品化は禁止。AI画像生成の参照画像も禁止 |
| Open Doodles https://www.opendoodles.com/ | ラフなペン描きの人物。動きのあるポーズ | 可 | 不要 | SVG・PNG（CC0） | |
| Open Peeps https://www.openpeeps.com/ | 髪型・服・表情を組み合わせる人物パーツ | 可 | 不要 | SVG・PNG（CC0） | |
| Loose Drawing https://loosedrawing.com/ | ゆるい線画の人物・モノ。日本語検索 | 可 | 不要 | PNG・JPG無料 | SVGは有料 |
| てがきですの！β https://regeld.com/desi/ | 手描き感の強い人物・小物。グラレコ風 | 規約の範囲で可 | 不要 | PNG | ロゴや事業の象徴となるキャラクターへの利用は不可 |

## 使い分け

- 小さなアイコンを同じ絵柄でそろえる → Doodle Icons
- 人物・仕事・生活の挿絵を日本語で探す → ソコスト
- ラフな手描き感のある人物 → Open Doodles（パーツ組み合わせなら Open Peeps）
- スライドに入れるなら **SVG** を選ぶ（拡大してもきれい、CSSで色を変えられる）

## 使う前の確認

規約は変わりうる。使う直前に公式サイトで、商用可否・表記・禁止用途（再配布、AI参照など）を確認する。

## 取得方法

このリポジトリは素材を含まない。`scripts/fetch_assets.py` が、使う人のPCへ配布元から直接取得する。

| サイト | 取り方 |
|---|---|
| Open Doodles | トップのHTMLに直リンクがある。`https://opendoodles.s3-us-west-1.amazonaws.com/<名前>.svg` |
| Doodle Icons | 公式の配布はGumroad（購入手続き・メール入力が要る）かFigma Community。スクリプトは、同じ絵をSVGで収めたnpmパッケージ `doodle-icons`（第三者が作った変換版）から取り出す。パッケージ内のコードは実行しない。**公式でなく第三者経由であり、規約は公式で確認すること** |
| ソコスト | 個別ページ `https://soco-st.com/<ID>` から `https://soco-st.com/wp-content/themes/socost/upload/<ID>_paint.svg`（色つき）または `<ID>_line.svg`（線のみ）。UAを付けて取得する |
| Open Peeps | トップのHTMLに `https://cdn.prod.website-files.com/...peep-N.svg` の直リンクがある |

ブラウザのファイル表示では相対パスの画像が読めないことがある。確認は `python -m http.server` などのローカルサーバー経由で行う。
