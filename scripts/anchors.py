"""見出しに英語のアンカー {#slug} を付け、翻訳後もページ内リンクが切れないようにする。

slug は上流サイト（rehype-slug = github-slugger）と同じ規則で作る。
usage: python3 -I anchors.py <file.md>...
"""
import re
import sys

HEADING_RE = re.compile(r'^(#{1,6})\s+(.*?)\s*$')


def slugify(text: str) -> str:
    text = re.sub(r'`([^`]*)`', r'\1', text)
    text = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', text)
    text = re.sub(r'[*_]{1,3}([^*_]+)[*_]{1,3}', r'\1', text)
    text = text.replace('\\', '')
    text = text.lower()
    text = re.sub(r'[^\w\- ]', '', text)
    return text.replace(' ', '-')


def process(text: str) -> str:
    out, seen, in_code = [], {}, False
    for line in text.split('\n'):
        if line.lstrip().startswith('```'):
            in_code = not in_code
        m = None if in_code else HEADING_RE.match(line)
        if m and not re.search(r'\{#[^}]+\}\s*$', line):
            base = slugify(m.group(2))
            n = seen.get(base, 0)
            seen[base] = n + 1
            slug = base if n == 0 else f'{base}-{n}'
            line = f'{m.group(1)} {m.group(2)} {{#{slug}}}'
        out.append(line)
    return '\n'.join(out)


if __name__ == '__main__':
    for path in sys.argv[1:]:
        with open(path, encoding='utf-8') as f:
            src = f.read()
        # frontmatter は見出しとして扱わない
        fm = re.match(r'^---\n.*?\n---\n', src, re.S)
        head, body = (fm.group(0), src[fm.end():]) if fm else ('', src)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(head + process(body))
