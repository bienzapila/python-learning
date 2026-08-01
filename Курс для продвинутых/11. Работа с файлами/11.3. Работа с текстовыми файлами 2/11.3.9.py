def read_csv(csv_file):
    with open(csv_file) as file:
        data = []
        for line in file:
            data.append(line.rstrip('\n').split(','))

        ans = []
        for n in range(1, len(data)):
            data_person = {}
            for i in range(len(data[0])):
                data_person[data[0][i]] = data[n][i]
            ans.append(data_person)
    return ans