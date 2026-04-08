n = int(input())

one = 0
two = 0
three = 0
four = 0

for i in range(n):
    s = input().split()

    if int(s[0]) > 0:
        if int(s[1]) > 0:
            one += 1
        elif int(s[1]) < 0:
            four += 1
    elif int(s[0]) < 0:
        if int(s[1]) > 0:
            two += 1
        elif int(s[1]) < 0:
            three += 1

print(f"Первая четверть: {one}")
print(f"Вторая четверть: {two}")
print(f"Третья четверть: {three}")
print(f"Четвертая четверть: {four}")
