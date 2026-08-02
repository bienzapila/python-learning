import turtle as t
window = t.Screen()
t.pencolor('red')
t.dot()
for i in range(-200, 210, 50):
    t.pencolor('green')
    t.goto(i, -200)
    t.pencolor('blue')
    t.dot()
    t.penup()
    t.goto(0, 0)
    t.pendown()
t.mainloop()