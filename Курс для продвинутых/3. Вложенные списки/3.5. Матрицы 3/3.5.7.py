nm = input().split()
n = int(nm[0])
m = int(nm[1])
mtrx = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        k = (i + j) // m
        mtrx[i][j] = i + j + 1 - k * m


for row in mtrx:
    print(*row)
