import turtle as t

window = t.Screen()


def square(side):
    for _ in range(4):
        t.forward(side)
        t.left(90)


t.left(20)
for _ in range(3):
    square(100)
    t.left(20)

window.mainloop()
