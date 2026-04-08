num = int(input())
n = len(str(num))
for i in range (1, n+1):
    digit = num // 10 ** (n - i) % 10
    if i == 2:
        a = digit
print(a)