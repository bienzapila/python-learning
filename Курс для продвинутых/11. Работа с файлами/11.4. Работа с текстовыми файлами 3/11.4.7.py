def write_long_session_users(file_name):
    with open(file_name) as file, open('output.txt', 'w') as output:
        for line in file.readlines():
            line_list = line.rstrip('\n').split(', ')
            ent = list(map(lambda x: int(x), line_list[1].split(':')))
            ex = list(map(lambda x: int(x), line_list[2].split(':')))

            if ex[0] - ent[0] >= 2:
                output.write(f'{line_list[0]}\n')
            elif ex[0] - ent[0] == 1:
                if ex[1] >= ent[1]:
                    output.write(f'{line_list[0]}\n')