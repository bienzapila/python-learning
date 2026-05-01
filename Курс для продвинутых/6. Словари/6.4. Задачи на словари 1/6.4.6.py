n = int(input())
l = []
ans = {}

for _ in range(n):
    s = input()
    for i in range(len(s)):
        if s[i] == " ":
            k = i
            break
    l.append([s[k + 1 :], s[:k]])

for r in range(len(l)):
    if l[r][0] in ans and isinstance(ans[l[r][0]], str):
        ans[l[r][0]] = [ans[l[r][0]]]
        ans[l[r][0]].append(l[r][1])
    elif l[r][0] in ans and isinstance(ans[l[r][0]], list):
        ans[l[r][0]].append(l[r][1])
    else:
        ans[l[r][0]] = l[r][1]

m = int(input())
for _ in range(m):
    s = input().title()
    if s in ans:
        print(ans[s]) if isinstance(ans[s], str) else print(*ans[s])
    else:
        print("абонент не найден")
