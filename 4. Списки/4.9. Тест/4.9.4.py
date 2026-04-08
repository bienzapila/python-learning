s = input().split()
ma = 0

for sp in s:
    if len(sp) > ma:
        ma = len(sp)

print(ma)
