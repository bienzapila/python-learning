n = int(input())
mtrx = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            mtrx[i][j] = 1

j = 0
for i in range(n - 1, -1, -1):
    mtrx[i][j] = 1
    j += 1

for row in mtrx:
    print(*row)
