nm = input().split()
n, m = int(nm[0]), int(nm[1])
mtrx = [[0] * m for _ in range(n)]

lst = [k for k in range(1, n * m + 1)]

l = 0
for j in range(m):
    for i in range(n):
        mtrx[i][j] = lst[l]
        l += 1

for row in mtrx:
    print(*row)
