nm = input().split()
n = int(nm[0])
m = int(nm[1])
mtrx = [[0] * m for _ in range(n)]

cnt = 1
for l in range(n + m - 1):
    for i in range(n):
        for j in range(m):
            if i + j == l:
                mtrx[i][j] = cnt
                cnt += 1

for row in mtrx:
    print(*row)
