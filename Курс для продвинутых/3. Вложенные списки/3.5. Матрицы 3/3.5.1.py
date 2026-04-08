nm = input().split()
n = int(nm[0])
m = int(nm[1])

mtrx = []

a = []
for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            if j % 2 == 0:
                a.append(".")
            else:
                a.append("*")
    else:
        for j in range(m):
            if j % 2 == 0:
                a.append("*")
            else:
                a.append(".")
    mtrx.append(a)
    a = []

for row in mtrx:
    print(*row)
