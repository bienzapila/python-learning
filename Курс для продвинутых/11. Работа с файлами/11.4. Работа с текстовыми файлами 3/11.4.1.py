def write_line(file_name):
    with open(file_name) as file:
        line = file.readline()
    with open('output.txt', 'w') as file:
        file.write(line)
