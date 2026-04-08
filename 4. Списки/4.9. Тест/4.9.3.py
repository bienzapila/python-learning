s = input().split()
summa = 0

for num in s:
    summa += int(num)


print(f'{"+".join(s)}={summa}')
