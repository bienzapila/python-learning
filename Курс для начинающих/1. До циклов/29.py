m, p, n = int(input()), int(input()), int(input())
p = p / 100
n = n - 1
print(1, m)
for i in range(n):
    m = m * (1 + p)
    print(i + 2, m)
