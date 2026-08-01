dict_prod = {}
for _ in range(int(input())):
    dict_prod[input()] = ['–', '–', '–']

filenames = ['desyatochka.txt', 'kubit.txt', 'polosa.txt']
for i in range(len(filenames)):
    with open(filenames[i]) as file:
        for line in file:
            list_line = line.rstrip('\n').split(': ')
            if list_line[0] in dict_prod:
                dict_prod[list_line[0]][i] = int(list_line[1])


dict_rel = {0: 'Десяточка', 1: 'Кубит', 2: 'Полоса'}
dict_shop = {'Десяточка': [], 'Кубит': [], 'Полоса': []}
for key in dict_prod.keys():
    dict_shop[dict_rel[dict_prod[key].index(min(map(lambda x: x if isinstance(x, int) else 1000, dict_prod[key])))]].append(key)

for key in dict_shop.keys():
    if len(dict_shop[key]) == 0:
        print(f'{key}:')
        print('–')
    else:
        print(f'{key}:')
        print(*dict_shop[key], sep=', ')