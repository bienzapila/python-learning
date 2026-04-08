n = int(input())
sp = []

for i in range(n):
    s = int(input())
    sp.append(s)

mi = min(sp)
ma = max(sp)

for i in range(len(sp)):
    if sp[i] == mi:
        mini = i
    elif sp[i] == ma:
        maxim = i

del sp[mini]

if mini < maxim:
    del sp[maxim - 1]
if mini > maxim:
    del sp[maxim]

print(*sp, sep="\n")
