import turtle as t

window = t.Screen()
for i in range(0, 361, 30):
    t.forward(100)
    t.backward(100)
    t.setheading(i)
window.mainloop()
