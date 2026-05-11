def generate_password(length):
    import random as rnd

    ans = ""
    for _ in range(length):
        n = rnd.randrange(65, 91)
        m = rnd.randrange(97, 123)
        k = rnd.randint(1, 2)
        if k == 1:
            ans += chr(n)
        elif k == 2:
            ans += chr(m)
    return ans


print(generate_password(10))
