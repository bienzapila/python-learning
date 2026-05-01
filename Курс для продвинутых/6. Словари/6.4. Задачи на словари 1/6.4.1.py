n = int(input())
l = []
for _ in range(n):
    s = input()
    for i in range(len(s)):
        if s[i] == ":" or s[i] == " ":
            k = i
            break
    l.append([s[:k].lower(), s[k + 2 :]])

ans = {}
for m in range(len(l)):
    ans[l[m][0]] = l[m][1]

r = int(input())
for _ in range(r):
    sp = input().lower()
    if sp in ans:
        print(ans[sp])
    else:
        print("Не найдено")
