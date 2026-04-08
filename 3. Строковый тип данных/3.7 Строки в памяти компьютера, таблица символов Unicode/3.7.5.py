s = input()
cost = 0

for i in range(len(s)):
    cost += ord(s[i])

print(f"Текст сообщения: '{s}'")
print(f'Стоимость сообщения: {cost * 3}🐝')