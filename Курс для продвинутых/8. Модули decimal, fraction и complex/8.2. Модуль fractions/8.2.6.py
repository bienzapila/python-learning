from math import factorial as fact
from fractions import Fraction as f

n = int(input())
ans = 0
for i in range(1, n + 1):
    ans += f(f"1/{fact(i)}")

print(ans)
