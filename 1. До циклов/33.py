a, b = int(input()), int(input())
count = 0
for _ in range(a, b + 1):
    if _ ** 3 % 10 == 4 or _ ** 3 % 10 == 9:
        count += 1
print(count)