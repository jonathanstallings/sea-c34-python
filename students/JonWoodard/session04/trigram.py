import io

f = io.open("marco-polo.txt", encoding="utf-8")
text_lines = f.readlines()
type(text_lines)
text = "".join(text_lines)
words = text.split()
len(words)
D = {}
for (i, word) in enumerate(words):
    a = word
    b = words[i + 1]
    c = words[i + 2]
    d = 0
    if ((a,b,c) in D(keys)):
        d = D(a,b,c)
        
