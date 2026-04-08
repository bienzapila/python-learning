sum = 0
sp = ("1 10 15 2").split()
print(sp)
n = 0
for i in range(len(sp) - 1, -1, -1):
    sum += int(sp[n]) * 16**i
    n += 1

print(sum)
