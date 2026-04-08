n, m = int(input()), int(input())
mtrx = []
mx = -99999999999

for _ in range(n):
    mtrx.append(input().split())

for i in range(n):
    for j in range(m):
        if int(mtrx[i][j]) > mx:
            mx = int(mtrx[i][j])

flag = False
for i in range(n):
    for j in range(m):
        if int(mtrx[i][j]) == mx:
            print(i, j)
            flag = True
            break
    if flag:
        break
