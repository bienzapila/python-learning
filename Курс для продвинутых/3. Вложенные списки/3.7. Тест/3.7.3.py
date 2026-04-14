n = int(input())
mtrx = []
for _ in range(n):
    mtrx.append(input().split())

cnt = 0
for i in range(n):
    for j in range(n):
        print(mtrx[j][i], end=" ")
        cnt += 1
        if cnt == n:
            print()
            cnt = 0
