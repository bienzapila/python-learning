with open(input()) as file:
    len_max = max(map(len, file.readlines()))
    file.seek(0)

    lines = file.readlines()
    for line in lines:
        if len(line) == len_max:
            print(line.rstrip('\n'))
