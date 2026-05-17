n = int(input())
from fractions import Fraction as F

final = set()
for i in range(2, n + 1):
    for k in range(1, i):
        final.add(F(f"{k}/{i}"))
print(*sorted(list(final)), sep="\n")
