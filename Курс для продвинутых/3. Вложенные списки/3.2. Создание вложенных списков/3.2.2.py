n = int(input())
sp = []

for i in range(n):
    sp.append([i + 1 for i in range(i + 1)])

print(*sp, sep="\n")
