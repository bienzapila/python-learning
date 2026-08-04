with open(input()) as file:
    revenue = 0
    for line in file.readlines():
        revenue += int(line.rstrip('\n')[1:])

print(f'${revenue}')