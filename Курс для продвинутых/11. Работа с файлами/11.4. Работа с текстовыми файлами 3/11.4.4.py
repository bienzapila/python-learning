def add_five(file_name):
    with open(file_name) as file, open('new_scores.txt', 'w') as output:
        length = len(file.readlines())
        file.seek(0)
        for _ in range(length):
            line_list = file.readline().rstrip('\n').split()
            line_list[1] = str(min(100, int(line_list[1]) + 5))
            line = ' '.join(line_list) + '\n'
            output.write(line)