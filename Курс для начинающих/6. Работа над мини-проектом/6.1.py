from math import log2, ceil

n = int(input())
print(ceil(log2(n + 1)) if n != 1 else 1)
