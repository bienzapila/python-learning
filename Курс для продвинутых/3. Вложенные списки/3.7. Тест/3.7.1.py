s = input().split()
n = int(input())
ans = []
for i in range(1, n + 1):
    ap = []
    for p in range(i - 1, len(s), n):
        ap.append(s[p])
    ans.append(ap)

print(ans)
