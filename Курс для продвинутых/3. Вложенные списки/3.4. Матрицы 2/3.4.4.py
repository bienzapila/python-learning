n = int(input())
mtrx = []

for _ in range(n):
    mtrx.append(input().split())

flag = False
for i in range(len(mtrx)):
    for j in range(len(mtrx[0])):
        if mtrx[i][j] != mtrx[j][i]:
            print("NO")
            flag = True
            break
    if flag:
        break

if not flag:
    print("YES")
