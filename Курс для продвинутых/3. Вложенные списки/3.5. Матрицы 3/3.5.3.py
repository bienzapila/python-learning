nm = input().split()
n, m = int(nm[0]), int(nm[1])
mtrx = []

lst = [k for k in range(1, n * m + 1)]

l = 0
for i in range(n):
    a = []
    for j in range(m):
        a.append(lst[l])
        l += 1
    mtrx.append(a)

for row in mtrx:
    print(*row)
