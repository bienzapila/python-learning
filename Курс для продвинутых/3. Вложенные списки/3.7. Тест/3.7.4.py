n = int(input())
mtrx = [["."] * n for _ in range(n)]

c = 0
for i in range(n):
    mtrx[i][c] = "*"
    c += 1

c = 0
for i in range(len(mtrx) - 1, -1, -1):
    mtrx[i][c] = "*"
    c += 1

i = len(mtrx) // 2
for c in range(len(mtrx)):
    mtrx[i][c] = "*"

c = len(mtrx) // 2
for i in range(len(mtrx)):
    mtrx[i][c] = "*"

for row in mtrx:
    print(*row)
