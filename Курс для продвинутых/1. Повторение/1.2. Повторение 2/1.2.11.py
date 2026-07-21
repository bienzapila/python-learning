line = [input(), 'запретил', 'букву']

letters = [
    "а",
    "б",
    "в",
    "г",
    "д",
    "е",
    "ж",
    "з",
    "и",
    "й",
    "к",
    "л",
    "м",
    "н",
    "о",
    "п",
    "р",
    "с",
    "т",
    "у",
    "ф",
    "х",
    "ц",
    "ч",
    "ш",
    "щ",
    "ъ",
    "ы",
    "ь",
    "э",
    "ю",
    "я",
]

for letter in letters:
    line_join = '+'.join(line)
    if letter in line_join:
        print(*line, letter)
    else:
        continue
    
    new_line_join = ''
    for symbol in line_join:
        if symbol != letter:
            new_line_join += symbol

    line = new_line_join.strip('+').split('+')
    
    new_line = []
    for i in range(len(line)):
        if line[i] != '':
            new_line.append(line[i])
    line = new_line




            
