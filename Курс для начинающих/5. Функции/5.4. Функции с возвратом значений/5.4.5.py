def get_factors(num):
    sp = []
    for i in range(1, num + 1):
        if num % i == 0:
            sp.append(i)
    return sp
