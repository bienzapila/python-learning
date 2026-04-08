num = int(input())
n = len(str(num))
sum = 0
count = 0
pr = 1
for i in range (1, n+1): 
    digit = num // 10 ** (n - i) % 10
    sum += digit
    count += 1
    pr *= digit
    if i == 1:
        digit1 = digit
    if i == n:
        digitlast = digit
avg = sum / count
print(sum, count, pr, avg, digit1, digitlast + digit1, sep ='\n')