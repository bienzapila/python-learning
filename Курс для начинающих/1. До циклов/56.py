num = int(input())
n = len(str(num))
count = 0
a = 0
for i in range (1, n+1):
    digit = num // 10 ** (n-i) % 10
    if digit % 2 == 0:
        a += 1
        print(a, '-я четная цифра равна ', digit, sep ='')
if a == 0:
    print('Четных цифр в числе нет')