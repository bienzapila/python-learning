l = input().split()
m = input().split()

sp = [int(l[i]) + int(m[i]) for i in range(len(l))]
print(*sp)
