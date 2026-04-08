sum = 0
min = 10 ** 6
for i in range (10):
    n = int(input())
    if abs(n) <= 10 ** 6:
        if n < 0:
            sum += n
        if n > min and n < 0:
            min = n
if min == 0:
    min = 'NO'
print(sum, min, sep = '\n')