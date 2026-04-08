a, b, c, d = input(), input(), input(), input()
suma = 0
sumb = 0
sumc = 0
sumd = 0
sum = 0

for i in range(len(b)):
    sumb += ord(b[i])
for i in range(len(a)):
    suma += ord(a[i])
for i in range(len(c)):
    sumc += ord(c[i])
for i in range(len(d)):
    sumd += ord(d[i])

list = [suma, sumb, sumc, sumd]
sum = max(list)
if sum == suma:
    print(a)
elif sum == sumb:
    print(b)
elif sum == sumc:
    print(c)
else:
    print(d)
