a, b = int(input()), int(input())

ans = []
for n in range(a, b+1):
    a = []
    if '0' in str(n):
        continue
    for s in str(n):
        if n % int(s) == 0:
            a.append(True)
        else:
            a.append(False)
    if all(a):
        ans.append(n)

print(*ans)


