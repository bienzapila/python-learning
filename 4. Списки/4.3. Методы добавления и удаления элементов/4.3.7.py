n = int(input())
sp = []

for i in range(n):
    s = input()
    sp.append(s)

k = int(input())-1
ans = ''

for i in range(len(sp)):
    if len(sp[i]) - 1 >= k:
        ans += sp[i][k]

print(ans)