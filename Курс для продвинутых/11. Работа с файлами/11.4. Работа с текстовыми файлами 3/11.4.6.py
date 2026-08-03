def concatenate_files(*args):
    file = open('output.txt', 'w')
    file.close()

    for arg in args:
        with open(arg) as file, open('output.txt', 'a') as output:
            for line in file.readlines():
                output.write(line)