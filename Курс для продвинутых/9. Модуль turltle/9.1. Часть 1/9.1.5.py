import turtle as t

window = t.Screen()


def hexagon(side):
    for _ in range(6):
        t.forward(side)
        t.left(60)


hexagon(100)


window.mainloop()
