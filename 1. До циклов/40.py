count = 0
for i in range(1, 11):
    num = int(input())
    if num % 2 != 0:
        count += 1
if count == 0:
    print('YES')
else:
    print('NO')