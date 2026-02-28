#!/usr/bin/env python3
"""
Include processor for DEV.to markdown files.
Replaces :(path/to/file.ext) and :(path/to/file.ext lang=LANG) with code blocks.

Usage:
  python scripts/include_processor.py posts/my-article/article.md [file2.md ...]
  Or set FILES environment variable (newline-separated paths):
    export FILES="posts/my-article/article.md"
    python scripts/include_processor.py

Output goes to processed_posts/ by default (configurable via OUT_DIR env var).
When run inside GitHub Actions, writes PROCESSED_FILES output for publish step.
"""
import os
import re
import sys

LANG_MAP = {
    '.ps1': 'powershell', '.sh': 'bash', '.js': 'javascript',
    '.ts': 'typescript', '.py': 'python', '.json': 'json',
    '.html': 'html', '.css': 'css', '.sql': 'sql',
    '.yml': 'yaml', '.yaml': 'yaml', '.xml': 'xml', '.md': 'markdown',
}

PATTERN = re.compile(r':\(\s*([^\s\)]+)(?:\s+lang=([^\)\s]+))?\s*\)')


def process_file(md_path, out_dir):
    if not os.path.exists(md_path):
        print(f'Skip missing: {md_path}')
        return None

    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    def repl(m):
        rel = m.group(1)
        lang = m.group(2)
        base = os.path.dirname(md_path)
        abs_path = rel if os.path.isabs(rel) else os.path.normpath(os.path.join(base, rel))
        if not os.path.exists(abs_path):
            print(f'Included file not found: {abs_path}')
            return m.group(0)
        ext = os.path.splitext(abs_path)[1].lower()
        if not lang:
            lang = LANG_MAP.get(ext, 'text')
        with open(abs_path, 'r', encoding='utf-8') as inc:
            code = inc.read().rstrip()
        return f'```{lang}\n{code}\n```'

    processed = PATTERN.sub(repl, content)
    rel = os.path.relpath(md_path)
    out_path = os.path.join(out_dir, rel)
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(processed)
    print(f'Wrote processed file: {out_path}')
    return out_path


def main():
    if len(sys.argv) > 1:
        files = sys.argv[1:]
    else:
        env_files = os.environ.get('FILES', '').strip()
        files = [f.strip() for f in env_files.splitlines() if f.strip()]

    if not files:
        print('No files to process')
        sys.exit(0)

    out_dir = os.environ.get('OUT_DIR', 'processed_posts')
    os.makedirs(out_dir, exist_ok=True)

    processed = []
    for md in files:
        result = process_file(md, out_dir)
        if result:
            processed.append(result)

    gh_out = os.environ.get('GITHUB_OUTPUT')
    if gh_out and processed:
        with open(gh_out, 'a', encoding='utf-8') as out:
            out.write('PROCESSED_FILES<<EOF\n')
            out.write('\n'.join(processed))
            out.write('\nEOF\n')


if __name__ == '__main__':
    main()
