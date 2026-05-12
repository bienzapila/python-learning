def generate_bingo():
    import random as rnd

    ans = [[0] * 5 for _ in range(5)]
    num = set()
    bum = []
    while len(num) != 24:
        num.add(rnd.randrange(1, 76))
    num = sorted(list(num))
    i = 0
    for n in range(5):
        for m in range(5):
            if n == m == 2:
                continue
            else:
                ans[n][m] = num[i]
                i += 1
    return ans


print(generate_bingo())
