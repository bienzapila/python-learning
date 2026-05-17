n = int(input())
from math import gcd
from fractions import Fraction as F

ans = 0
k = n - 1
for i in range(1, n + 1):
    if gcd(i, k) == 1 and F(f"{i}/{k}") > ans and i < k:
        ans = F(f"{i}/{k}")
    k -= 1


print(ans)
