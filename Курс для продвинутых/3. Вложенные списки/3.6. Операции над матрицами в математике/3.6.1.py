nm = input().split()
n = int(nm[0])
m = int(nm[1])
mtrx1 = []
mtrx2 = []

for i in range(n):
    mtrx1.append(input().split())
input()

for i in range(n):
    mtrx2.append(input().split())

for i in range(n):
    for j in range(m):
        mtrx1[i][j] = int(mtrx1[i][j]) + int(mtrx2[i][j])

for row in mtrx1:
    print(*row)
