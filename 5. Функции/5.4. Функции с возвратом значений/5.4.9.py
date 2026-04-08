def find_all(target, symbol):
    sp = []
    for i in range(len(target)):
        if target[i] == symbol:
            sp.append(i)
    return sp
