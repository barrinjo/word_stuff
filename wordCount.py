import re
from collections import Counter

f = open("wanderingGhosts.txt", "r")
if f.mode == 'r':
    inside = f.read()
    length = f.read()

lines = 0
for x in inside:
    if x == '\n':
        lines = lines + 1

for x in ':?;!\".,-\n\ufeff':
    inside = inside.replace(x, ' ')
inside = re.split(" ", inside)
inside = [x for x in inside if x != ""]
print(inside)

lib = {}
for x in inside:
    lib[x] = True

c = Counter(inside)
print(lib.keys())
for word, count in c.most_common():
    print(word, "appears", count, "times.")

print(lines, "lines")
print(len(inside), "words")
print()
