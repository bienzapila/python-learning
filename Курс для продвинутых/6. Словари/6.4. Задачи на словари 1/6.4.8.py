s = input()
s1 = ""
for sp in s:
    if sp.isalpha() or sp == " ":
        s1 += sp.lower()

s1 = s1.split()
ans = {}
for sp in s1:
    ans[sp] = s1.count(sp)

k = min(ans.values())
b = []
for key in ans.keys():
    if ans[key] == k:
        b.append(key)

print(min(b))
