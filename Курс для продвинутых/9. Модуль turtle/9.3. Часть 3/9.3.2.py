import turtle as t

t.fillcolor('black')
t.begin_fill()
for _ in range(2):
    t.forward(100)
    t.left(90)
    t.forward(200)
    t.left(90)
t.end_fill()

colors = ['green', 'yellow', 'red']
t.penup()
t.goto(50, 20)
t.pendown()
for color in colors:
    t.fillcolor(color)
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    t.penup()
    t.goto(50, t.ycor() + 55)
    t.pendown()



t.Screen().mainloop()