s = input()

if s == 'я' or s == 'Я':
    print('Дальше букв нет')
else:
    print(chr(ord(s)+1))