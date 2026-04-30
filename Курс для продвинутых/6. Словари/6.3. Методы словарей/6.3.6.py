text = "bridge snake island game glory eye arrogant car nature game glory game"
l = text.split()
d = {}
for lp in l:
    d[lp] = l.count(lp)

ans = list()
for key in d.keys():
    if d[key] == max(d.values()):
        ans.append(key)

print(min(ans))
