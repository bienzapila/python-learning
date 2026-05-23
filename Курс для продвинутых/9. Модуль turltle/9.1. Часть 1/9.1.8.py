import turtle as t

window = t.Screen()


def figure(side):
    for i in range(4):
        if i % 2 == 0:
            t.forward(side)
            t.left(60)
        else:
            t.forward(side)
            t.left(120)


figure(100)
window.mainloop()
