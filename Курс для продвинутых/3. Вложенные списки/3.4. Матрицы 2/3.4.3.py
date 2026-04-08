n, m = int(input()), int(input())
mtrx = []

for i in range(n):
    mtrx.append(input().split())

n1m1 = input().split()
n1, m1 = int(n1m1[0]), int(n1m1[1])

for i in range(len(mtrx)):
    mtrx[i][n1], mtrx[i][m1] = mtrx[i][m1], mtrx[i][n1]

for row in mtrx:
    print(*row)
