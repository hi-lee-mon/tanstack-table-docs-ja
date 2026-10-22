"""訳文を原文と突き合わせ、翻訳で壊してはいけない部分が変わっていないか調べる。

調べるもの: コードブロック、リンク先、見出しアンカー、frontmatter の title 以外のキー、
英文が残っていないか（段落単位の目安）。
usage: python3 -I verify.py <orig docs dir> <translated docs dir> <rel path>...
"""
import re
import sys
from pathlib import Path

FENCE_RE = re.compile(r'^(\s*)(```+|~~~+).*?^\1\2\s*$', re.M | re.S)
LINK_RE = re.compile(r'\]\(([^)\s]+)')
ANCHOR_RE = re.compile(r'\{#([^}]+)\}\s*$', re.M)
FM_RE = re.compile(r'^---\n(.*?)\n---\n', re.S)


def code_blocks(s: str) -> list[str]:
    return [m.group(0) for m in FENCE_RE.finditer(s)]


def strip_code(s: str) -> str:
    s = FENCE_RE.sub('', s)
    return re.sub(r'`[^`\n]*`', '', s)


def fm_keys(s: str) -> dict[str, str]:
    m = FM_RE.match(s)
    if not m:
        return {}
    out = {}
    for line in m.group(1).splitlines():
        k, _, v = line.partition(':')
        out[k.strip()] = v.strip()
    return out


def english_leftovers(s: str) -> list[str]:
    body = strip_code(FM_RE.sub('', s))
    hits = []
    for para in re.split(r'\n\s*\n', body):
        text = re.sub(r'\]\([^)]*\)|\{#[^}]+\}|<[^>]+>|https?://\S+', '', para)
        words = re.findall(r'[A-Za-z]{3,}', text)
        has_ja = re.search(r'[぀-ヿ一-鿿]', text)
        if len(words) >= 8 and not has_ja:
            hits.append(para.strip()[:80])
    return hits


def check(orig: str, tr: str) -> list[str]:
    errs = []
    oc, tc = code_blocks(orig), code_blocks(tr)
    if oc != tc:
        errs.append(f'code blocks differ ({len(oc)} -> {len(tc)})')
    ol, tl = sorted(LINK_RE.findall(strip_code(orig))), sorted(LINK_RE.findall(strip_code(tr)))
    if ol != tl:
        missing = sorted(set(ol) - set(tl))
        extra = sorted(set(tl) - set(ol))
        errs.append(f'links differ missing={missing[:5]} extra={extra[:5]}')
    if ANCHOR_RE.findall(orig) != ANCHOR_RE.findall(tr):
        errs.append('heading anchors differ')
    ofm, tfm = fm_keys(orig), fm_keys(tr)
    for k in ofm:
        if k not in tfm:
            errs.append(f'frontmatter key missing: {k}')
        elif k != 'title' and ofm[k] != tfm[k]:
            errs.append(f'frontmatter {k} changed')
    for para in english_leftovers(tr):
        errs.append(f'untranslated? {para!r}')
    return errs


if __name__ == '__main__':
    orig_dir, tr_dir, *rels = sys.argv[1:]
    bad = 0
    for rel in rels:
        o = (Path(orig_dir) / rel).read_text(encoding='utf-8')
        t = (Path(tr_dir) / rel).read_text(encoding='utf-8')
        errs = check(o, t)
        if errs:
            bad += 1
            print(f'NG {rel}')
            for e in errs:
                print(f'   - {e}')
        else:
            print(f'OK {rel}')
    sys.exit(1 if bad else 0)
