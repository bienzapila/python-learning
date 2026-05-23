import turtle as t

window = t.Screen()


def square(side):
    for _ in range(4):
        t.forward(side)
        t.left(90)


for i in range(100, 0, -5):
    side = i
    square(side)
window.mainloop()
