with open(input()) as file:
    lines = file.readlines()

    for i in range(len(lines) - 1, -1, -1):
        print(lines[i].rstrip('\n'))