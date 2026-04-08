n = int(input())
sp = []
num = []

for i in range(n):
    s = int(input())
    sp.append((s+1)**2)
    num.append(s)

print(*num, sep ='\n')
print()
print(*sp, sep ='\n')