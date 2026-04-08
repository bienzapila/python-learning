s = input()
cost = 0

for i in range(len(s)):
    cost += ord(s[i])

print(f'Старая стоимость: {cost * 3}🐝')

eng = list('eyopaxcETOPAHXCBM')
rus = list('еуорахсЕТОРАНХСВМ')
s = list(s)

for i in range(len(s)):
    for c in range(len(eng)):
        if s[i] == eng[c]:
            s[i] = rus[c]
''.join(s)

cost = 0
for i in range(len(s)):
    cost += ord(s[i])

print(f'Новая стоимость: {cost * 3}🐝')
