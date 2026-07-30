with open(input()) as file:
    countries = {}
    for row in file.readlines():
        row_new = row.rstrip('\n').split('\t')
        ''.join(row_new[1].split('_'))
        countries[row_new[0]] = int(row_new[1])

    for key in countries.keys():
        if key.startswith('G') and countries[key] >= 500000:
            print(key)