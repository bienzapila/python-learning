nm = input().split()
n, m = int(nm[0]), int(nm[1])
mtrx = [[0] *  m for _ in range(n)]

k = 0
i = 0
j = 0
while k < n * m:
    i