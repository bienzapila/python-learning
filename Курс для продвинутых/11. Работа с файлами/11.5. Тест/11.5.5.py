with open(input()) as file:
    lines = list(map(lambda x: x.rstrip('\n'), file.readlines()))
    if len(lines) >= 10:
        for i in range(-10, 0):
            print(lines[i])
    else:
        for line in lines:
            print(line)