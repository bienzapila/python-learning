s = input().split()
s.insert(0, s[-1])
del s[-1]
print(*s)
