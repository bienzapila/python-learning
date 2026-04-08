s = input()
a = s.split()
for i in range(len(a)):
    a[i] = int(a[i])

a.sort()
print(*a)
a.sort(reverse=True)
print(*a)
