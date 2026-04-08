n = int(input())
mtrx = []
main = []
sec = []

for _ in range(n):
    mtrx.append(input().split())

j = 0
for i in range(len(mtrx)):
    main.append(mtrx[i][j])
    j += 1

j = 0
for i in range(len(mtrx) - 1, -1, -1):
    sec.append(mtrx[i][j])
    mtrx[i][j] = main[j]
    j += 1

j = 0
for i in range(len(mtrx)):
    mtrx[i][j] = sec[i]
    j += 1

for row in mtrx:
    print(*row)
