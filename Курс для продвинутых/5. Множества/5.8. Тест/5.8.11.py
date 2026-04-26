m = int(input())
ans = set()
for i in range(m):
    n = int(input())
    ans0 = set()
    for k in range(n):
        s = input()
        ans0.add(s)
    if i == 0:
        ans.update(ans0)
        continue
    else:
        ans &= ans0

for c in sorted(ans):
    print(c)
