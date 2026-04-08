n = int(input())
mtrx = []

for _ in range(n):
    mtrx.append(input().split())

j = n - 1
for i in range(n // 2):
    mtrx[i], mtrx[j] = mtrx[j], mtrx[i]
    j -= 1

for row in mtrx:
    print(*row)
