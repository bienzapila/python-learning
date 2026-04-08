n = int(input())

for i in range(n):
    s = input()
    digit = ''
    alpha = ''

    for k in range(len(s)):
        if s[k].isdigit():
            digit += s[k]

    for k in range(len(s)):
        if s[k].isalpha():
            alpha += s[k]


    only_digits_and_alpha = (len(digit) + len(alpha) == len(s))

    if (only_digits_and_alpha
            and len(alpha) == 1 
            and 'А' <= alpha <= 'П'
            and alpha != 'Ё'
            and len (digit) == 1):
        print('YES')
    else:
        print('NO')
