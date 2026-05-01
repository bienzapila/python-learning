n = int(input())
ans = {}
for _ in range(n):
    s = input().split()
    ans[s[0]] = s[1]
    ans[s[1]] = s[0]

print(ans[input()])
