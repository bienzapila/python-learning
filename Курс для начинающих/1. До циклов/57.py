num = int(input())
n = len(str(num))
flag = True
for i in range (1, n+1):
    digit = num // 10 ** (n-i) % 10
    if i == 1:
        last = digit
    if digit > last:
        flag = False
if flag == True:
    print('YES')
else:
    print('NO')