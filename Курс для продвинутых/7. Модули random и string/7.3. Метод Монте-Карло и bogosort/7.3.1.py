import random as rnd

n = int(input())
s0 = 16
k = 0
for _ in range(n):
    x = rnd.uniform(-2, 2)
    y = rnd.uniform(-2, 2)
    if -2 <= x <= 2 and -2 <= y <= 2 and x**3 + y**4 + 2 >= 0 and 3 * x + y**2 <= 2:
        k += 1
print(round(k / n * s0, 1))
