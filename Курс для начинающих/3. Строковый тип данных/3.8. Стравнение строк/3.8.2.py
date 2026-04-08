max = ''
min = 'яяяяяяяяяяя'

while True:
    s = input()
    if s == 'КОНЕЦ':
        break
    if s >= max:
        max = s
    if s <= min:
        min = s

print(f'Минимальная строка ⬇️: {min}')
print(f'Максимальная строка ⬆️: {max}')