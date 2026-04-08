n = int(input())
three = 0
last = n % 10 
countl = 0
even = 0
sum5 = 0
prod7 = 1
count05 = 0
while n > 0:
    nn = n % 10
    if nn == 3:
        three += 1
    if nn == last:
        countl += 1
    if nn % 2 == 0:
        even += 1
    if nn > 5:
        sum5 += nn
    if nn > 7:
        prod7 *= nn
    if nn == 5 or nn == 0:
        count05 += 1
    n //= 10
print(three, countl, even, sum5, prod7, count05, sep ='\n')