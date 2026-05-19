import turtle as t

window = t.Screen()


def square(side):
    for _ in range(4):
        t.forward(side)
        t.left(90)


t.left(45)
for _ in range(8):
    square(100)
    t.left(45)

window.mainloop()
