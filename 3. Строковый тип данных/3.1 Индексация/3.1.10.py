n = int(input())
sum =''
while n >0:
    a = n % 2
    n //= 2
    sum += str(a)
sum = str(sum)
for i in range(len(sum)-1, -1, -1):
    print(sum[i], end='')