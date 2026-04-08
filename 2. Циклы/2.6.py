# 28n+30k+31m=365.
n = 365 // 28
k = 365 // 30
m = 365 // 31
for i in range(1, n + 1):
    for j in range(1, k + 1):
        for k in range(1, m + 1):
            if 28 * i + 30 * j + 31 * k == 365:
                print(i, j, k)
                print()