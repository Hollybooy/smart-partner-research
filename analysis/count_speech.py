"""Count the spoken words of the script in SPEECH.md and estimate its duration."""

import io
import os
import re

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
text = io.open(os.path.join(root, 'SPEECH.md'), encoding='utf-8').read()
body = text.split('## The script')[1].split('## Delivery notes')[0]

body = re.sub(r'\*\*\[.*?\]\*\*', '', body)   # [0:00 - 0:20] Title  headings
body = re.sub(r'\(\s*beat[^)]*\)', '', body)  # (beat) / (slow down ...) cues
body = re.sub(r'\*\*', '', body)              # bold markers
body = re.sub(r'`', '', body)                 # inline code markers
body = re.sub(r'---', '', body)               # horizontal rules

words = [w for w in body.split() if re.search(r'[A-Za-z0-9]', w)]
n = len(words)

print('spoken words ~', n)
for wpm in (130, 140, 150):
    print('  at %d wpm -> %.2f min' % (wpm, n / wpm))
