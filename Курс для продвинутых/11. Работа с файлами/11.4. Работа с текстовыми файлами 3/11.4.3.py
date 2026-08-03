def numbering_write(file_name):
    with open(file_name) as file, open('output.txt', 'w') as output:
        length = len(file.readlines())
        file.seek(0)
        for i in range(length):
            output.write(f'{i+1}) {file.readline()}')