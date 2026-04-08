def get_last_index(data, value):
    count = -1
    for i in range(len(data)):
        if data[i] == value:
            count = i
    if count == -1:
        return "ERROR!"
    else:
        return count
