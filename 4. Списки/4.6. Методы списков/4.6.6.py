n = int(input())
sp = []

for i in range(n):
    sp.append(input())
a = sp.sort()

print(*sp, sep="\n")
