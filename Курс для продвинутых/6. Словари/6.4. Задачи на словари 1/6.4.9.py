s = input().split()
base = {}
ans = []
for sp in s:
    if sp not in ans:
        ans.append(sp)
        base[sp] = 0
    else:
        base[sp] += 1
        ans.append(f"{sp}_{base[sp]}")

print(*ans)
