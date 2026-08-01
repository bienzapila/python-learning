ans_dict = {}
for _ in range(int(input())):
    input_file = input()
    with open(input_file) as file:
        length = 0
        for line in file:
            line.replace('\n', 'aa')
            print(line)
            length += len(line)
        ans_dict[input_file] = length

print(ans_dict)