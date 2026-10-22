"""上流 TanStack/table の docs から React 向けのページだけを取り出し、翻訳前の下ごしらえをする。

usage: python3 -I seed.py <upstream docs dir> <dest docs dir>
"""
import re
import shutil
import sys
from pathlib import Path

SRC = Path(sys.argv[1])
DST = Path(sys.argv[2])
OFFICIAL = 'https://tanstack.com/table/latest/docs/'

INCLUDE = [
    'overview.md', 'installation.md', 'devtools.md', 'agent-skills.md',
    'guide', 'framework/react', 'reference',
]

FRAMEWORK_RE = re.compile(r'<!-- ::start:framework -->\n(.*?)<!-- ::end:framework -->\n?', re.S)
TABS_RE = re.compile(r'<!-- ::start:tabs variant="package-managers" -->\n(.*?)<!-- ::end:tabs -->\n?', re.S)
LINK_RE = re.compile(r'(\]\()([^)\s]+)(\))')


def react_section(m: re.Match) -> str:
    body = m.group(1)
    parts = re.split(r'^# (.+)\n', body, flags=re.M)
    # parts = [pre, name1, body1, name2, body2, ...]
    for name, content in zip(parts[1::2], parts[2::2]):
        if name.strip() == 'React':
            return content.strip('\n') + '\n\n'
    raise ValueError('framework block without React section')


def package_tabs(m: re.Match) -> str:
    pkgs = dict(
        line.split(': ', 1) for line in m.group(1).strip().splitlines() if ': ' in line
    )
    pkg = pkgs['react']
    return (
        '::: code-group\n\n'
        f'```sh [npm]\nnpm install {pkg}\n```\n\n'
        f'```sh [pnpm]\npnpm add {pkg}\n```\n\n'
        f'```sh [yarn]\nyarn add {pkg}\n```\n\n'
        f'```sh [bun]\nbun add {pkg}\n```\n\n'
        ':::\n\n'
    )


def exists(rel_from_docs: str) -> bool:
    p = DST / rel_from_docs
    return p.with_suffix('.md').exists() or p.exists() or (p / 'index.md').exists()


def rewrite_links(text: str, file_rel: Path) -> str:
    """翻訳対象に含まれないページへの相対リンクを公式サイトの URL に置き換える。"""

    def repl(m: re.Match) -> str:
        href = m.group(2)
        if re.match(r'^[a-z]+:|^#|^/', href):
            return m.group(0)
        path, _, frag = href.partition('#')
        if not path:
            return m.group(0)
        resolved = (Path('/') / file_rel.parent / path).resolve()
        rel = str(resolved).lstrip('/')
        rel_noext = re.sub(r'\.md$', '', rel)
        if exists(rel_noext):
            return m.group(0)
        url = OFFICIAL + rel_noext + (f'#{frag}' if frag else '')
        return f'{m.group(1)}{url}{m.group(3)}'

    out = []
    in_code = False
    for line in text.split('\n'):
        if line.lstrip().startswith('```'):
            in_code = not in_code
        out.append(line if in_code else LINK_RE.sub(repl, line))
    return '\n'.join(out)


def main() -> None:
    for item in INCLUDE:
        s = SRC / item
        d = DST / item
        d.parent.mkdir(parents=True, exist_ok=True)
        if s.is_dir():
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)

    for p in DST.rglob('*.md'):
        text = p.read_text(encoding='utf-8')
        text = FRAMEWORK_RE.sub(react_section, text)
        text = TABS_RE.sub(package_tabs, text)
        p.write_text(text, encoding='utf-8')

    # リンク書き換えは全ファイルを配置し終えてから行う（存在判定のため）
    for p in DST.rglob('*.md'):
        rel = p.relative_to(DST)
        text = p.read_text(encoding='utf-8')
        p.write_text(rewrite_links(text, rel), encoding='utf-8')


if __name__ == '__main__':
    main()
