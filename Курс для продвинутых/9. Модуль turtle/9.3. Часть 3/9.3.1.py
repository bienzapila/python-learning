import turtle as t
window = t.Screen()

t.fillcolor('blue')
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

t.penup()
t.goto(-30, 100)
t.pendown()

t.fillcolor('brown')
t.begin_fill()
for _ in range(3):
    t.forward(160)
    t.left(120)
t.end_fill()

window.mainloop()