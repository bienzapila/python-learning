def print_products(*args):
    ans = []
    for a in args:
        if a not in (list, tuple, set, dict):
            if type(a) == str and a != '':
                ans.append(a)
        else:
            if a is not dict:
                for k in a:
                    if type(k) == str and k != '':
                        ans.append(k)
            else:
                for s in a.keys():
                    if type(a[s]) == str and a[s] != '':
                        ans.append(a[s])

    if len(ans) > 0:
        n = 1
        for m in ans:
            print(f'{n}) {m}')
            n += 1
    else:
        print('Нет продуктов')