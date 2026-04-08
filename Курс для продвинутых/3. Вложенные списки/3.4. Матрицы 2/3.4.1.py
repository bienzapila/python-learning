n, m = int(input()), int(input())
mtrx = []

for i in range(n):
    row = []
    for j in range(m):
        row.append(i * j)
    mtrx.append(row)

for i in range(n):
    for j in range(m):
        print(str(mtrx[i][j]).ljust(2), end=" ")
    print()
