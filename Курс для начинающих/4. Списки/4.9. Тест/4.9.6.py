num = input()
flag = False

if num.count('-') == 2 or num.count('-') == 3:
    num_split = num.split('-')

    if num_split[0] == '7' and len(num_split) == 4:
        for i in range(1, 4):
            if i < 3:
                if len(num_split[i]) != 3 or not num_split[i].isdigit():
                    break
            else:
                if len(num_split[3]) != 4 or not num_split[i].isdigit():
                    break
        else:
            flag = True
    elif len(num_split) == 3:
        for i in range(0, 3):
            if i < 2:
                if len(num_split[i]) != 3 or not num_split[i].isdigit():
                    break
            else:
                if len(num_split[2]) != 4 or not num_split[i].isdigit():
                    break
        else:
            flag = True
            
print('YES') if flag else print('NO')