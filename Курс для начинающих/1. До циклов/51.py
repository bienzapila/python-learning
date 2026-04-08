a = int(input())
while a != 0:
    last_digit = a % 10
    print(last_digit, end = '')
    a //= 10