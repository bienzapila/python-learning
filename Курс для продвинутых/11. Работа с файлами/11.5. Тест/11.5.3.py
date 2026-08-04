with open(input()) as file:
    count = 0
    for line in file.readlines():
        line_list = line.rstrip('\n').split()
        flag = True
        for i in range(1, 4):
            if int(line_list[i]) < 65:
                flag = False
        if flag:
            count += 1

print(count)
