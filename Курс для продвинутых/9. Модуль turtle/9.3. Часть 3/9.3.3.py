import turtle as t
for _ in range(3):
    t.forward(300)
    t.left(120)

t.penup()
t.goto(0, 123.2)
t.pendown()
t.pencolor('white')
for _ in range(3):
    t.right(90)
    t.forward(50)
    t.fillcolor('black')
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    t.penup()
    t.backward(50)
    t.pendown()
    t.left(30)
    t.forward(300)


t.Screen().mainloop()