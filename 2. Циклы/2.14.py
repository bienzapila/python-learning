a, b = int(input()), int(input())
sum = 0
flag = 0
for c in range(a, b+1):
    flag = 0
    for i in range (1, c+1):
        if c % i == 0:
            flag += i
    if flag >= sum:
        sum = flag
        num = c
print(num, sum,)