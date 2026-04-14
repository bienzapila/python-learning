n = int(input())
mtrx = []
for _ in range(n):
    mtrx.append(input().split())

flag = False
for i in range(n):
    for j in range(n):
        if i < n - 1 - j:
            if mtrx[i][j] != mtrx[n - j - 1][n - i - 1]:
                flag = True
                break
    if flag:
        print("NO")
        break
    else:
        continue
else:
    print("YES")
