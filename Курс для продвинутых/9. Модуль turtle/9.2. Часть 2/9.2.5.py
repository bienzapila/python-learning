import turtle as t
window = t.Screen()

t.Screen().bgcolor('blue')
t.shape('turtle')
t.stamp()
t.penup()
n = 12
for _ in range(n):
    t.forward(70)
    t.pendown()
    t.forward(20)
    t.penup()
    t.forward(10)
    t.stamp()
    t.backward(100)
    t.left(360 / n)


window.mainloop()