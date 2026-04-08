num = int(input())
n = len(str(num))
count = 0
for i in range (1, n+1):
    digit = num // 10 ** (n-i) % 10
    if i == 1:
        last = digit
    if digit == last:
        count += 1
if count == n:
    print('YES')
else:
    print('NO')