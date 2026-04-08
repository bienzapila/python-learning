count = 0
total = 1
while True:
    n = int(input())
    total += 1
    if len(str(n)) > 7:
        count += 1
    if n % 100 == 11:
        break
print(count, '/', total, sep ='')