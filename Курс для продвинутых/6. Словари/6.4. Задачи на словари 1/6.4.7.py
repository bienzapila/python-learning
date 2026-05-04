m = input()
m1 = set(m)
ans1 = {}
for s in m1:
    ans1[s] = m.count(s)

n = int(input())
ans2 = {}
for _ in range(n):
    s = input().split(": ")
    ans2[s[0]] = int(s[1])

for key2 in ans2.keys():
    for key1 in ans1.keys():
        if ans2[key2] == ans1[key1]:
            m = m.replace(key1, key2)

print(m)
