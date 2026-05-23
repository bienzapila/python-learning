import turtle as t

window = t.Screen()


def hexagon(side):
    for _ in range(6):
        t.forward(side)
        t.left(60)


hexagon(100)
t.right(120)
hexagon(100)
t.right(120)
hexagon(100)

t.setheading(0)
t.forward(100)
t.right(60)
hexagon(100)

t.setheading(60)
t.forward(100)
t.setheading(0)
hexagon(100)

t.setheading(120)
t.forward(100)
t.setheading(180)
t.forward(100)
t.setheading(0)
hexagon(100)

t.setheading(120)
hexagon(100)


window.mainloop()
