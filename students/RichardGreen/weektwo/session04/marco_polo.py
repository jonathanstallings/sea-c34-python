# marco_polo.py

import io
f = io.open("marco-polo.txt", encoding="utf-8")
dir(f)
text_lines = f.readlines()
text = "".join(text_lines)
words = text.split()
D = {}
for (i, word) in enumerate(words):
    a = word
    b = words[i + 1]
    c = words[i + 2]
    d = 0
    if((a,b,c)) in D .keys()):
        d=
