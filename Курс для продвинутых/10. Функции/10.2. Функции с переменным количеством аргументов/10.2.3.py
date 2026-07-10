def mean(*args):
    s = 0
    n = 0
    for a in args:
        if type(a) in (int, float):
            s += a
            n += 1
        else:
            continue
    return s / n if n != 0 else 0
