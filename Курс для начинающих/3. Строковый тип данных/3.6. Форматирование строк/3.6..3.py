date = int(input())
weight = float(input())
ed = 12 / 60
goal = 100 - date * ed

if date * ed > 100 - weight:
    print('Что-то пошло не так')
    print(f'#{date} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {goal} кг')
else:
    print('Все идет по плану')    
    print(f'#{date} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {goal} кг')