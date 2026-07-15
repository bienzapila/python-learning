import turtle as t

window = t.Screen()


def triangle(side):
    for _ in range(3):
        t.forward(side)
        t.left(120)


triangle(200)

window.mainloop()
