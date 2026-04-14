n = int(input())
mtrx = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        mtrx[i][j] = abs(i - j)

for row in mtrx:
    print(*row)
