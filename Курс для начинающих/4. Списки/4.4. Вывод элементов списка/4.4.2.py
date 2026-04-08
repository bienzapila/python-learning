n = int(input())
sp = []

for i in range(n):
    s = input()
    if s not in sp:
        sp.append(s)

print(*sp, sep = '\n')