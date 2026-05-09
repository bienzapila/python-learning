s = "3:animal 4:house 8:tree 2:color 21:moon 31:fire 12:ship"
s = s.split()
for i in range(len(s)):
    s[i] = s[i].split(":")

ans = {int(c[0]): c[1] for c in s}
print(ans)
