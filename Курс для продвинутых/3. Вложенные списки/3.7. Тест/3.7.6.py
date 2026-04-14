n = int(input())
mtrx = []
for _ in range(n):
    mtrx.append(input().split())
st = set([str(i) for i in range(1, n + 1)])

flag = False
for i in range(n):
    if set(mtrx[i]) == st:
        continue
    else:
        print("NO")
        flag = True
        break

if not flag:
    ans = []
    for j in range(n):
        for i in range(n):
            ans.append(mtrx[i][j])
        if st == set(ans):
            continue
        else:
            print("NO")
            break
    else:
        print("YES")
