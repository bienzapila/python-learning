ans = {}
s = input().split()
for c in s:
    if c not in ans:
        ans[c] = 1
        print(ans[c], end=" ")
    else:
        ans[c] += 1
        print(ans[c], end=" ")
