n = int(input())
ans = set()
for _ in range(n):
    s = input().lower()
    for i in range(len(s)):
        ans.add(s[i])

print(len(ans))
