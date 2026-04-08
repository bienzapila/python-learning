# 10n+5k+0.5m=100
n = 100 // 10
k = 100 // 5
m = 100 // 0.5
for i in range(1, n + 1):
    for j in range(1, k + 1):
        for k in range(1, int(m) + 1):
            if 10 * i + 5 * j + 0.5 * k == 100 and i + j + k == 100:
                print(i, j, k)
                print()