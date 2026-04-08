def print_symbol_counts(s):
    s = list(s.lower())
    s.sort()
    flag = ""
    for sp in s:
        if sp in flag:
            continue
        else:
            print(f"{sp}: {s.count(sp)}")
            flag += sp
