ans_list = []
for _ in range(int(input())):
    input_file = input()
    with open(input_file) as file:
        lines = file.read().replace('\n', '  ')
    ans_list.append((len(lines), input_file))

values_sorted = sorted(ans_list, key=lambda x: (-x[0], x[1]))
for value in values_sorted:
    print(f'{value[1]} {value[0]}B')