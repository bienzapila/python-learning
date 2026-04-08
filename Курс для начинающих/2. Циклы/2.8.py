for i in range (1, 151):
    for j in range (i, 151):
        for k in range (j, 151):
            for l in range (k, 151):
                for m in range (l, 151):
                    if i ** 5 + j ** 5 + k ** 5 + l ** 5 == m ** 5:
                        print (i, j, k, l, m)
