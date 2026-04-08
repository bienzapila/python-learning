n = int(input())
a = -1
sum = 1
for i in range(2, n + 1):
    sum += a * i
    a = -a
print(sum)
