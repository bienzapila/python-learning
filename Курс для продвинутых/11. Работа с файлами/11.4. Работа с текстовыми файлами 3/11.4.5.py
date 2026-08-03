def fresco_goats(file_name):
    with open(file_name) as file, open('answer.txt', 'w') as answer:
        file.readline()
        count = 0
        colors_dict = {}
        line = file.readline().rstrip('\n')
        while line != 'GOATS':
            if line != 'GOATS':
                colors_dict[line] = 0
            line = file.readline().rstrip('\n')
        line = file.readline().rstrip('\n')
        while line != '':
            if line != '':
                colors_dict[line] += 1
                count += 1
            line = file.readline().rstrip()

        ans_list = []
        for key in colors_dict.keys():
            if colors_dict[key] / count > .07:
                ans_list.append(key)
        for key in sorted(ans_list):
            answer.write(f'{key}\n')

        