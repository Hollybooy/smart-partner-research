"""Sanity-check index.html: HTML tag balance and DATA percentage sums."""

import io
import os
import re
from html.parser import HTMLParser

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
html = io.open(os.path.join(root, 'index.html'), encoding='utf-8').read()

VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input',
        'link', 'meta', 'param', 'source', 'track', 'wbr'}


class Checker(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack:
            self.errors.append('stray </%s>' % tag)
        elif self.stack[-1] == tag:
            self.stack.pop()
        elif tag in self.stack:
            while self.stack and self.stack[-1] != tag:
                self.errors.append('unclosed <%s>' % self.stack.pop())
            if self.stack:
                self.stack.pop()
        else:
            self.errors.append('no opener for </%s>' % tag)


c = Checker()
c.feed(html)
print('=== HTML tag balance ===')
print('tag errors :', c.errors or 'none')
print('unclosed   :', c.stack or 'none')

print('\n=== DATA percentage sums ===')
for name in ('donut', 'freqBars'):
    m = re.search(name + r':\s*\[(.*?)\n    \]', html, re.S)
    vals = [int(x) for x in re.findall(r'pct:\s*(\d+)', m.group(1))] if m else []
    print('  %-10s %-30s sum = %d' % (name, vals, sum(vals)))

print('\n=== Structure ===')
print('  cards      :', len(re.findall(r'<section class="card"', html)))
print('  num badges :', re.findall(r'class="num">(\d)<', html))
print('  placeholders left:', html.count("'—'"))
