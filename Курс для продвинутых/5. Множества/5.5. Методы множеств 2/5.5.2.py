s1, s2 = input().split(), input().split()

for i in range(len(s1)):
    s1[i] = int(s1[i])
for i in range(len(s2)):
    s2[i] = int(s2[i])
s1, s2 = set(s1), set(s2)

print(*(sorted(s1 & s2)))
