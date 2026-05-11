def generate_bingo():
    import random as rnd

    ans = []
    final = []
    for n in range(5):
        for m in range(5):
            if n == m == 2:
                final[n][m] = 0
            else:
                final[n][m] = rnd.randrange(1, 76)
                while final[n][m] not in ans:
                    final[n][m] = rnd.randrange(1, 76)
                ans.append(final[n][m])
    return final


print(generate_bingo())
