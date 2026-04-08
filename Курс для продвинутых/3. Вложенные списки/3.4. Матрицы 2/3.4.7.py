n = int(input())
mtrx = []

for _ in range(n):
    mtrx.append(input().split())

nmtrx = []
new = []
for j in range(len(mtrx[0])):
    for i in range(len(mtrx)):
        new.append(mtrx[i][j])
    new.reverse()
    nmtrx.append(new)
    new = []

for row in nmtrx:
    print(*row)
