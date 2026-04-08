def drew_triangle(fill, base):
    for i in range(1, base // 2 + 1):
        print(fill * i)
    for i in range(base // 2 + 1, 0, -1):
        print(fill * i)
