a = input()
count = 0
for i in range(len(a)):
    c = a.count(a[i])
    if c >= count:
        count = c
        n = a[i]
    c = 0
print(n)