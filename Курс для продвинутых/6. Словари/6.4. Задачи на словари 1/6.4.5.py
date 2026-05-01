n = int(input())
ans = {}
l = []

for _ in range(n):
    s = input()
    for i in range(len(s)):
        if s[i] == " ":
            k = i
            break
    l.append([s[:k], s[k + 1 :]])

for m in range(len(l)):
    ans[l[m][0]] = l[m][1].split()

m = int(input())
for _ in range(m):
    s = input()
    for key in ans.keys():
        if s in ans[key]:
            print(key)
