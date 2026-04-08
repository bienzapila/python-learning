n = int(input())
mtrx = []

for i in range(n):
    a = []
    for j in range(n):
        a.append(0)
    mtrx.append(a)
    a = []

j = 0
for i in range(len(mtrx) - 1, -1, -1):
    mtrx[i][j] = 1
    j += 1

for i in range(n):
    for j in range(n):
        if i > n - 1 - j:
            mtrx[i][j] = 2

for row in mtrx:
    print(*row)
