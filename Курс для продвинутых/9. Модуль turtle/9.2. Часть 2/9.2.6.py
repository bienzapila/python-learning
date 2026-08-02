import turtle as t
window = t.Screen()
t.shape('turtle')
t.stamp()
t.penup()
step = 10
for _ in range(50):
    t.stamp()
    t.right(22)
    t.forward(step)
    step += 2


window.mainloop()