correct = 0
wrong = 0
correct_users = set()
for _ in range(int(input())):
    line_split = input().split(': ')

    if line_split[1] == 'Correct':
        correct += 1
        correct_users.add(line_split[0])
    else:
        wrong += 1

def true_round(num):
    number = num
    while num >= 1:
        num -= 1
    
    if num >= 0.5:
        return round(number + 0.5)
    else:
        return round(number)

if correct != 0:
    print(f'Верно решили {len(correct_users)} учащихся')
    print(f'Из всех попыток {true_round((correct/(correct+wrong)) * 100)}% верных')
else:
    print('Вы можете стать первым, кто решит эту задачу')
