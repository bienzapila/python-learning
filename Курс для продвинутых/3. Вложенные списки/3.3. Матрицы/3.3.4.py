n = int(input())
mtrx = []

for _ in range(n):
    mtrx.append(input().split())

mx = -10000000
for i in range(len(mtrx)):
    for j in range(len(mtrx[0])):
        if i >= j and int(mtrx[i][j]) > mx:
            mx = int(mtrx[i][j])

print(mx)
