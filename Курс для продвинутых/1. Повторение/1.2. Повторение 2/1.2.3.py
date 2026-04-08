s = input().split()

for i in range(0, len(s), 2):
    if len(s) % 2 == 1 and i == len(s) - 1:
        break
    s[i], s[i + 1] = s[i + 1], s[i]

print(*s)
