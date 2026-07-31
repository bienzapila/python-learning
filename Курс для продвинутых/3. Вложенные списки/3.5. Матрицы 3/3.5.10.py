nm = input().split()
n, m = int(nm[0]), int(nm[1])
mtrx = [[0] *  m for _ in range(n)]

count = 1
ia = n - 1
ja = m - 1
i = 0
j = 0
if n == 1:
    for _ in range(m):
        mtrx[i][j] = count
        j += 1
        count += 1
elif m == 1:
    for _ in range(n):
        mtrx[i][j] = count
        i += 1
        count += 1
elif min(n, m) % 2 == 0:
    for _ in range(min(n, m) // 2):
        for _ in range(ja):
            mtrx[i][j] = count
            j += 1
            count += 1
        for _ in range(ia):
            mtrx[i][j] = count
            i += 1
            count += 1
        for _ in range(ja):
            mtrx[i][j] = count
            j -= 1
            count += 1
        for _ in range(ia):
            mtrx[i][j] = count
            i -= 1
            count += 1
        j += 1
        i += 1
        ia -= 2
        ja -= 2
else:
    for _ in range(min(n, m) // 2):
        for _ in range(ja):
            mtrx[i][j] = count
            j += 1
            count += 1
        for _ in range(ia):
            mtrx[i][j] = count
            i += 1
            count += 1
        for _ in range(ja):
            mtrx[i][j] = count
            j -= 1
            count += 1
        for _ in range(ia):
            mtrx[i][j] = count
            i -= 1
            count += 1
        j += 1
        i += 1
        ia -= 2
        ja -= 2
    for _ in range(ja + 1):
        mtrx[i][j] = count
        j += 1
        count += 1

for row in mtrx:
    print(*row)