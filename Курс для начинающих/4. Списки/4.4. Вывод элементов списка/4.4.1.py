n = int(input())
neg = []
zer = []
pos = []

for i in range(n):
    s = int(input())
    if s < 0:
        neg.append(s)
    elif s > 0:
        pos.append(s)
    else:
        zer.append(s)

print(*neg, *zer, *pos, sep="\n")
