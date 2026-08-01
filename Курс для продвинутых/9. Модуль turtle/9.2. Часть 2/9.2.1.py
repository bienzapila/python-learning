import turtle as t
window = t.Screen()

t.shape('square')
for _ in range(10):
    t.dot()
    t.penup()
    t.forward(10)
    t.pendown()

window.mainloop()