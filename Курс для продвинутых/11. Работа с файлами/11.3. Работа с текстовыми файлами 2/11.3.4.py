with open(input()) as file:
    for line in map(lambda line: line.rstrip('\n').split(), file.readlines()):
        print(sum(map(int, line)))