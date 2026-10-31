#!/usr/bin/env python3
"""手書き風スライドが使う素材（SVG）を、配布元から使う人のPCへ取得する。

このリポジトリは素材を含まない。再配布を避けるため、素材は実行した人が
それぞれの配布元から直接取得する。使う前に各サイトの規約を確認すること。

使い方:
  python scripts/fetch_assets.py <作業フォルダ>

<作業フォルダ>の *.html が参照している assets/doodle-icons/<名前>.svg と
assets/open-doodles/<名前>.svg だけを取得し、<作業フォルダ>/assets/ に置く。
  --all-icons  Doodle Icons を全件（約440点）取得する

標準ライブラリのみ。取得したパッケージ内のコードは実行しない（文字として読むだけ）。
"""
import argparse
import io
import re
import sys
import tarfile
import urllib.request
from pathlib import Path

OPEN_DOODLES_URL = 'https://opendoodles.s3-us-west-1.amazonaws.com/%s.svg'
# Doodle Icons の公式配布は Gumroad / Figma（メール入力や購入手続きが要る）。
# ここでは、その絵を SVG のまま収めている npm パッケージから取り出す。
DOODLE_ICONS_TGZ = 'https://registry.npmjs.org/doodle-icons/-/doodle-icons-1.1.0.tgz'
UA = {'User-Agent': 'Mozilla/5.0 (handdrawn-slides-skill fetch_assets.py)'}

REF = re.compile(r'assets/(doodle-icons|open-doodles)/([A-Za-z0-9_-]+)\.svg')


def get(url, timeout=60):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def referenced(folder):
    found = {'doodle-icons': set(), 'open-doodles': set()}
    for html in Path(folder).glob('*.html'):
        for kind, name in REF.findall(html.read_text(encoding='utf-8')):
            found[kind].add(name)
    return found


def extract_doodle_icons(wanted):
    """npm tarball の index.es.js から、アイコンのSVGを文字列として取り出す。"""
    print('Doodle Icons を npm から取得中 ...')
    data = get(DOODLE_ICONS_TGZ, timeout=120)
    with tarfile.open(fileobj=io.BytesIO(data), mode='r:gz') as tar:
        member = tar.extractfile('package/build/index.es.js')
        src = member.read().decode('utf-8')
    icons = {}
    for chunk in re.split(r'(?=var Svg\w+ = function)', src):
        m = re.match(r'var Svg(\w+) = function', chunk)
        if not m:
            continue
        end = chunk.find('\nvar ', 5)
        body = chunk if end < 0 else chunk[:end]
        body = re.sub(r'jsx\("defs".*', '', body, flags=re.S)  # clipPath の白い矩形を除く
        vb = re.search(r'viewBox: "([^"]+)"', body)
        paths = []
        for attrs in re.findall(r'jsx\("path", \{ ([^}]*)\}', body):
            d = re.search(r'd: "([^"]+)"', attrs)
            if not d or d.group(1).startswith('M0 0h'):
                continue
            fill = re.search(r'fill: "([^"]+)"', attrs)
            tr = re.search(r'transform: "([^"]+)"', attrs)
            paths.append('<path d="%s"%s%s/>' % (
                d.group(1),
                ' fill="%s"' % fill.group(1) if fill else '',
                ' transform="%s"' % tr.group(1) if tr else ''))
        if vb and paths:
            icons[m.group(1)] = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="%s">%s</svg>'
                                 % (vb.group(1), ''.join(paths)))
    if wanted is not None:
        missing = sorted(set(wanted) - set(icons))
        if missing:
            print('  見つからないアイコン:', ', '.join(missing), file=sys.stderr)
        icons = {k: v for k, v in icons.items() if k in wanted}
    return icons


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('folder', help='index.html のある作業フォルダ')
    ap.add_argument('--all-icons', action='store_true', help='Doodle Icons を全件取得する')
    args = ap.parse_args()

    folder = Path(args.folder)
    found = referenced(folder)
    out = folder / 'assets'

    names = sorted(found['open-doodles'])
    if names:
        (out / 'open-doodles').mkdir(parents=True, exist_ok=True)
    for n in names:
        try:
            (out / 'open-doodles' / (n + '.svg')).write_bytes(get(OPEN_DOODLES_URL % n))
            print('Open Doodles:', n)
        except Exception as e:  # noqa: BLE001
            print('  取得失敗 %s: %s' % (n, e), file=sys.stderr)

    if found['doodle-icons'] or args.all_icons:
        icons = extract_doodle_icons(None if args.all_icons else found['doodle-icons'])
        (out / 'doodle-icons').mkdir(parents=True, exist_ok=True)
        for n, svg in sorted(icons.items()):
            (out / 'doodle-icons' / (n + '.svg')).write_text(svg, encoding='utf-8')
        print('Doodle Icons: %d 点' % len(icons))

    print('完了。素材は %s にあります。各素材の規約は配布元で確認してください。' % out)


if __name__ == '__main__':
    main()
