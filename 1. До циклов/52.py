a = int(input())
ma = 0
mi = 10
while a != 0:
    last_digit = a % 10
    if last_digit > ma:
        ma = last_digit
    if last_digit < mi:
        mi = last_digit
    a //= 10
print('Максимальная цифра равна', ma)
print('Минимальная цифра равна', mi)