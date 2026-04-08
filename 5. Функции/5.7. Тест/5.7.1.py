def draw_triangle():
    cnt = 1
    spc = 7
    for i in range(8):
        print(" " * spc + "*" * cnt)
        cnt += 2
        spc -= 1


draw_triangle()
