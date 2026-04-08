a = input()
plus = 0
star = 0
for i in range(len(a)):
    if a[i] in '+':
        plus += 1
    elif a[i] in '*':
        star += 1
print('Символ + встречается', plus, 'раз')
print('Символ * встречается', star, 'раз')