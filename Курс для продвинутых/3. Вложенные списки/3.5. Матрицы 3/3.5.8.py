nm = input().split()
n = int(nm[0])
m = int(nm[1])
mtrx = [[0] * m for _ in range(n)]

for i in range(n):
    if i == 0:
        mtrx[0] = [k for k in range(1, m + 1)]
    elif i % 2 == 0:
        mtrx[i] = [k for k in range(mtrx[i - 1][0] + 1, mtrx[i - 1][0] + m + 1)]
    else:
        mtrx[i] = [
            k for k in range(mtrx[i - 1][m - 2] + m + 1, mtrx[i - 1][m - 2] + 1, -1)
        ]


for row in mtrx:
    print(*row)
