n = int(input())
s1 = set()

for _ in range(n):
    s = set(input())
    if _ == 0:
        s1.update(s)
    else:
        s1 = s1 & s

s1 = list(s1)
for i in range(len(s1)):
    s1[i] = int(s1[i])

print(*sorted(set(s1)))
