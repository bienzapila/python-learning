import random as rnd

s0 = 4
n = int(input())
k = 0
for _ in range(n):
    x, y = rnd.uniform(-1, 1), rnd.uniform(-1, 1)
    if x**2 + y**2 <= 1:
        k += 1
print(round(k / n * s0, 4))
