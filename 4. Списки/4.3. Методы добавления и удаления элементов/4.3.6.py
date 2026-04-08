n = int(input())
sp = []

for i in range(n):
    s = int(input())
    sp.append(s)

del sp[1::2]

print(sp)