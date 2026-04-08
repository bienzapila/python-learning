n = int(input())
mtrx1 = []
for i in range(n):
    mtrx1.append(input().split())
mtrx2 = mtrx1.copy()
mtrx3 = [[0] * n for _ in range(n)]
k = int(input())
for _ in range(k - 1):
    for i in range(n):
        for j in range(n):
            summa = 0
            c = 0
            for r in range(n):
                summa += int(mtrx1[i][r]) * int(mtrx2[c][j])
                c += 1
            mtrx3[i][j] = summa
    mtrx1 = mtrx3.copy()
    if _ != k - 2:
        mtrx3 = [[0] * n for _ in range(n)]

for row in mtrx3:
    print(*row)
