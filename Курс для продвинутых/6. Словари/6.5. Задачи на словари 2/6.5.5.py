def dict_diff(data1, data2):
    for key1 in data1.keys():
        for key2 in data2.keys():
            if key1 == key2:
                if data1[key1] == data2[key2]:
                    return 'unchanged'
                else:
                    return 'changed'
        else:
            key2