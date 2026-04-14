n = int(input())
mtrx = []
for _ in range(n):
    mtrx.append(input().split())

ans = []
for i in range(n):
    for j in range(n):
        if i >= n - 1 - j:
            ans.append(mtrx[i][j])

print(max(ans))
