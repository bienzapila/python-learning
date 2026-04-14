s = input().split()
for i in range(len(s)):
    s[i] = s[i].lstrip("0")
a = set()

for sn in s:
    if sn in a:
        print("YES")
    else:
        print("NO")
    a.add(sn)
