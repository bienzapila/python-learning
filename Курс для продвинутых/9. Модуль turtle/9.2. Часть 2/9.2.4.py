import turtle as t
window = t.Screen()

t.shape('turtle')
t.stamp()
t.penup()
n = 10
for _ in range(n):
    t.forward(100)
    t.stamp()
    t.backward(100)
    t.left(360 / n)


window.mainloop()