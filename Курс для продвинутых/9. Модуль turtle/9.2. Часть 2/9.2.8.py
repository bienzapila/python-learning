import turtle as t
window = t.Screen()

def triangle():
    for _ in range(3):
        t.forward(100)
        t.left(120)

triangle()
t.penup()
t.goto(0, 66.6)
t.pendown()
t.right(60)
triangle()


window.mainloop()