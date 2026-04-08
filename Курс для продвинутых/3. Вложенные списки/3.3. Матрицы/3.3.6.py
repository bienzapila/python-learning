n = int(input())
mtrx = []

for _ in range(n):
    mtrx.append(input().split())

up = 0
right = 0
low = 0
left = 0

for i in range(len(mtrx)):
    for j in range(len(mtrx[0])):
        if i > j:
            if i < n - 1 - j:
                left += int(mtrx[i][j])
            elif i > n - 1 - j:
                low += int(mtrx[i][j])
        elif i < j:
            if i < n - 1 - j:
                up += int(mtrx[i][j])
            elif i > n - 1 - j:
                right += int(mtrx[i][j])

print(f"Верхняя четверть: {up}")
print(f"Правая четверть: {right}")
print(f"Нижняя четверть: {low}")
print(f"Левая четверть: {left}")
