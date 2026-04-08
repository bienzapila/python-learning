for i in range(40):
    for k in range(40):
        for l in range(40):
            for m in range(40):
                    if i ** 3 + k ** 3 == l ** 3 + m ** 3 and i != k and i != l and i!= m and k != l and k != m and m!= l:
                         print(i, k, l, m, i ** 3 + k ** 3)
