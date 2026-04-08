nm = input().split()
n = int(nm[0])
m = int(nm[1])
mtrx1 = []
for i in range(n):
    mtrx1.append(input().split())
input()

mk = input().split()
m = int(mk[0])
k = int(mk[1])
mtrx2 = []
for i in range(m):
    mtrx2.append(input().split())

mtrx3 = [[0] * k for _ in range(n)]

for i in range(n):
    for j in range(k):
        summa = 0
        c = 0
        for r in range(m):
            summa += int(mtrx1[i][r]) * int(mtrx2[c][j])
            c += 1
        mtrx3[i][j] = summa


for row in mtrx3:
    print(*row)
